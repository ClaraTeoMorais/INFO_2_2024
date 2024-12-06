import streamlit as st
import pandas as pd
from views import View
import time

class AlterarDados:
    def main():
        clientes = View.cliente_listar()
        perfis = View.perfil_listar()

        admin = st.session_state["cliente_nome"] == "admin"
        # mensagen de bem-vindo
        st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])

        op = st.session_state["cliente_id"]
        if st.session_state["cliente_nome"] == "admin":
            nome = "admin"
            email = "admin"
            fone = "1234"
            id_perfil = "admin"
            senha = st.text_input("Informe a nova senha", st.session_state["cliente_senha"], type="password")
            if st.button("Atualizar"):
                View.cliente_atualizar(op, nome, email, fone, senha, id_perfil)
                st.success("Dados atualizados com sucesso")
                time.sleep(2)
                st.rerun()
        
        else: 
            nome = st.text_input("Informe o novo nome", st.session_state["cliente_nome"])
            email = st.text_input("Informe o novo e-mail", st.session_state["cliente_email"])
            fone = st.text_input("Informe o novo fone", st.session_state["cliente_fone"])
            id_perfil = None if op.id_perfil in [0, None] else op.id_perfil
            perfil = st.selectbox("Informe o novo perfil", perfis, next((i for i, c in enumerate(perfis) if c.id == id_perfil), None))
            senha = st.text_input("Informe a nova senha", st.session_state["cliente_senha"], type="password")
            if st.button("Atualizar"):
                id_perfil = None
                if perfil != None: 
                    id_perfil = perfil.id
                View.cliente_atualizar(op.id, nome, email, fone, senha, id_perfil)
                st.success("Dados atualizados com sucesso")
                time.sleep(2)
                st.rerun()