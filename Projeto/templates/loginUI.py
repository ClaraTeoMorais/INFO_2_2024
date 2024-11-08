import streamlit as st
from views import View
import time

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        senha2 = st.text_input("Digite novamente a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha, senha2)
            if c == None: 
                st.write("E-mail ou senha inválidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.rerun()
            if senha != senha2:
                st.write("As senhas não podem ser diferentes")