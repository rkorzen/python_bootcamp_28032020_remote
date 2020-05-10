from bankomat import CashMachine, NotEnoughSpacForBills, BillException

cash_machine = CashMachine(capacity=8)
cash_machine.put_money([200, 200, 100, 100, 50, 50])


while True:
    operation = input("Podaj typ operacji: [wplata, wyplata, koniec]: ")
    if operation == "koniec":
        break
    elif operation == "wplata":
        bills = input("Podaj liste banknotów rozdzielajac je przecinkiem np:100,100,50,50:  ")
        bills = bills.split(",")
        bills = [int(bill) for bill in bills]
        try:
            cash_machine.put_money(bills)
        except NotEnoughSpacForBills as e:
            print("Error: ", e)
    elif operation == "wyplata":
        amount =int(input("Podaj kwotę do wypłaty: "))
        try:
            bills = cash_machine.withdraw_money(amount)
        except BillException as e:
            print("Błąd: ", e)
        except KeyError as e:
            print("Kwota powinna być wielokrotnością 10 PLN")