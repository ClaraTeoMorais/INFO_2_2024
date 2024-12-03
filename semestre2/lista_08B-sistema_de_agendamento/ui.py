from view import View
import streamlit as st
import pandas as pd

class index_UI:
    @staticmethod
    def main():
        manter_cliente_UI.main()
        

class manter_cliente_UI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        l, i, a, e = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with l:
            manter_cliente_UI.listar()

        with i:
            manter_cliente_UI.inserir()

        with a:
            manter_cliente_UI.atualizar()

        with e:
            manter_cliente_UI.excluir()
    
    @staticmethod
    def listar():
        obj = View.cliente_listar()
        objetos_df = pd.DataFrame(obj)
        print(objetos_df) 

    @staticmethod
    def inserir():
        n = st.text_input("Informe o nome")
        e = st.text_input("Informe o email")
        p = st.text_input("Informe o telefone")
        if st.button ("Inserir"):
            View.cliente_inserir(n, e, p)
    
    @staticmethod
    def atualizar():
        novo_cliente = st.selectbox(
            "Atualização de Clientes",
            (View.cliente_listar())
        ) 
        n = st.text_input("Informe o novo nome")
        e = st.text_input("Informe o novo email")
        p = st.text_input("Informe o novo telefone")
        if st.button ("Atualizar"):
            View.cliente_atualizar(novo_cliente, n, e, p)
    
    @staticmethod
    def excluir():
        excluir = st.selectbox(
            "Exclusão de Clientes",
            (View.cliente_listar())
        )
        if st.button ("Excluir"):
            View.cliente_excluir(excluir)


index_UI.main()