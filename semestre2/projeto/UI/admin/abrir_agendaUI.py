import streamlit as st
from view import View

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda do Dia")
        data = "05/11/2024"
        inicio = "08:00"
        fim = "12:00"
        intervalo = 60
        View.horario_abrir_agenda(data, inicio, fim, intervalo)