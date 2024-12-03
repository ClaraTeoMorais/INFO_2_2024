from cliente import Cliente, Clientes
from servico import Servico, Servicos
from horario import Horario, Horarios
from datetime import datetime

class View:
    #CLIENTE:
    def cliente_listar():
        return Clientes.listar()
    
    def cliente_inserir(nome, email, phone):
        c = Cliente(0, nome, email, phone)
        Clientes.inserir(c)

    def cliente_atualizar(id, nome, email, phone):
        c = Cliente(0, nome, email, phone)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        c = Cliente(id,"", "", "")
        Clientes.excluir(c)

    #SERVIÇO
    def servico_listar():
        return Servicos.listar()
    
    def servico_inserir(descricao, valor, duracao):
        s = Servico(0, descricao, valor, duracao)
        Servicos.inserir(s)

    def servico_atualizar(id, descricao, valor, duracao):
        s = Servico(0, descricao, valor, duracao)
        Servicos.atualizar(s)

    def servico_excluir(id):
        s = Servico(id,"", "", "")
        Servicos.excluir(s)
    
    #HORÁRIO
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        h = Horario(0, data, confirmado, id_cliente, id_servico)
        Horarios.inserir(h)

    def horario_listar():
        return Horarios.listar()
    
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        h = Servico(0, data, confirmado, id_cliente, id_servico)
        Servicos.atualizar(h)
    
    def horario_excluir(id):
        h = Servico(id,"", "", "", "")
        Servicos.excluir(h)


    def abrir_agenda(data, h_inicio, h_fim, intervalo):
        inicio = datetime.datetime.strptime(f"{data} {h_inicio}", "%d/%m/%Y %H:%M")
        fim = datetime.datetime.strptime(f"{data} {h_fim}", "%d/%m/%Y %H:%M")
        int = datetime.timedelta(minutes = intervalo) 
        obj = inicio
        while obj <= fim:
            h = Horario(0, obj, False, 0, 0)
            Horarios.inserir(h)
            obj += int