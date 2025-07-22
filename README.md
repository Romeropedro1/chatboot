# 🤖 ChatBot com IA (OpenAI + Streamlit)

Este projeto é uma aplicação web simples de chatbot criada com [Streamlit](https://streamlit.io/) e a API da [OpenAI](https://platform.openai.com/). O usuário pode conversar com a IA através de uma interface amigável.

## 🚀 Funcionalidades

- Interface interativa com chat estilo mensageiro.
- Memória de conversas durante a sessão.
- Conecta-se à API da OpenAI (modelo GPT-4o).
- Carregamento de chave de API via `.env`.

## 🧰 Tecnologias utilizadas

- Python
- Streamlit
- OpenAI SDK
- dotenv

## 📁 Estrutura do Projeto


## 🔧 Como rodar localmente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Romeropedro1/chatboot.git
   cd "python Dev Criação de Site e Sistemas"

2. Crie um ambiente virtual (opcional, mas recomendado):

   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. Instale as dependências:

   pip install streamlit python-dotenv openai

4. Crie um arquivo .env com sua chave da OpenAI:

   OPENAI_API_KEY=sua_chave_aqui

5. Execute a aplicação:

   streamlit run main.py







