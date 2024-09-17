from datetime import *

menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

while True:
  opcao = input(menu)

  match opcao.upper():

    case "D":
      valor = float(input("Informe o valor do depósito: "))

      if valor > 0:
        saldo += valor
        extrato += f"[{datetime.now().isoformat(' ', 'seconds')}] Depósito: R$ {valor:.2f}\n"
      else:
        print("Operação abortada: O valor informado é inválido, digite um valor maior que 0.")

    case "S":
      if numero_saques >= LIMITE_NUMERO_SAQUES:
          print("Operação abortada: Número máximo de saques excedido.")
      elif saldo <= 0:
        print("Operação abortada: A conta não possui saldo no momento.");
      else:
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
          print("Operação abortada: A conta não possui saldo o suficiente.")
        elif valor > limite:
          print("Operação abortada: O valor informado excede a quantia limite.")
        elif numero_saques >= LIMITE_NUMERO_SAQUES:
          print("Operação abortada: Número máximo de saques excedido.")  
        elif valor <= 0:
          print("Operação abortada: O valor informado é inválido, digite um valor maior que 0.")

        else:
          saldo -= valor
          extrato += f"[{datetime.now().isoformat(' ', 'seconds')}] Saque: R$ {valor:.2f}\n"
          numero_saques += 1
        
    
    case "E":
      print("EXTRATO".center(50, "="))
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("".center(50, "="))

    case "Q":
      break;

    case _:
      print("Operação invalida: Selecione novamente a operação desejada.")