from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        a = View.cliente_listar()
        for x in a:
            x = email
            if x == a.self.__email:
                raise ValueError("Email já cadastrado")
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        a = View.cliente_listar()
        for x in a:
            x = email
            if x == a.self.__email:
                raise ValueError("Email já cadastrado")
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        a = View.horario_listar()
        for x in a:
            x = id
            if x == a.self.__id_cliente:
                raise ValueError("Este cliente já possui um horário agendado. Não pode ser excluído")
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)    

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        h = View.horario_listar()
        for x in h and y in h:
            x = id_cliente
            y = id_servico
            if x != h.self.__id_cliente:
                raise ValueError("Este horário não possui um cliente válido")
            elif y != h.self.__id_servico:
                raise ValueError("Este horário não possui um serviço válido")
        c = Horario(0, data)
        c.self.__confirmado = confirmado
        c.self.__id_cliente = id_cliente
        c.self.__id_servico = id_servico
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.get_data() >= datetime.now() and h.get_id_cliente() == None: 
                disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.self.__confirmado = confirmado
        c.self.__id_cliente = id_cliente
        c.self.__id_servico = id_servico
        h = View.horario_listar()
        for x in h and y in h:
            x = id_cliente
            y = id_servico
            if x != h.self.__id_cliente:
                raise ValueError("Este horário não possui um cliente válido")
            elif y != h.self.__id_servico:
                raise ValueError("Este horário não possui um serviço válido")
        Horarios.atualizar(c)

    def horario_excluir(id):
        h = View.horario_listar()
        for x in h:
            x = id
            if x == h.self.__id_cliente:
                raise ValueError("Este horário não possui um cliente agendado. Não pode ser excluído")
        c = Horario(id, None)
        Horarios.excluir(c)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        i = data + " " + hora_inicio   # "05/11/2024 08:00"
        f = data + " " + hora_fim      # "05/11/2024 12:00"
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di

        dt = datetime.strptime(data, "%d/%m/%Y")
        hi = datetime(8, 0)
        hf = datetime(19, 0)
        if dt.date() < datetime.now().date():
            raise ValueError("A data não pode estar no passado")
        if intervalo > 120:
            raise ValueError("Intervalo máximo é de 2 horas (120 min)")
        if hora_inicio < hi and hora_inicio > hf:
            raise ValueError("O horário só pode iniciar após às 8h")
        if hora_fim > hf and hora_fim < hi:
            raise ValueError("O horário deve encerrar até às 19h")
        
        while x <= df:
            #cadastrar o horário x
            View.horario_inserir(x, False, None, None)
            #passar para o próximo horário
            x = x + d

    def servico_inserir(descricao, valor, duracao):
        if valor < 0: 
            raise ValueError("Valor inválido")
        if duracao < 0: 
            raise ValueError("Duração inválida")
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        s = View.horario_listar()
        for x in s:
            x = id
            if x == s.self.__id_servico:
                raise ValueError("Este servico já possui um horario na agenda. Não pode ser excluído")
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)    
 