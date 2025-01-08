class person:
    firstname = 'mohammed'
    lastname = 'nihad'
class customer(person):
    def __init__(self, balance):
        self.balance = balance

    def print(self):
        print(self.balance)

    def deposit(self, dep):
        self.balance =self.balance + dep
        print(f"{dep} has been added and the new balance is {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"{amount} has been withdrawn and the new balance is {self.balance}")

print('hello you can either chekc withdraw or deposit on your account')
balance = int(input('please state initial balance: '))
customer1=customer(balance)



def choices():
    choice = input('which one would you like: ')
    while True:
        if choice == 'check':
            customer1.print()
            choices()
        elif choice == 'deposit':
            dep = int(input("Enter the amount to deposit: "))
            customer1.deposit(dep)
            choices()
        elif choice == 'withdraw':
            amount = int(input("Enter the amount to withdraw: "))
            customer1.withdraw(amount)
            choices()
        elif choice == 'exit':
            print("Thank you! Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")
            choices()
choices()
