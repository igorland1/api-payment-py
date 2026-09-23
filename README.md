# API Payment Pix

> API simples em Flask para criar e gerenciar pagamentos via Pix, com atualizações em tempo real utilizando WebSockets (Flask-SocketIO).

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Flask--SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-3.1.1-D71F00?style=flat)](https://flask-sqlalchemy.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

---

## 📋 Sobre o projeto

**API Payment Pix** é uma API para gerar cobranças e confirmar pagamentos simulados via Pix. Utilizando o framework Flask, este projeto permite a criação de pagamentos com QR Code (através das bibliotecas `qrcode` e `Pillow`), persistência de dados em um banco de dados SQLite, e a notificação instantânea do status do pagamento ao front-end via WebSockets, utilizando o `Flask-SocketIO`.

### Principais características

- ✅ **Criação de Pagamento Pix** — Gera uma nova cobrança com expiração e cria um QR Code correspondente
- ✅ **Confirmação de Pagamento** — Endpoint (Webhook) para confirmar o pagamento via ID bancário
- ✅ **Atualização em Tempo Real** — Dispara um evento WebSocket para a página do usuário quando o pagamento é concluído
- ✅ **Visualização de Pagamento** — Interface web para apresentar o QR Code e indicar se a cobrança foi paga
- ✅ **Isolamento por Banco Relacional** — Salva as informações e controle de estado no banco de dados SQLite

---

## 🏗️ Arquitetura

### Stack utilizada

- **Linguagem**: Python 3
- **Framework Web**: Flask 2.3.0
- **ORM**: Flask-SQLAlchemy 3.1.1
- **WebSockets**: Flask-SocketIO 5.3.6
- **Geração de Imagens**: qrcode 7.4.2 e Pillow 10.2.0
- **Banco de dados**: SQLite

### Estrutura do projeto

```
api-payment-py/
├── db_models/
│   └── payment.py         # Modelo Payment (SQLAlchemy)
├── repository/
│   └── database.py        # Instância do SQLAlchemy (db)
├── payments/
│   └── pix.py             # Lógica simulada de integração Pix
├── static/
│   └── img/               # Armazena os QR Codes em PNG
├── templates/
│   ├── payment.html           # Tela principal de cobrança (com QR Code)
│   ├── confirmed_payment.html # Tela de sucesso após pagamento
│   └── 404.html               # Página de não encontrado
├── app.py                 # Rotas principais, SocketIO e entrypoint do Flask
├── requirements.txt       # Dependências do projeto
└── .gitignore
```

### Modelo de dados

**Payment** (`db_models/payment.py`)

| Campo               | Tipo      | Descrição                                         |
|---------------------|-----------|---------------------------------------------------|
| `id`                | int       | Identificador único do pagamento                  |
| `value`             | float     | Valor da cobrança                                 |
| `paid`              | boolean   | Status de pagamento (True/False)                  |
| `bank_payment_id`   | string    | ID único de referência gerado para o banco        |
| `qr_code`           | string    | Caminho ou nome do arquivo do QR Code             |
| `expiration_date`   | datetime  | Data/hora limite de expiração da cobrança         |

---

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd api-payment-py
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie a aplicação**:
   ```bash
   python app.py
   ```

5. O servidor ficará disponível em `http://127.0.0.1:5000`.

---

## 🛣️ Endpoints da API

- `POST /payments/pix`: Cria um novo pagamento (requer JSON com `value`).
- `GET /payments/pix/qr_code/<file_name>`: Retorna a imagem PNG gerada com o QR Code.
- `POST /payments/pix/confirmation`: Endpoint para recebimento do webhook e confirmação (requer `bank_payment_id` e `value`).
- `GET /payments/pix/<int:payment_id>`: Renderiza o HTML da cobrança ou de pagamento confirmado.
