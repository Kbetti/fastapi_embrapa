# fastapi_embrapa

Este é um projeto de API desenvolvido com **FastAPI**, voltado para o mercado de uvas e vinhos. O deploy foi realizado utilizando **Vercel** para garantir alta performance e acessibilidade.

---

## 🚀 Funcionalidades

- **Autenticação JWT**: Proteção de rotas sensíveis com tokens de autenticação.
- **Previsão de Produção e Exportação**: Modelos de Machine Learning para prever a produção de uvas e a demanda de vinhos.
- **API de Dados**: Exposição de dados sobre a produção, importação e exportação de vinhos.
- **Documentação Automática**: Geração automática da documentação com **Swagger**.

---

## 📁 Estrutura do Projeto
![image](https://github.com/user-attachments/assets/ffe122de-07a8-49c0-af88-09cc6bbad037)


* **app/**: O diretório principal do código da aplicação.  
  * Pode conter os endpoints, lógica de negócios, e funções principais do FastAPI.  
* **auth/**: Responsável pela autenticação e autorização de usuários.  
  * Provavelmente contém a lógica de login, geração de tokens JWT, e verificação de permissões.  
* **loader/**: Este diretório parece lidar com o carregamento e processamento de dados.  
  * Pode conter scripts ou serviços que manipulam dados para serem usados pela aplicação.  
* **tests/**: Contém os testes automatizados da aplicação.  
  * Geralmente inclui testes de unidade, testes de integração e testes funcionais para validar a integridade do código.


---

## 📊 Arquitetura do Projeto

Aqui está um diagrama simples que ilustra a arquitetura da aplicação:



---

## 🛠️ Como Executar o Projeto

 Instalação e Configuração

#### **Requisitos:**

* Python **3.8** ou superior.  
* Dependências adicionais especificadas em `requirements.txt`.

#### **Passos de Instalação:**
### **1.Clone o repositório**:  
  
    `git clone https://github.com/usuario/projeto_fastapi_embrapa.git`  
    `cd projeto_fastapi_embrapa`
     
### **2.Instale as dependências**:  
      
     `pip install -r requirements.txt`  
 
### **3.Configuração de variáveis de ambiente**:
O projeto pode requerer a configuração de variáveis de ambiente, como chaves de API, URLs de banco de dados, etc. 
Verifique ou configure um arquivo `.env` ou defina as variáveis diretamente no ambiente.


### **4. Autenticação e Segurança**

O módulo **auth/** lida com a autenticação da aplicação. Aqui estão alguns pontos que podem estar implementados:

* **Autenticação com JWT (JSON Web Tokens)**: A autenticação pode ser baseada em tokens JWT, onde o usuário faz login e recebe um token, que deve ser enviado nas requisições subsequentes.  
* **Rotas Protegidas**: Algumas rotas podem ser protegidas por decoradores de segurança, exigindo que o usuário esteja autenticado para acessá-las.  
* **Estrutura Geral**:  
  * Login: Uma rota POST para `/auth/login` que retorna um token JWT.   
  * Verificação de Token:
    Rotas protegidas devem verificar o token antes de permitir o acesso.  
  

### **5.Loader (Carregamento de Dados)**

Este módulo é responsável por processar e carregar dados. Ele inclui:

* Scripts para **importar dados de arquivos**.  
* Funções de pré-processamento de dados antes de serem enviados para a API ou banco de dados.

---

### **6.Execução da Aplicação**

  #### **Executar o servidor localmente:**

  * **Inicie o servidor FastAPI**:   
    `uvicorn app.main:app --reload`
    
1. Isso iniciará o servidor em modo de desenvolvimento, com recarga automática ao salvar arquivos.
   
3. **Acesse a aplicação**: Abra seu navegador e vá para: http://127.0.0.1:8000.

  #### 📖 **Documentação automática:**

FastAPI gera automaticamente a documentação interativa da AP que e está disponível em:
http://localhost:8000/docs.


  ---
