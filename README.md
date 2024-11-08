# automation_project
Este projeto é o trabalho final da disciplina de Automação de testes da pós-graduação de Engenharia de Qualidade e Teste de Software.

O projeto contém o teste automatizado de interface usando Python, Selenium Webdriver e o padrão Page Object Model.

## Requisitos
**Python** 3.11

**pip** (24.3.1)

**venv** (recomendado)

## Instalação 
1. Realize o clone ou download deste projeto.
2. Na pasta principal, realize os comandos abaixo para criar um ambiente virtual e depois ativá-lo:
   
   ```
   python -m venv .venv
   ```
   
   ```
   .\venv\Scripts\activate
   ```
   
4. Instale as dependências do projeto, com o comando:

   ```
   pip install -r requirements.txt
   ```

6. Utilize o comando abaixo para executar o teste:
   
   ```
   python -m pytest -k test_demo.py
   ```
   
