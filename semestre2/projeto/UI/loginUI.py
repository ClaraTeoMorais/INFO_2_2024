import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("e-mail")
        senha = st.text_input("senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c == None: st.write("e-mail ou senha inválidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.rerun()