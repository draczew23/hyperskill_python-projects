import random
import sqlite3

conn = sqlite3.connect('example.s3db')
cur = conn.cursor()

cur.execute('''CREATE TABLE clients (
            pin TEXT, 
            number TEXT, 
            balance INT DEFAULT 0, 
            id INT
);''')

class Account():

    def __init__(self):
        self.pin = ""
        self.card_number = ""
        self.balance = 0

class Banking_Sys():

    clients_accounts = []

    def sum_digits(self, digit):
        if digit < 10:
            return digit
        else:
            SUM = (digit % 10) + (digit // 10)
            return SUM

    def acc_numb_gen(self):
        card_numb = random.randint(0, 9999999999)
        new_card_numb = "400000" + str(card_numb)

        return new_card_numb

    def luhn_acc_numb_validation(self):
        while True:
            cc_num = self.acc_numb_gen()

            # reverse the credit card number
            cc_num = cc_num[::-1]

            # convert to integer list
            cc_num = [int(x) for x in cc_num]

            # double every second digit
            doubled_second_digit_list = list()
            digits = list(enumerate(cc_num, start=1))
            for index, digit in digits:
                if index % 2 == 0:
                    doubled_second_digit_list.append(digit * 2)
                else:
                    doubled_second_digit_list.append(digit)

            # add the digits if any number is more than 9
            doubled_second_digit_list = [self.sum_digits(x)
                                         for x in doubled_second_digit_list]

            # sum all digits
            sum_of_digits = sum(doubled_second_digit_list)

            if (sum_of_digits % 10 == 0) is True:
                break

            else:
                continue

        separator = ""
        reversed_list = cc_num[::-1]
        final_str = separator.join(map(str, reversed_list))
        return final_str

    def create_account(self):
        new_account = Account()

        pin_number = ''.join(str(random.randint(0, 9)) for _ in range(4))
        card_numb = self.luhn_acc_numb_validation()

        new_account.pin = pin_number
        new_account.card_number = card_numb

        print("Your card number:")
        print(new_account.card_number)
        print("Your card PIN:")
        print(str(new_account.pin))
        print()

        self.clients_accounts.append(new_account)
        cur.execute("INSERT INTO clients VALUES (?, ?, ?, ?)",
                    (new_account.pin, new_account.card_number, new_account.balance, 1))
        conn.commit()
        cur.execute("SELECT * FROM  clients")
        data = cur.fetchall()
        for row in data:
            print(row)

    def log_into_account(self):
        input_card_numb = input("Enter your card number:")
        input_pin = input("Enter your PIN:")

        cur.execute("SELECT * FROM  clients")
        data = cur.fetchall()

        for user in data:
            if user[1] == input_card_numb and user[0] == input_pin:
                print("You have successfully logged in!")
                self.logged_options(user[1], user[0])
                break

            else:
                print("Wrong card number or PIN!")
                break

    def show_balance(self, user_numb, user_pin):
        cur.execute("SELECT * FROM  clients")
        data = cur.fetchall()

        for user in data:
            if user[1] == user_numb and user[0] == user_pin:
                print("Balance " + str(user[2]))
                self.logged_options(user)
                break

    def logged_options(self, user_numb, user_pin):
        while True:
            print("1. Balance \n2. Log out \n0. Exit")

            user_input = input()

            if user_input == "1":
                self.show_balance(user_numb, user_pin)

            elif user_input == "2":
                break

            elif user_input == "0":
                print("Bye!")
                exit()

    def main(self):
        while True:
            print("1. Create an account \n2. Log into account \n0. Exit")
            user_input = input()

            if user_input == "1":
                self.create_account()

            elif user_input == "2":
                self.log_into_account()

            elif user_input == "0":
                print("Bye!")
                break


bank_sys = Banking_Sys()
bank_sys.main()
conn.close()
