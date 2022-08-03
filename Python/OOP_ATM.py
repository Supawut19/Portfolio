class atm:
    def __init__(self, account, sex, birth, years, job, amount):
        self.account = account
        self.sex = sex
        self.birth = birth
        self.years = years
        self.job = job
        self.amount = amount
    def __str__(self):
        print("Auto Trading Machine")

    def profile(self):
        print(f"""
              Name: {self.account}
              Sex: {self.sex}
              Birth: {self.birth}
              Years: {self.years}
              Job: {self.job}
              Balance: {self.amount}
              """)
    def deposit(self, num):
        print(f"Deposit {num} Bath")
        self.amount += num
        print(f"Balance: {self.amount} Bath")
    def withdraw(self, num2):
        print(f"Withdraw {num2} Bath")
        self.amount -= num2
        print(f"Balance: {self.amount} Bath")
    def transfer(self, acc1, person, num3):
        if acc1 == self.account:
            print(f"Transfer to {person} {num3} Bath")
            self.amount -= num3
            print(f"Balance: {self.amount} Bath")
        else:
            print("Your account is not correct, please check and try again")
    def check(self, acc2):
        if acc2 == self.account:
            print(f"Balance: {self.amount} Bath")
        else:
            print("Your account is not correct, please check and try again")