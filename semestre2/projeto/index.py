from UI.admin.manter_clienteUI import ManterClienteUI
from UI.admin.manter_horarioUI import ManterHorarioUI
from UI.admin.manter_servicoUI import ManterServicoUI
from UI.admin.abrir_agendaUI import AbrirAgendaUI
from UI.abrir_contaUI import AbrirContaUI
from UI.loginUI import LoginUI
from view import View

import streamlit as st

class IndexUI:

    def main():
        View.criar_admin()
        if "cliente_id" in st.session_state:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            if st.session_state["cliente_nome"] == "admin":
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
        else:
            IndexUI.menu_visitante()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Abrir Conta", "Entrar no Sistema"])
        if op == "Abrir Conta": 
            AbrirContaUI.main()
        if op == "Entrar no Sistema": 
            LoginUI.main()
    
    def menu_cliente():
        pass

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia", "Abrir Conta", "Entrar no Sistema"])
        if op == "Cadastro de Clientes": 
            ManterClienteUI.main()
        if op == "Cadastro de Horários": 
            ManterHorarioUI.main()
        if op == "Cadastro de Serviços": 
            ManterServicoUI.main()
        if op == "Abrir Agenda do Dia": 
            AbrirAgendaUI.main()
        IndexUI.sair_do_sistema()

    def sair_do_sistema():
        pass


        
IndexUI.main()