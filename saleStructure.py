import pymongo

from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto
# from Venda import Venda


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["projeto_mongodb_python"]
col_cliente = mydb["cliente"]
col_funcionario = mydb["funcionario"]
col_produto = mydb["produto"]
# col_venda = mydb["venda"]



def mensagem_erro():
    print('\nOcorreu um problema na aplicação, tente novamente.')


def mensagem_nenhum_registro(param):
    print('\nNenhum', param, 'encontrado.')


# Metodos do Cliente

def inserir_cliente(cliente):
    result = col_cliente.insert_one(cliente.__dict__)
    if result.inserted_id:
        print(f'\nO cliente {cliente.get_nome()} foi inserido com sucesso.')


def preencher_cliente():
    cliente = Cliente()
    cliente.set_nome(input('\nInforme o nome: '))
    cliente.set_telefone(input('\nInforme o telefone: '))
    cliente.set_endereco(input('\nInforme o endereco: '))
    cliente.set_cidade(input('\nInforme a cidade: '))
    cliente.set_estado(input('\nInforme o estado: '))
    cliente.set_data_nascimento(input('\nInforme a data de nascimento: '))
    cliente.set_email(input('\nInforme o email: '))
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
            print("\nID: ", cliente["_id"], "\nNome: ", cliente["nome"], "\nTelefone: ", cliente["telefone"],
                  "\nEndereço: ", cliente["endereco"], "\nCidade: ", cliente["cidade"], "\nEstado: ", cliente["estado"],
                  "\nData Nascimento: ", cliente["data_nascimento"], "\nEmail: ", cliente["email"])
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
    funcionario.set_telefone(input('\nInforme o telefone: '))
    funcionario.set_nome_produto_venda(input('\nInforme o nome do produto venda: '))
    funcionario.set_segmento_produto(input('\nInforme o segmento do produto: '))

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
            print("\nID: ", funcionario["_id"], "\nNome: ", funcionario["nome"], "\nTelefone: ", funcionario["telefone"],
                  "\nNome produto venda: ", funcionario["nome_produto_venda"], "\nSegmento do produto: ",
                  funcionario["segmento_produto"])
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
    print("Lanchonente excluído com sucesso!")


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

    elif opcao == '0':
        continuar = False

    else:
        print('\nOpção inválida.')