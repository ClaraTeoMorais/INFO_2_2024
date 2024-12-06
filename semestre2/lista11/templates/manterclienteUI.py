import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:    
            #for obj in clientes: st.write(obj)
            dic = []
            for obj in clientes: 
                perfil = View.perfil_listar_id(obj.id_perfil)
                if perfil != None: 
                    perfil = perfil.nome
                dic.append({"id" : obj.id, "nome" : obj.nome, "email" : obj.email, "fone" : obj.fone, "senha" : obj.senha, "perfil" : perfil})
                dic.append(obj.__dict__)

            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        perfis = View.perfil_listar()

        nome = st.text_input("Informe o nome do cliente")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        perfil = st.selectbox("Selecione o perfil", perfis, index = None)
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            id_perfil = None
            if perfil != None: 
                id_perfil = perfil.id
            View.cliente_inserir(nome, email, fone, senha, id_perfil)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = View.cliente_listar()
        perfis = View.perfil_listar()

        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", clientes)
            nome = st.text_input("Informe o novo nome do cliente", op.nome)
            email = st.text_input("Informe o novo e-mail", op.email)
            fone = st.text_input("Informe o novo fone", op.fone)
            id_perfil = None if op.id_perfil in [0, None] else op.id_perfil
            perfil = st.selectbox("Informe o novo perfil", perfis, next((i for i, c in enumerate(perfis) if c.id == id_perfil), None))
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            if st.button("Atualizar"):
                id_perfil = None
                if perfil != None: 
                    id_perfil = perfil.id
                View.cliente_atualizar(op.id, nome, email, fone, senha, id_perfil)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de perfil", clientes)
            if st.button("Excluir"):
                View.cliente_excluir(op.id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
