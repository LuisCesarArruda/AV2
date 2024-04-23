def create_transaction():
    print_message = lambda: print("Criando transação...")
    print_message()
    payment_type = input("Digite o tipo de pagamento (Dinheiro/Crédito): ")
    process_payment = lambda type: receive_cash() if type.lower() == "dinheiro" else request_account_details()
    process_payment(payment_type)

def receive_cash():
    print_message = lambda: print("Recebendo dinheiro...")
    print_message()
    amount = int(input("Digite a quantidade de dinheiro recebida: "))
    print_receipt = lambda amount: print(f"Imprimindo recibo de pagamento para {amount} reais...")
    print_receipt(amount)
    return_payment_receipt()

def return_payment_receipt():
    print_message = lambda: print("Devolvendo recibo de pagamento...")
    print_message()
    complete_transaction()

def request_account_details():
    print_message = lambda: print("Solicitando detalhes da conta...")
    print_message()
    account_details = input("Digite os detalhes da conta: ")
    request_payment_from_bank(account_details)

def request_payment_from_bank(account_details):
    print_message = lambda: print(f"Solicitando pagamento do banco para a conta {account_details}...")
    print_message()
    confirm_approval_from_bank()

def confirm_approval_from_bank():
    print_message = lambda: print("Confirmando aprovação do banco...")
    print_message()
    close_transaction()

def complete_transaction():
    print_message = lambda: print("Transação concluída!")
    print_message()

def close_transaction():
    print_message = lambda: print("Transação fechada!")
    print_message()

create_transaction()
