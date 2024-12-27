# Web Scraper Sell
Este projeto é um web scraper que extrai informações de produtos de sites como Mercado Livre e Amazon.

## Configuração do Ambiente
### Requisitos
- Python 3.11
- `venv` para criação de ambientes virtuais

### Passos para Configuração
1. **Clone o repositório:**
    ```sh
    git clone https://github.com/seu-usuario/webscraper-sell.git
    cd webscraper-sell
    ```

2. **Crie um ambiente virtual:**
    ```sh
    python3.11 -m venv meuambiente
    ```

3. **Ative o ambiente virtual:**
    - No macOS/Linux:
        ```sh
        source meuambiente/bin/activate
        ```
    
    - No Windows:
        ```sh
        .\meuambiente\Scripts\activate
        ```

4. **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

### Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de que o arquivo contém as seguintes bibliotecas:

```txt
selenium
webdriver_manager
```
- Ou instale individualmente:
```
pip install selenium
pip install webdriver_manager
```

## Executando o Projeto
Para executar o projeto, utilize o comando:
```
python mercadolivre.py
```
ou
```
python amazon.py
```
OBS: Não esqueça de alterar 'URL' pelo path do anuncio.

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.