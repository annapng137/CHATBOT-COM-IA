
import streamlit as st
from openai import OpenAI


modelo_ia = OpenAI ()

st.set_page_config(
    page_title="Chatbot IA",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Chatbot com Inteligência Artificial")

if  not "lista_mensagens" in st.session_state:
    st.session_state ["lista_mensagens"] = [] 



for mensagem in st.session_state["lista_mensagens"]: 
    role = mensagem["role"]
    content = mensagem["content"] 
    st.chat_message (role).write(content)

texto_usuario = st.chat_input("Digite sua mensagem aqui...")

if texto_usuario: 
   
    st.chat_message ("user").write( texto_usuario )
    mensagem= {"role" : "user" , "content" : texto_usuario}
    st.session_state ["lista_mensagens"].append(mensagem)
    

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o-mini"
    )
    texto_resposta_ia =  resposta_ia.choices[0].message.content
   
    st.chat_message ("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role" : "assistant" , "content" : texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    
