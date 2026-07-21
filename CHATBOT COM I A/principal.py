import os
import streamlit as st
from openai import OpenAI


modelo_ia ="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"

st.write ("# Chatbot com IA")

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
        model="gpt-4o"
    )
    texto_resposta_ia =  resposta_ia.choices[0].message.content
   
    st.chat_message ("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role" : "assistant" , "content" : texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    
