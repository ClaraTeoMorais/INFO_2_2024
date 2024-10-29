from view import View
import streamlit as st
import pandas as pd
import time
from datetime import datetime

class index_UI:
    @staticmethod
    def main():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Abrir Agenda do Dia"])
        if op == "Cadastro de Clientes": 
            manter_cliente_UI.main()
        if op == "Cadastro de Horários": 
            manter_horario_UI.main()
        if op == "Cadastro de Serviços": 
            manter_servico_UI.main()
        if op == "Abrir Agenda do Dia": 
            abrir_agenda_UI.main()
        

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
        if len(obj) == 0:
            st.write("Nnenhum cliente cadastrado")
        else:
            dic = []
            for i in obj:
                dic.append(i.__dict__)
            objetos_df = pd.DataFrame(dic)
            st.dataframe(objetos_df) 

    @staticmethod
    def inserir():
        n = st.text_input("Informe o nome")
        e = st.text_input("Informe o email")
        p = st.text_input("Informe o telefone")
        if st.button ("Inserir"):
            View.cliente_inserir(n, e, p)
            st.success("Cliente inserido com sucesso!")
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def atualizar():
        obj = View.cliente_listar()
        if len(obj) == 0:
            st.write("Nnenhum cliente cadastrado")
        else:
            novo_cliente = st.selectbox("Atualização de Clientes", obj) 
            n = st.text_input("Informe o novo nome", obj.n)
            e = st.text_input("Informe o novo email", obj.e)
            p = st.text_input("Informe o novo telefone", obj.p)
            if st.button ("Atualizar"):
                View.cliente_atualizar(novo_cliente.id, n, e, p)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    
    @staticmethod
    def excluir():
        obj = View.cliente_listar()
        if len(obj) == 0:
            st.write("Nnenhum cliente cadastrado")
        else:
            excluir = st.selectbox("Exclusão de Clientes",obj) 
            if st.button ("Excluir"):
                View.cliente_excluir(excluir)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()


class manter_servico_UI:
    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        l, i, a, e = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with l:
            manter_servico_UI.listar()

        with i:
            manter_servico_UI.inserir()

        with a:
            manter_servico_UI.atualizar()

        with e:
            manter_servico_UI.excluir()
    
    @staticmethod
    def listar():
        obj = View.servico_listar()
        if len(obj) == 0:
            st.write("Nnenhum serviço cadastrado")
        else:
            dic = []
            for i in obj:
                dic.append(i.__dict__)
            objetos_df = pd.DataFrame(dic)
            st.dataframe(objetos_df) 

    @staticmethod
    def inserir():
        d = st.text_input("Informe a descrição")
        v = st.text_input("Informe o valor")
        t = st.text_input("Informe a duração")
        if st.button ("Inserir"):
            View.servico_inserir(d, v, t)
            st.success("Serviço inserido com sucesso!")
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def atualizar():
        obj = View.servico_listar()
        if len(obj) == 0:
            st.write("Nnenhum serviço cadastrado")
        else:
            novo_servico = st.selectbox("Atualização de Serviços", obj) 
            d = st.text_input("Informe a nova descrição", obj.d)
            v = st.text_input("Informe o novo valor", obj.v)
            t = st.text_input("Informe a nova duração", obj.t)
            if st.button ("Atualizar"):
                View.servico_atualizar(novo_servico.id, d, v, t)
                st.success("Serviço atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    
    @staticmethod
    def excluir():
        obj = View.servico_listar()
        if len(obj) == 0:
            st.write("Nnenhum serviço cadastrado")
        else:
            excluir = st.selectbox("Exclusão de Serviços",obj) 
            if st.button ("Excluir"):
                View.servico_excluir(excluir)
                st.success("Serviço atualizado com sucesso!")
                time.sleep(2)
                st.rerun()


class manter_horario_UI:
    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        l, i, a, e = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with l:
            manter_horario_UI.listar()

        with i:
            manter_horario_UI.inserir()

        with a:
            manter_horario_UI.atualizar()

        with e:
            manter_horario_UI.excluir()
    
    @staticmethod
    def listar():
        obj = View.horario_listar()
        if len(obj) == 0:
            st.write("Nnenhum horario cadastrado")
        else:
            dic = []
            for i in obj:
                dic.append(i.__dict__)
            objetos_df = pd.DataFrame(dic)
            st.dataframe(objetos_df) 

    @staticmethod
    def inserir():
        d = st.text_input("Informe o horário (dd/mm/aa hh:mm)")
        clientes = View.cliente_listar()
        c = st.selectbox("Selecione o cliente", clientes)
        servicos = View.servico_listar()
        s = st.selectbox("Selecione o serviço", servicos)
        if st.button ("Inserir"):
            data = datetime.datetime.strptime(d, "%d/%m/%Y %H:%M")
            View.agenda_inserir(data, True, c.id, s.id)
            st.success("Horário inserido com sucesso!")
            time.sleep(2)
            st.rerun()
    
    @staticmethod
    def atualizar():
        obj = View.horario_listar()
        cliente = View.cliente_listar()
        servico = View.servico_listar()
        if len(obj) == 0:
            st.write("Nnenhum horário disponível")
        else:
            novo_horario = st.selectbox("Atualização de Horário", obj) 
            d = st.text_input("Informe o novo horário (dd/mm/aa hh:mm)", obj.d)
            c = st.selectbox("Selecione o novo cliente", cliente)
            s = st.selectbox("Selecione o novo serviço", servico)
            if st.button ("Atualizar"):
                View.horario_atualizar(novo_horario.id, d, c, s)
                st.success("Horário atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    
    @staticmethod
    def excluir():
        obj = View.horario_listar()
        if len(obj) == 0:
            st.write("Nnenhum horário disponível")
        else:
            excluir = st.selectbox("Exclusão de Horários",obj) 
            if st.button ("Excluir"):
                View.horario_excluir(excluir)
                st.success("Horário atualizado com sucesso!")
                time.sleep(2)
                st.rerun()


class abrir_agenda_UI():
    def main():
        st.header("Abrir Agenda do Dia")
        abrir_agenda_UI.abrir_agenda()
    
    def abrir_agenda():
        d = st.text_input("Informe a data (dd/mm/aaaa)")
        h_inicio = st.text_input("Informe o horário inicial (hh:mm)")
        h_fim = st.text_input("Informe o horário final (hh:mm)")
        i = st.text_input("Informe o interlavo entre os horários (min)")
        if st.button("Inserir horários"):
            View.abrir_agenda(d, h_inicio, h_fim, int(i))
            st.success("Horário(s) inserido(s) com sucesso!")
            time.sleep(2)
            st.rerun()


index_UI.main()