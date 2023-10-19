# Inicialize uma lista vazia para armazenar os registros de estudantes
registros_de_estudantes = []

# Função para adicionar um novo registro de estudante
def adicionar_registro():
    nome = input("Digite o nome do estudante: ")
    id_estudante = input("Digite o ID do estudante: ")
    notas = input("Digite as notas do estudante separadas por espaços: ")
    
    # Divida as notas em uma lista
    notas = notas.split()
    
    # Crie um dicionário com as informações do estudante
    estudante = {
        'Nome': nome,
        'ID': id_estudante,
        'Notas': [float(nota) for nota in notas]
    }
    # Adicione o estudante à lista de registros
    registros_de_estudantes.append(estudante)
    print("Registro de estudante adicionado com sucesso!")

# Função para exibir todos os registros de estudantes
def listar_registros():
    if not registros_de_estudantes:
        print("Nenhum registro de estudante encontrado.")
        return
    
    print("Lista de Registros de Estudantes:")
    for i, estudante in enumerate(registros_de_estudantes, 1):
        print(f"Estudante {i}:")
        print(f"Nome: {estudante['Nome']}")
        print(f"ID: {estudante['ID']}")
        print(f"Notas: {', '.join(map(str, estudante['Notas']))}")
        print()

# Função para procurar um estudante pelo ID
def procurar_por_id(id_procurado):
    for estudante in registros_de_estudantes:
        if estudante['ID'] == id_procurado:
            print("Registro do estudante encontrado:")
            print(f"Nome: {estudante['Nome']}")
            print(f"ID: {estudante['ID']}")
            print(f"Notas: {', '.join(map(str, estudante['Notas']))}")
            return
    print(f"Estudante com o ID {id_procurado} não encontrado.")

# Função para calcular e exibir a média de notas de todos os estudantes
def calcular_media_notas():
    if not registros_de_estudantes:
        print("Nenhum registro de estudante encontrado para calcular a média.")
        return
    
    total_notas = 0
    total_estudantes = len(registros_de_estudantes)
    
    for estudante in registros_de_estudantes:
        total_notas += sum(estudante['Notas'])
    
    media = total_notas / total_estudantes
    
    print(f"Média de notas de todos os estudantes: {media:.2f}")

# Função para salvar os registros de estudantes em um arquivo CSV
def salvar_registros_em_arquivo(filename):
    try:
        with open(filename, 'w') as file:
            for estudante in registros_de_estudantes:
                linha = f"{estudante['Nome']},{estudante['ID']},{','.join(map(str, estudante['Notas']))}\n"
                file.write(linha)
        print(f"Registros de estudantes foram salvos no arquivo {filename}")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os registros: {str(e)}")

# Função para carregar registros de estudantes de um arquivo CSV
def carregar_registros_de_arquivo(filename):
    try:
        with open(filename, 'r') as file:
            registros_de_estudantes.clear()  # Limpa os registros existentes
            for linha in file:
                partes = linha.strip().split(',')
                if len(partes) == 3:
                    nome, id_estudante, notas_str = partes
                    notas = [float(nota) for nota in notas_str.split(',')]
                    estudante = {
                        'Nome': nome,
                        'ID': id_estudante,
                        'Notas': notas
                    }
                    registros_de_estudantes.append(estudante)
        print(f"Registros de estudantes foram carregados do arquivo {filename}")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os registros: {str(e)}")

# Função para exibir o menu
def exibir_menu():
    print("\nSistema de Gerenciamento de Registros de Estudantes")
    print("1. Adicionar um novo registro de estudante")
    print("2. Exibir lista de registros de estudantes")
    print("3. Procurar um estudante por ID")
    print("4. Calcular a média de notas de todos os estudantes")
    print("5. Salvar registros de estudantes em um arquivo")
    print("6. Carregar registros de estudantes de um arquivo")
    print("7. Sair")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-7): ")

    if opcao == "1":
        adicionar_registro()
    elif opcao == "2":
        listar_registros()
    elif opcao == "3":
        id_procurado = input("Digite o ID do estudante que deseja procurar: ")
        procurar_por_id(id_procurado)
    elif opcao == "4":
        calcular_media_notas()
    elif opcao == "5":
        nome_arquivo = "registros_estudantes.csv"
        # nome_arquivo = input("Digite o nome do arquivo para salvar os registros: ")
        salvar_registros_em_arquivo(nome_arquivo)
    elif opcao == "6":
        nome_arquivo = "registros_estudantes.csv"
        # nome_arquivo = input("Digite o nome do arquivo para carregar os registros: ")
        carregar_registros_de_arquivo(nome_arquivo)
    elif opcao == "7":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-7).")









