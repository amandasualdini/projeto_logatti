import pymongo

from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto
from Venda import Venda
from VendaItem import VendaItem

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["projeto_mongodb_python"]
col_cliente = mydb["cliente"]
col_funcionario = mydb["funcionario"]
col_produto = mydb["produto"]
col_venda = mydb["venda"]
col_venda_item = mydb["vendaItem"]


def mensagem_erro(erro):
    print('\nOcorreu um problema na aplicação, tente novamente.', erro)


def mensagem_nenhum_registro(param):
    print('\nNenhum', param, 'encontrado.')


# Metodos do Cliente

def inserir_cliente(cliente):
    result = col_cliente.insert_one(cliente.__dict__)
    if result.inserted_id:
        print(f'\nO cliente {cliente.get_nome()} foi inserido com sucesso.')


def preencher_cliente():
    cliente = Cliente()
    cliente.set_nome(input('\nInforme o seu nome: '))
    cliente.set_cpf(input('\nInforme o seu cpf: '))
    return cliente


def excluir_cliente(id_cliente):
    col_cliente.delete_one({"_id": ObjectId(id_cliente)})
    print("Cliente excluído com sucesso!")


def atualizar_cliente(id_cliente, cliente):
    result = col_cliente.update_one({'_id': ObjectId(id_cliente)}, {"$set": cliente.__dict__})
    if result.modified_count > 0:
        print(f'\nO cliente {cliente.get_nome()} foi alterado com sucesso.')


def listar_clientes():
    if col_cliente.estimated_document_count() > 0:
        for cliente in col_cliente.find():
            print("\nID: ", cliente["_id"], "\nNome: ", cliente["nome"], "\nCpf: ", cliente["cpf"])
    else:
        print("Não existem clientes cadastrados no banco de dados")


# Metodos do Funcionário

def inserir_funcionario(funcionario):
    result = col_funcionario.insert_one(funcionario.__dict__)
    if result.inserted_id:
        print(f'\nO funcionario {funcionario.get_nome()} foi inserido com sucesso.')


def preencher_funcionario():
    funcionario = Funcionario()
    funcionario.set_nome(input('\nInforme o nome: '))
    funcionario.set_cpf(input('\nInforme o CPF do funcionario: '))
    funcionario.set_salario(input('\nInforme o salario: '))

    return funcionario


def excluir_funcionario(id_funcionario):
    col_funcionario.delete_one({"_id": ObjectId(id_funcionario)})
    print("Funcionário excluído com sucesso!")


def atualizar_funcionario(id_funcionario, funcionario):
    result = col_funcionario.update_one({'_id': ObjectId(id_funcionario)}, {"$set": funcionario.__dict__})
    if result.modified_count > 0:
        print(f'\nO funcionario {funcionario.get_nome()} foi alterado com sucesso.')


def listar_funcionario():
    if col_funcionario.estimated_document_count() > 0:
        for funcionario in col_funcionario.find():
            print("\nID: ", funcionario["_id"], "\nNome: ", funcionario["nome"], "\nCpf: ", funcionario["cpf"],
                  "\nSalario: ", funcionario["salario"])
    else:
        print("Não existem funcionarios cadastrados no banco de dados")


# Metodos dos Produto

def inserir_produto(produto):
    result = col_produto.insert_one(produto.__dict__)
    if result.inserted_id:
        print(f'\nO produto {produto.get_descricao()} foi inserido com sucesso.')


def preencher_produto():
    produto = Produto()
    produto.set_descricao(input('\nInforme a descrição: '))
    produto.set_valor(input('\nInforme o valor do produto: '))
    produto.set_qtde_produtos(input('\nInforme a quantidade de produtos: '))

    return produto


def excluir_produto(id_produto):
    col_produto.delete_one({"_id": ObjectId(id_produto)})
    print("Produto excluído com sucesso!")


def atualizar_produto(id_produto, produto):
    result = col_produto.update_one({'_id': ObjectId(id_produto)}, {"$set": produto.__dict__})
    if result.modified_count > 0:
        print(f'\nO produto {produto.get_nome()} foi alterado com sucesso.')


def listar_produto():
    if col_produto.estimated_document_count() > 0:
        for produto in col_produto.find():
            print("\nID: ", produto["_id"], "\nDescrição: ", produto["descricao"], "\nValor do Produto: ",
                  produto["valor"],
                  "\nQuantidade de Produtos: ", produto["qtde_produtos"])
    else:
        print("Não existem produtos cadastrados no banco de dados")

# Metodos da Venda

def inserir_venda(venda):
    result = col_venda.insert_one(venda.__dict__)
    if result.inserted_id:
        print(f'\nA venda do funcionario de id {venda.get_funcionario_id()} foi inserido com sucesso.')


def preencher_venda():
    venda = Venda()
    venda.set_data(input('\nInforme a data da venda: '))
    venda.set_cliente_id(input('\nInforme o id do cliente: '))
    venda.set_funcionario_id(input('\nInforme o id do funcionario: '))
    return venda


def excluir_venda(id_venda):
    col_venda.delete_one({"_id": ObjectId(id_venda)})
    print("Venda excluído com sucesso!")


def atualizar_venda(id_venda, venda):
    result = col_venda.update_one({'_id': ObjectId(id_venda)}, {"$set": venda.__dict__})
    if result.modified_count > 0:
        print(f'\nA venda {venda.get_nome()} foi alterada com sucesso.')


def listar_venda():
    if col_venda.estimated_document_count() > 0:
        for venda in col_venda.find():
            print("\nID: ", venda["_id"], "\Data: ", venda["datga"], "\nId do funcionario: ",
                  venda["funcionario_id"], "\nId do cliente: ", venda["cliente_id"])
    else:
        print("Não existem vendas cadastradas no banco de dados")

# Metodos da Venda Item

def inserir_venda_item(venda_item):
    result = col_venda_item.insert_one(venda_item.__dict__)
    if result.inserted_id:
        print(f'\nA venda item {venda_item.get_id()} foi inserida com sucesso.')


def preencher_venda_item():
    venda_item = VendaItem()
    venda_item.set_quantidade(input('\nInforme a quantidade de itens: '))
    venda_item.set_total(input('\nInforme o valor do item: '))
    venda_item.set_venda_id(input('\nInforme o id da venda: '))
    venda_item.set_produto_id(input('\nInforme o id do produto: '))
    return venda_item

def listar_venda_item():
    if col_venda_item.estimated_document_count() > 0:
        for venda_item in col_venda_item.find():
            print("\nID: ", venda_item["_id"], "\nQuantidade: ", venda_item["quantidade"], "\nTotal: ",
                  venda_item["total"], "\nId da venda: ", venda_item["venda_id"],
                  "\nId do produto: ", venda_item["produto_id"],)
    else:
        print("Não existem vendas itens cadastradas no banco de dados")

continuar = True

while continuar:
    print('\n---------- Menu Cliente ---------- ')
    print('\n1 - Inserir cliente')
    print('\n2 - Listar clientes')
    print('\n3 - Excluir cliente')
    print('\n4 - Alterar cliente')
    print('\n---------- Menu Funcionário ---------- ')
    print('\n5 - Inserir funcionario')
    print('\n6 - Listar funcionario')
    print('\n7 - Excluir funcionario')
    print('\n8 - Alterar funcionario')
    print('\n---------- Menu Produto ---------- ')
    print('\n9 - Inserir produto')
    print('\n10 - Listar produto')
    print('\n11 - Excluir produto')
    print('\n12 - Alterar produto')
    print('\n0 - Sair do sistema')
    print('\n---------- Menu Venda ---------- ')
    print('\n13 - Inserir venda')
    print('\n14 - Listar venda')
    print('\n15 - Excluir venda')
    print('\n16 - Alterar venda')
    print('\n0 - Sair do sistema')
    print('\n---------- Menu Venda Item ---------- ')
    print('\n17 - Inserir venda item')
    print('\n18 - Listar venda item')   
    print('\n0 - Sair do sistema')

    opcao = input('\nInforme a opção desejada: ')

    if opcao == '1':
        try:
            print("\n====================Adicionar Cliente====================")
            inserir_cliente(preencher_cliente())
        except:
            mensagem_erro()

    elif opcao == '2':
        try:
            print("\n====================Lista de Clientes====================")
            listar_clientes()
        except:
            mensagem_erro()

    elif opcao == '3':
        try:
            print("\n=====================Excluir Cliente=====================")
            id_cliente = str(input("\nInforme o id do Cliente: "))
            excluir_cliente(id_cliente)
        except:
            mensagem_erro()

    elif opcao == '4':
        try:
            print("\n=====================Alterar Cliente=====================")
            id_cliente = str(input("\nInforme o id do Cliente: "))
            atualizar_cliente(id_cliente, preencher_cliente())
        except:
            mensagem_erro()

    elif opcao == '5':
        try:
            print("\n====================Inserir Funcionario====================")
            inserir_funcionario(preencher_funcionario())
        except:
            mensagem_erro()

    elif opcao == '6':
        try:
            print("\n=====================Lista de Funcionarios=====================")
            listar_funcionario()
        except:
            mensagem_erro()

    elif opcao == '7':
        try:
            print("\n=====================Excluir Funcionarior=====================")
            id_funcionario = str(input("\nInforme o id do Funcionario: "))
            excluir_funcionario(id_funcionario)
        except:
            mensagem_erro()

    elif opcao == '8':
        try:
            print("\n====================Alterar Funcionario====================")
            id_funcionario = str(input("\nInforme o id do Funcionario: "))
            atualizar_funcionario(id_funcionario, preencher_funcionario())
        except:
            mensagem_erro()

    elif opcao == '9':
        try:
            print("\n=====================Inserir Produto=====================")
            inserir_produto(preencher_produto())
        except:
            mensagem_erro()

    elif opcao == '10':
        try:
            print("\n=====================Lista de Produtos=====================")
            listar_produto()
        except:
            mensagem_erro()

    elif opcao == '11':
        try:
            print("\n=====================Excluir Produto=====================")
            id_produto = str(input("\nInforme o id do Produto: "))
            excluir_produto(id_produto)
        except:
            mensagem_erro()

    elif opcao == '12':
        try:
            print("\n=====================Alterar Produto=====================")
            id_produto = str(input("\nInforme o id do Produto: "))
            atualizar_produto(id_produto, preencher_produto())
        except:
            mensagem_erro()

    elif opcao == '13':
        try:
            print("\n=====================Inserir Venda=====================")
            inserir_venda(preencher_venda())
        except:
            mensagem_erro() 
    elif opcao == '14':
        try:
            print("\n=====================Listar Venda=====================")
            listar_venda()
        except:
            mensagem_erro()
    elif opcao == '15':
        try:
            print("\n=====================Alterar Venda=====================")
            id_venda = str(input("\nInforme o id da Venda: "))
            atualizar_venda(id_venda, preencher_venda())
        except:
            mensagem_erro()
    elif opcao == '16':
        try:
            print("\n=====================Excluir Venda=====================")
            id_venda = str(input("\nInforme o id da Venda: "))
            excluir_venda(id_venda)
        except:
            mensagem_erro()

    elif opcao == '17':
        try:
            print("\n=====================Inserir Venda Item=====================")
            inserir_venda_item(preencher_venda_item())
        except:
            mensagem_erro() 
    elif opcao == '18':
        try:
            print("\n=====================Listar Venda Item=====================")
            listar_venda_item()
        except:
            mensagem_erro()

    elif opcao == '0':
        continuar = False

    else:
        print('\nOpção inválida.')