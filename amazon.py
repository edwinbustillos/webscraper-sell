from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

def configurar_chrome():
    """Configura as opções do Chrome e retorna o driver"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executa em modo headless (sem interface gráfica)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    # Inicializa o driver do Chrome usando o webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


def extrair_informacoes_produto(url):
    """Extrai título e preço do produto do Mercado Livre"""
    driver = configurar_chrome()
    
    try:
        # Acessa a URL
        driver.get(url)
        
        # Aguarda a página carregar (máximo 10 segundos)
        wait = WebDriverWait(driver, 10)
        
        # Extrai o título
        titulo = wait.until(EC.presence_of_element_located((
            By.ID, "productTitle"))).text.strip()
        
        # Extrai o preço
        # Tenta diferentes seletores para o preço, já que a Amazon pode ter variações
        try:
            # Primeiro tenta o preço normal
            preco = wait.until(EC.presence_of_element_located((
                By.CLASS_NAME, "a-price-whole"))).text
            
            # Tenta pegar os centavos
            centavos = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
            preco_completo = f"${preco}.{centavos}"
            
        except:
            # Se não encontrar no formato anterior, tenta outro seletor comum
            try:
                preco_completo = wait.until(EC.presence_of_element_located((
                    By.CLASS_NAME, "a-offscreen"))).get_attribute("textContent")
            except:
                preco_completo = "Preço não disponível"
        
        return {
            "titulo": titulo,
            "preco": preco_completo
        }
        
    except Exception as e:
        print(f"Erro ao extrair informações: {str(e)}")
        return None
        
    finally:
        driver.quit()

def main():
    url = "https://www.amazon.com.br/dp/B09B2TSNNN"
    resultado = extrair_informacoes_produto(url)
    
    if resultado:
        print("Informações extraídas com sucesso:")
        print(f"Título: {resultado['titulo']}")
        print(f"Preço: {resultado['preco']}")
        
        # Salva as informações em um arquivo JSON
        with open("produto.json", "w") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=4)
    else:
        print("Não foi possível extrair as informações.")

if __name__ == "__main__":
    main()