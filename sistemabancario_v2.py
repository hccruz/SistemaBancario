def Deposito(saldo, dep, extrato):
    if dep < 0:
        print('Operação não efetuada. Não aceitamos valores negativos.')
    else:
        saldo += dep
        extrato += f'Depósito: R$ {dep:.2f}\n'
        print(f'Depósito de R$ {dep:.2f} efetuado com sucesso.')
    return saldo, extrato


def Saque(sal=0, saque=0, ext="", lim=0, num_saques=0, lim_saques=0):
    if numeros_saques < LIMITE_SAQUES:
        if saque < 0:
            print('Operação não efetuada. Não aceitamos valores negativos')
        elif saque > sal:
            print(f'Saldo insuficiente. Saldo atual é de R$ {sal:.2f}.')
        elif saque > 500:
            print(f'Limite diário de saque ultrapassado. Digite um valor menor do que R$ {lim:.2f}.')
        else:
            sal -= saque
            num_saques += 1
            ext += f'Saque: R$ {saq:.2f}\n'
            print(f'Saque de R$ {saq:.2f} efetuado com sucesso.')
            print(f'Você ainda pode efetuar {lim_saques - num_saques} saque(s).')
    else:
        print(f'Operação não efetuada. Número total de saques atingiu o limite.')
    return sal, ext, num_saques


def Extrato(saldo, ext=''):
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo atual: R$ {saldo:.2f}')


def Usuario(cpf):
    nome = input('Digite o seu nome: ')
    data_nasc = input('Digite a sua data de nascimento: ')
    logradouro = input('Digite o nome da rua onde você mora: ')
    nro = input('Digite o número da sua casa: ')
    bairro = input('Digite o bairro da sua casa: ')
    cidade = input('Digite a cidade onde você mora: ')
    estado = input('Informe a sigla do estado da sua cidade: ')
    endereco = f'{logradouro}, {nro} - {bairro} - {cidade}/{estado}'
    cliente_dic = {'nome': nome, 'data de nascimento': data_nasc, 'CPF': cpf, 'endereço': endereco}
    return cliente_dic


def Criar_Conta(cliente, num_conta):
    conta_dic = {'agencia': '0001', 'número da conta': num_conta, 'usuário': cliente}
    return conta_dic


menu = """

[u] Cadastro de Usuário(Cliente)
[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3
clientes = []
conta= []
num_conta = 1

while True:

    opcao = input(menu).lower()

    if opcao == 'd':
        print("Depósito")
        dep = float(input('Qual o valor que deseja depositar?: '))
        saldo, extrato = Deposito(saldo, dep, extrato)      

    elif opcao == 's':
        print("Saque")
        saq = float(input('Qual o valor que deseja sacar?: '))
        saldo, extrato, numeros_saques = Saque(sal = saldo, saque = saq, ext = extrato, lim = limite, num_saques = numeros_saques,
         lim_saques = LIMITE_SAQUES)
        
    elif opcao == 'e':
        print("==========Extrato==========")
        Extrato(saldo, ext=extrato)
        print('===========================')

    elif opcao == 'u':
        print("Cadastro de Usuário (Cliente)")
        if clientes != []:
            cpf = input('Digite o seu CPF: ')
            for i in range(len(clientes)):
                if clientes[i]['CPF'] == cpf:
                    print('CPF duplicado')
                    cpf = input('Digite o seu CPF: ')
                    i = 0
        else:
            cpf = input('Digite o seu CPF: ')

        clientes.append(Usuario(cpf))
        print(clientes)

    elif opcao == 'c':
        print("Criar Conta Bancária")
        cpf = input('Digite o CPF do usuário: ')
        for i in range(len(clientes)):
            if clientes[i]['CPF'] == cpf:
                conta.append(Criar_Conta(clientes[i]['nome'], num_conta))
                print(conta)
                num_conta += 1
                break
        else:
            print('Digite um CPF cadastrado ou faça o cadastro de usuário!!!')
    elif opcao == 'q':
        break

    else:
        print("Opção incorreta, digite as opções do menu!!")
