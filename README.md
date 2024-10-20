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

```
fastApiProject/
│
├── api/                  # Módulo principal da API
│   ├── __init__.py      
│   └── main.py          # Ponto de entrada da aplicação FastAPI; configura rotas e inicializa o servidor
│
├── auth/                 # Módulo de autenticação
│   ├── __init__.py      
│   └── auth.py          # Implementa as funcionalidades de autenticação (login, registro, etc.)
│
├── loader/               # Módulo para carregar dados
│   ├── __init__.py      
│   └── loader.py        # Contém funções para carregar e manipular dados 
│
├── requirements.txt      # Lista de dependências do projeto (bibliotecas necessárias)
├── venv/                 # Ambiente virtual para isolar as dependências do projeto
├── README.md             # Documentação do projeto 
└── vercel.json           # Configuração específica para deployment na Vercel

```

* **app/**: O diretório principal do código da aplicação.  
  * Pode conter os endpoints, lógica de negócios, e funções principais do FastAPI.  
* **auth/**: Responsável pela autenticação e autorização de usuários.  
  * Provavelmente contém a lógica de login, geração de tokens JWT, e verificação de permissões.  
* **loader/**: Este diretório parece lidar com o carregamento e processamento de dados.  
  * Pode conter scripts ou serviços que manipulam dados para serem usados pela aplicação.  



---

## 📊 Arquitetura do Projeto

Aqui está um diagrama simples que ilustra a arquitetura da aplicação:


![image](https://github.com/user-attachments/assets/eaf9602a-19cc-4857-a32b-c362aa47468c)




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

---
     
### **2.Instale as dependências**:  
      
     `pip install -r requirements.txt`  

---
 
### **3.Configuração de variáveis de ambiente**:
O projeto pode requerer a configuração de variáveis de ambiente, como chaves de API, URLs de banco de dados, etc. 
Verifique ou configure um arquivo `.env` ou defina as variáveis diretamente no ambiente.

---

### **4. Autenticação e Segurança**

O módulo **auth/** lida com a autenticação da aplicação. Aqui estão alguns pontos que podem estar implementados:

* **Autenticação com JWT (JSON Web Tokens)**: A autenticação pode ser baseada em tokens JWT, onde o usuário faz login e recebe um token, que deve ser enviado nas requisições subsequentes.  
* **Rotas Protegidas**: Algumas rotas podem ser protegidas por decoradores de segurança, exigindo que o usuário esteja autenticado para acessá-las.  
* **Estrutura Geral**:  
  * Login: Uma rota POST para `/auth/login` que retorna um token JWT.   
  * Verificação de Token:
    Rotas protegidas devem verificar o token antes de permitir o acesso.  
  
---

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
http://127.0.0.1:8000/docs.

 ---
## **Deploy na Vercel**

A aplicação foi implantada na Vercel, facilitando o acesso remoto e garantindo alta performance. A Vercel é conhecida pela facilidade de integração com projetos FastAPI e por otimizar o processo de deploy. Para acessar a versão de produção da aplicação, utilize a URL fornecida no painel de controle da Vercel após o deploy.

### **Passos para o Deploy na Vercel:**

**1. Configuração inicial**:  
   * Certifique-se de que o projeto está configurado corretamente no GitHub ou em outro repositório Git.  
   * No painel da Vercel, conecte seu repositório e configure as variáveis de ambiente necessárias (como chaves de API e strings de conexão com bancos de dados).  

 **2.Configurar o projeto para Vercel**:

Crie um arquivo `vercel.json` na raiz do projeto se necessário. Ele deve incluir as seguintes configurações básicas:  
```
`{`  
  `"builds": [`  
    `{ "src": "app/main.py", "use": "@vercel/python" }`  
  `],`  
  `"routes": [`  
    `{ "src": "/(.*)", "dest": "app/main.py" }`  
  `]`  
`}`
```
  
**3. Deploy**:  
   * Acesse o painel da Vercel, clique em "Deploy" para realizar o deploy da sua aplicação.  
   * A Vercel fará o build automaticamente e, em alguns minutos, sua aplicação estará disponível online.
     

# **Especificações da API**

Cria uma instância da API com um título, descrição e versão.
```
`app = FastAPI(`  
   `title="Embrapa CSV API",`  
   `description="API para consulta de dados CSV da Embrapa",`  
   `version="1.0.0"`  
`)`
```
Cria uma instância da API com um título, descrição e versão.

### **URLs dos CSVs**

Um dicionário chamado `CSV_URLS` é definido para armazenar as URLs dos arquivos CSV disponíveis:

* `producao`: Produção de vinhos.  
* `processa`: Processamento de vinhos viníferas.  
* `comercio`: Dados de comércio de vinhos.  
* `importacao`: Dados de importação de vinhos.  
* `exportacao`: Dados de exportação de vinhos.

### **Endpoints**

#### **1\. Endpoint Raiz**

```
`@app.get("/", tags=["Root"])`  
`def read_root():`  
   `return {"message": "API para consulta de dados CSV da Embrapa"}`
```
* **Método**: `GET`  
* **Descrição**: Retorna uma mensagem de boas-vindas à API.

**Resposta**:  
```
`{`  
  `"message": "API para consulta de dados CSV da Embrapa"`  
`}`

```

#### **2\. Endpoint de Geração de Token**

```
`@app.post("/token", tags=["Authentication"])`  
`def generate_token():`  
    `"""`  
    `Endpoint para gerar o token JWT.`  
    `"""`  
    `...`
```

* **Método**: `POST`  
* **Descrição**: Gera um token JWT para autenticação.

**Resposta**:  
```
`{`  
  `"token": "<JWT_TOKEN>"`  
`}`
```


#### **3\. Endpoint para Obter Dados CSV**
``` 
`@app.get("/{file_id}", tags=["CSV Data"])`  
`def get_csv_by_id(file_id: str, token: dict = Depends(verify_token)):`  
    `"""`  
    `Retorna os dados de um CSV específico identificado por file_id.`  
    `"""`  
    `...`
```

* **Método**: `GET`  
* **Parâmetros**:  
  * `file_id`: Identificador do arquivo CSV a ser acessado.  
  * `token`: Token JWT para autenticação, verificado através da função `verify_token`.  
* **Descrição**: Retorna os dados de um CSV específico. Se o `file_id` não existir ou os dados estiverem vazios, são retornados os seguintes códigos de erro:  
  * **404**: CSV não encontrado.  
  * **400**: Dados do CSV estão vazios ou ocorreu um erro na leitura.

**Resposta** (exemplo):  
```
`[`  
  `{`  
    `"coluna1": "valor1",`  
    `"coluna2": "valor2",`  
    `...`  
  `},`  
  `...`
 `]`
```
