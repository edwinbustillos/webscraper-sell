from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
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
        titulo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-pdp-title"))).text
        
        # Extrai o preço
        # Primeiro, tenta localizar o elemento do preço principal
        preco = wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, "andes-money-amount__fraction"))).text
        
        # Formata o preço (adiciona R$ e formata com vírgula)
        preco_formatado = f"R$ {preco}"
        
        return {
            "titulo": titulo,
            "preco": preco_formatado
        }
        
    except Exception as e:
        print(f"Erro ao extrair informações: {str(e)}")
        return None
        
    finally:
        driver.quit()

def main():
    url = "https://www.mercadolivre.com.br/samsung-galaxy-s23-256-gb-5g-preto-8-gb-ram/p/MLB21436188"
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