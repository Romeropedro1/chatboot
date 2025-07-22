from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from openai import OpenAI

# Inicializa o cliente da OpenAI com sua chave
openai.api_key = os.getenv("OPENAI_API_KEY")
# Título do app
st.write("### ChatBot com IA")

# Inicializa a memória da conversa se ainda não existir
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibe o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# Campo de entrada do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # Mostra a mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    
    # Adiciona à lista de mensagens
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    # Gera resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    # Extrai a resposta da IA
    resposta_ia = resposta_modelo.choices[0].message.content

    # Mostra a resposta da IA na interface
    st.chat_message("assistant").write(resposta_ia)

    # Adiciona a resposta da IA ao histórico
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})
