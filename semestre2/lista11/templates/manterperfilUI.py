import streamlit as st
import pandas as pd
from views import View
import time

class ManterPerfilUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: 
            ManterPerfilUI.listar()
        with tab2: 
            ManterPerfilUI.inserir()
        with tab3: 
            ManterPerfilUI.atualizar()
        with tab4: 
            ManterPerfilUI.excluir()

    def listar():
        perfis = View.perfil_listar()
        if len(perfis) == 0: 
            st.write("Nenhum perfil cadastrado")
        else:    
            dic = []
            for obj in perfis: 
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do perfil")
        descricao = st.text_input("Informe a descrição")
        beneficios = st.text_input("Informe os benefícios")
        if st.button("Inserir"):
            View.perfil_inserir(nome, descricao, beneficios)
            st.success("Perfil inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        perfis = View.perfil_listar()
        if len(perfis) == 0: 
            st.write("Nenhum perfil cadastrado")
        else:
            op = st.selectbox("Atualização de perfil", perfis)
            nome = st.text_input("Informe o novo nome do perfil", op.nome)
            descricao = st.text_input("Informe a nova descrição", op.descricao)
            beneficios = st.text_input("Informe os novos benefícios", str(op.beneficios))
            if st.button("Atualizar"):
                View.perfil_atualizar_atualizar(op.id, nome, descricao, beneficios)
                st.success("Perfil atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        perfis = View.perfil_listar()
        if len(perfis) == 0: 
            st.write("Nenhum pefil cadastrado")
        else:
            op = st.selectbox("Exclusão de pefil", perfis)
            if st.button("Excluir"):
                View.servico_excluir(op.id)
                st.success("Perfil excluído com sucesso")
                time.sleep(2)
                st.rerun()
