import streamlit as st
from views import View
import time

class ClienteAgendarUI:
    def main():
        st.header("Agendar um Horário")
        ClienteAgendarUI.agendar()

    def agendar():
        horarios = View.horario_listar_disponiveis()
        horario = st.selectbox("Selecione o horário para agendar", horarios, index = None)
        servicos = View.servico_listar()
        servico = st.selectbox("Informe o serviço", servicos, index = None)

        if st.button("Inserir"):
            id_cliente = st.session_state["cliente_id"]
            id_servico = None
            confirmado = None

            if servico != None: 
                id_servico = servico.id

            View.horario_atualizar(horario, confirmado, id_cliente, id_servico)
            st.success("Horário inserido com sucesso")
            time.sleep(2)
            st.rerun()




        # clientes = View.cliente_listar()
        # servicos = View.servico_listar()
        # data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        # confirmado = st.checkbox("Confirmado")
        # cliente = st.selectbox("Informe o cliente", clientes, index = None)
        # servico = st.selectbox("Informe o serviço", servicos, index = None)
        # if st.button("Inserir"):
        #     id_cliente = None
        #     id_servico = None
        #     if cliente != None: id_cliente = cliente.id
        #     if servico != None: id_servico = servico.id
        #     View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
        #     st.success("Horário inserido com sucesso")
        #     time.sleep(2)
        #     st.rerun()