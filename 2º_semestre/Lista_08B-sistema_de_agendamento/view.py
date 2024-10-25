from cliente import Cliente, Clientes

class View:
    def cliente_listar():
        return Clientes.listar()
    
    def cliente_inserir(nome, email, phone):
        c = Cliente(0, nome, email, phone)
        Clientes.inserir(c)

    def cliente_atualizar(id, nome, email, phone):
        c = Cliente(0, nome, email, phone)
        Clientes.atualizar

    def cliente_excluir(id):
        c = Cliente(id,"", "", "")
        Clientes.excluir(c)