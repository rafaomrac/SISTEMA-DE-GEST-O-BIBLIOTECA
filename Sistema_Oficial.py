import getpass

# Dados iniciais
admins = {
    'petrick': '01',
    "luan": "33", 
    "andrew": "22",
    "rafael": "29", "ygor": "69",
    "camila": "13"
}

usuarios = []
bibliotecarios = []
livros = {
    'Romance': [
        {'nome': 'Orgulho e Preconceito', 'autor': 'Jane Austen', 'ano': '1813', 'local': 'Estante A1', 'tipo': 'físico'},
        {'nome': 'O Morro dos Ventos Uivantes', 'autor': 'Emily Brontë', 'ano': '1847', 'local': 'Estante A2', 'tipo': 'físico'},
        {'nome': 'Dom Casmurro', 'autor': 'Machado de Assis', 'ano': '1899', 'local': 'Estante A3', 'tipo': 'online'}
    ],
    'Fantasia': [
        {'nome': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano': '1954', 'local': 'Estante B1', 'tipo': 'físico'},
        {'nome': 'Harry Potter e a Pedra Filosofal', 'autor': 'J.K. Rowling', 'ano': '1997', 'local': 'Estante B2', 'tipo': 'físico'},
        {'nome': 'O Hobbit', 'autor': 'J.R.R. Tolkien', 'ano': '1937', 'local': 'Estante B3', 'tipo': 'online'}
    ],
    'Ficção Científica': [
        {'nome': 'Duna', 'autor': 'Frank Herbert', 'ano': '1965', 'local': 'Estante C1', 'tipo': 'físico'},
        {'nome': 'Neuromancer', 'autor': 'William Gibson', 'ano': '1984', 'local': 'Estante C2', 'tipo': 'físico'},
        {'nome': 'Fundação', 'autor': 'Isaac Asimov', 'ano': '1951', 'local': 'Estante C3', 'tipo': 'online'}
    ],
    'Ensino Médio': [
        {'nome': 'Matemática Essencial', 'autor': 'Paulo Araújo', 'ano': '2010', 'local': 'Estante D1', 'tipo': 'físico'},
        {'nome': 'Física Básica', 'autor': 'Hélio Pereira', 'ano': '2012', 'local': 'Estante D2', 'tipo': 'físico'},
        {'nome': 'Química para Todos', 'autor': 'Roberto Silva', 'ano': '2011', 'local': 'Estante D3', 'tipo': 'online'}
    ],
    'Faculdade': [
        {'nome': 'Cálculo I', 'autor': 'James Stewart', 'ano': '2008', 'local': 'Estante E1', 'tipo': 'físico'},
        {'nome': 'Introdução à Programação', 'autor': 'Paul Deitel', 'ano': '2013', 'local': 'Estante E2', 'tipo': 'físico'},
        {'nome': 'Economia Básica', 'autor': 'Gregory Mankiw', 'ano': '2005', 'local': 'Estante E3', 'tipo': 'online'}
    ]
}


# (obs)Funções de menu!

def exibir_menu_principal_admin():
    print("Menu Principal do Administrador:")
    print("1. Cadastro prévio de usuário")
    print("2. Cadastro prévio de bibliotecário")
    print("3. Remover bibliotecário")
    print("4. Saida")
    print()
def exibir_menu_principal_acesso():
    print("Menu Principal de Acesso:")
    print("1. Login de usuário")
    print("2. Login de bibliotecário")
    print("3. Listar usuários cadastrados")
    print("4. Listar bibliotecários cadastrados")
    print("5. Sair")
    print()
def exibir_menu_usuario():
    print("Menu Usuário:")
    print("1. Pesquisar livro")
    print("2. Catálogo de livros")
    print("3. Saida")
    print()
def exibir_menu_bibliotecario():
    print("Menu Bibliotecário:")
    print("1. Pesquisar livro")
    print("2. Cadastrar livro")
    print("3. Catálogo de livros")
    print("4. Remover livro")
    print("5. Remover usuário")
    print("6. Saida")
    print()

def registrar_o_log(mensagem):
    with open("log.txt", "a") as arquivo_log:
        arquivo_log.write(f"{mensagem}")
#(obs) Funções de cadastro e remoção
def cadastrar_pessoa(lista, tipo):
    try:
        nome = input(f"Digite o nome completo do {tipo}: ")
        while True:
            matricula = input(f"Digite o número de matrícula (9 dígitos): ")
            if len(matricula) == 9 and matricula.isdigit():
                break
            else:
                print("Número de matrícula inválido. Tente novamente.")
        senha = getpass.getpass(f"Digite a senha do {tipo}: ")

        lista.append({'nome': nome, 'matricula': matricula, 'senha': senha})
        registrar_o_log(f"{tipo.capitalize()} '{nome}' cadastrado com matrícula '{matricula}'.")
        print()
        print(f"{tipo.capitalize()} cadastrado com sucesso!")
        print()
    except Exception as e:
        print(f"Erro ao cadastrar {tipo}: {e}")
    finally:
        print(f"Fim do processo de cadastro de {tipo}.")
        print()
def remover_bibliotecario():
    try:
        matricula = input("Digite o número de matrícula do bibliotecário a ser removido: ")
        for bibliotecario in bibliotecarios:
            if bibliotecario['matricula'] == matricula:
                bibliotecarios.remove(bibliotecario)
                print("Bibliotecário removido com sucesso!")
                registrar_o_log(f"Bibliotecário '{bibliotecario['nome']}' removido.")
                print()
                return
        print("Matrícula não encontrada.")
    except Exception as e:
        print(f"Erro ao remover bibliotecário: {e}")
        print()
    finally:
        print("Fim do processo de remoção de bibliotecário.")
        print()
# Funções do login
def login(tipo):
    try:
        nome = input("Digite o nome : ")
        senha = getpass.getpass("Digite a senha: ")
        matricula = input("Digite a matrícula: ")
        print()
        lista = usuarios if tipo == "usuário" else bibliotecarios
        for pessoa in lista:
            if pessoa['nome'] == nome and pessoa['senha'] == senha and pessoa['matricula'] == matricula:
                print(f"Login de {tipo} bem-sucedido!")
                registrar_o_log(f"{tipo.capitalize()} '{nome}' fez login.")
                print()
                return True
        print("Credenciais inválidas.")
        print()
        return False
    except Exception as e:
        print(f"Erro ao fazer login de {tipo}: {e}")
        return False
    finally:
        print(f"Fim do processo de login de {tipo}.")
        print()
# Funções de gerenciamento de livros
def cadastrar_livros():
    try:
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano do livro: ")
        local = input("Digite a localização do livro no catálogo: ")
        tipo = input("O livro está disponível online ou físico? (online/físico): ")
        print()
        print("Gêneros disponíveis: Romance, Fantasia, Ficção Científica, Ensino Médio, Faculdade")
        genero = input("Digite o gênero do livro: ")

        if genero not in livros:
            print("Gênero inválido. Livro não cadastrado.")
            return

        livros[genero].append({'nome': nome, 'autor': autor, 'ano': ano, 'local': local, 'tipo': tipo})
        livros[genero].sort(key=lambda x: (x['nome'], x['autor'], x['ano']))
        print("Livro cadastrado com sucesso!")
        registrar_o_log(f"Livro '{nome}' cadastrado no gênero '{genero}'.")
        print()
        print()
    except Exception as e:
        print(f"Erro ao cadastrar livro: {e}")
        print()
    finally:
        print("Fim do processo de cadastro de livro.")
        print()
def remover_livro():
    try:
        nome = input("Digite o nome do livro a ser removido: ")
        encontrado = False
        for genero in livros:
            for livro in livros[genero]:
                if livro['nome'] == nome:
                    livros[genero].remove(livro)
                    print("Livro removido com sucesso!")
                    encontrado = True
                    return
        if not encontrado:
            print("Livro não encontrado.")
    except Exception as e:
        print(f"Erro ao remover livro: {e}")
    finally:
        print("Fim do processo de remoção de livro.")
        print()

def buscar_binaria(lista, chave, campo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista == chave:
            return lista[meio]
        elif lista < chave:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

def buscar_livro():
    try:
        print("Buscar Livro:")
        print("1. Buscar por Nome do Livro")
        print("2. Buscar por Autor e Ano")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Observação: coloque o nome do livro com letras maiuscula e com o devido espaçamento!")
            print("Qualquer duvida veja o catalogo!")
            nome = input("Digite o nome do livro: ")
            for genero in livros:
                resultado = buscar_binaria(livros[genero], nome, 'nome')
                if resultado:
                    print(f"Gênero: {genero}, Nome: {resultado['nome']}, Autor: {resultado['autor']}, Ano: {resultado['ano']}, Local: {resultado['local']}, Tipo: {resultado['tipo']}")
                    if resultado['tipo'] == 'físico':
                        opcao = input("Deseja pedir emprestimo? (s/n): ")
                        if opcao.lower() == 's':
                            print("Livro pedido com sucesso!")
                            print("Por favor, vá ate a biblioteca busca-lo")
                            print()
                    else:
                        opcao = input("Deseja acessar o livro online? (s/n): ")
                        if opcao.lower() == 's':
                            print("Acessando o livro online...")
                    return
            print("Livro não encontrado.")
        elif opcao == '2':
            autor = input("Digite o nome do autor: ")
            ano = input("Digite o ano do livro: ")
            for genero in livros:
                resultados = [livro for livro in livros[genero] if livro['autor'].lower() == autor.lower() and livro['ano'] == ano]
                if resultados:
                    for resultado in resultados:
                        print(f"Gênero: {genero}, Nome: {resultado['nome']}, Autor: {resultado['autor']}, Ano: {resultado['ano']}, Local: {resultado['local']}, Tipo: {resultado['tipo']}")
                        if resultado['tipo'] == 'físico':
                            opcao = input("Deseja pedir emprestado? (s/n): ")
                            if opcao.lower() == 's':
                                print("Livro pedido com sucesso!")
                        else:
                            opcao = input("Deseja acessar o livro online? (s/n): ")
                            if opcao.lower() == 's':
                                print("Acessando o livro online...")
                    return
            print("Livro não encontrado.")
        else:
            print("Opção inválida. Tente novamente.")
            print()
    except Exception as e:
        print(f"Erro ao buscar livro: {e}")
        print()
    finally:
        print("Fim do processo de busca de livro.")
        print()
def listar_livros():
    try:
        generos_ordenados = sorted(livros.keys())
        for genero in livros:
            print(f"Gênero: {genero}")
            livros[genero].sort(key=lambda x: x['nome'])
            if livros[genero]:
                for livro in livros[genero]:
                    print(f"  Nome: {livro['nome']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Local: {livro['local']}, Tipo: {livro['tipo']}")
            else:
                print("Nenhum livro cadastrado nesse gênero.")
                print()
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
    finally:
        print("Fim do processo de listagem de livros.")
        print()

def listar_pessoas(lista, tipo):
    try:
        lista_ordenada = sorted(lista, key=lambda x: x['nome'].lower())
        print(f"Lista de {tipo}s cadastrados:")
        for pessoa in lista_ordenada:
            print(f"Nome: {pessoa['nome']}, Matrícula: {pessoa['matricula']}")
        print()
    except Exception as e:
        print(f"Erro ao listar {tipo}s: {e}")
    finally:
        print(f"Fim do processo de listagem de {tipo}s.")
        print()
def remover_pessoa(lista, tipo):
    try:
        matricula = input(f"Digite o número de matrícula do {tipo} a ser removido: ")
        for pessoa in lista:
            if pessoa['matricula'] == matricula:
                lista.remove(pessoa)
                print(f"{tipo.capitalize()} removido com sucesso!")
                return
        print("Matrícula não encontrada.")
        print()
    except Exception as e:
        print(f"Erro ao remover {tipo}: {e}")
        print()
    finally:
        print(f"Fim do processo de remoção de {tipo}.")
        print()

def main():
    try:
        while True:
            print("Bem-vindo ao Sistema de Biblioteca Virtual")
            admin_nome = input("Digite o nome de administrador: ")
            admin_senha = getpass.getpass("Digite a senha de administrador: ")
            print()
            if admins.get(admin_nome) == admin_senha:
                while True:
                    exibir_menu_principal_admin()
                    opcao = input("Escolha uma opção: ")

                    if opcao == '1':
                        print("Você escolheu a opção de cadastrar novo usuário")
                        cadastrar_pessoa(usuarios, "usuário")
                    elif opcao == '2':
                        print("Você escolheu a opção de cadastrar bibliotecário")
                        cadastrar_pessoa(bibliotecarios, "bibliotecário")
                    elif opcao == '3':
                        print("Você escolheu a opção de remover bibliotecário")
                        remover_bibliotecario()
                    elif opcao == '4':
                        print(f"Saida do administrador.")
                        print()
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Credenciais de administrador inválidas.")
                break
            while True:
                exibir_menu_principal_acesso()
                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    if login("usuário"):
                        while True:
                            exibir_menu_usuario()
                            opcao_usuario = input("Escolha uma opção: ")

                            if opcao_usuario == '1':
                                buscar_livro()
                            elif opcao_usuario == '2':
                                listar_livros()
                            elif opcao_usuario == '3':
                                print("Saida do usuário.")
                                print()
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                                print()
                    else:
                        print("Credenciais de usuário inválidas.")
                        return
                        print()
                elif opcao == '2':
                    if login("bibliotecário"):
                        while True:
                            exibir_menu_bibliotecario()
                            opcao_bibliotecario = input("Escolha uma opção: ")

                            if opcao_bibliotecario == '1':
                                buscar_livro()
                            elif opcao_bibliotecario == '2':
                                cadastrar_livros()
                            elif opcao_bibliotecario == '3':
                                listar_livros()
                            elif opcao_bibliotecario == '4':
                                remover_livro()
                            elif opcao_bibliotecario == '5':
                                remover_pessoa(usuarios, "usuário")
                            elif opcao_bibliotecario == '6':
                                print("Saida do bibliotecário.")
                                print()
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                elif opcao == '3':
                    print("Você escolheu a opção de listar usuários")
                    listar_pessoas(usuarios, "usuário")
                elif opcao == '4':
                    print("Você escolheu a opcão de listar bibliotecário")
                    listar_pessoas(bibliotecarios, "bibliotecário")
                elif opcao == '5':
                    print("Saindo do sistema...")
                    print("bye bye continue a ler...")
                    return
                else:
                    print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro no sistema: {e}")
    finally:
        print("Sistema encerrado.")

if __name__ == "__main__":
    main()