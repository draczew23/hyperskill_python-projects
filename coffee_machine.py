ESPRESSO = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'cost': 4}
LATTE = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'cost': 7}
CAPPUCINO = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'cost': 6}

OPTIONS = ["buy", "fill", "take", "remaining", "exit"]

class CoffeeMachine:
    def __init__(self):
       self.machine_status = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'cups': 9, 'money': 550}
     
    def print_machine_status(self, machine_status):
        """Prints machine status"""

        print("The coffee machine has: ")
        print(str(self.machine_status['water']) + " of water")
        print(str(self.machine_status['milk']) + " of milk")
        print(str(self.machine_status['coffee_beans']) + " of coffee beans")
        print(str(self.machine_status['cups']) + " of disposable cups")
        print(str(self.machine_status['money']) + " of money")
     
    def buy_coffee(self, coffee_type):
        """It changes machine status based on coffee type """
        global ESPRESSO
        global LATTE
        global CAPPUCINO
        
        if coffee_type == "1":
            if self.status_check(ESPRESSO) == True:
                self.machine_status['water'] = self.machine_status['water'] - ESPRESSO['water']
                self.machine_status['milk'] = self.machine_status['milk'] - ESPRESSO['milk']
                self.machine_status['coffee_beans'] = self.machine_status['coffee_beans'] - ESPRESSO['coffee_beans']
                self.machine_status['cups']  = self.machine_status['cups'] - 1
                self.machine_status['money'] = self.machine_status['money'] + ESPRESSO['cost']
        
        elif coffee_type == "2":
            if self.status_check(LATTE) == True:
                self.machine_status['water'] = self.machine_status['water'] - LATTE['water']
                self.machine_status['milk'] = self.machine_status['milk'] - LATTE['milk']
                self.machine_status['coffee_beans'] = self.machine_status['coffee_beans'] - LATTE['coffee_beans']
                self.machine_status['cups'] = self.machine_status['cups'] - 1
                self.machine_status['money'] = self.machine_status['money'] + LATTE['cost']
                
        elif coffee_type == "3":
            if self.status_check(CAPPUCINO) == True:
                self.machine_status['water'] = self.machine_status['water'] - CAPPUCINO['water']
                self.machine_status['milk'] = self.machine_status['milk'] - CAPPUCINO['milk']
                self.machine_status['coffee_beans'] = self.machine_status['coffee_beans'] - CAPPUCINO['coffee_beans']
                self.machine_status['cups'] = self.machine_status['cups'] - 1
                self.machine_status['money'] = self.machine_status['money'] + CAPPUCINO['cost']  
          
    def fill_machine(self):
        """Fills machine with ingridients and cups"""
        #global machine_status
    
        water = int(input("Write how many ml of water do you want to add:"))
        self.machine_status["water"] = self.machine_status["water"] + water
    
        milk = int(input("Write how many ml of milk do you want to add:"))
        self.machine_status["milk"] = self.machine_status["milk"] + milk
    
        coffee_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        self.machine_status["coffee_beans"] = self.machine_status["coffee_beans"] + coffee_beans
    
        cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.machine_status["cups"] = self.machine_status["cups"] + cups
        
        print()
    def take_money(self):
        """Takes all the money"""
       # global machine_status
    
        print("I gave you $" + str(self.machine_status['money']))
        self.machine_status['money'] = 0
        
    def machine_options(self, OPTIONS_LIST):
        """Provides managment"""
    
        while True:
            #print_machine_status(machine_status)
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            print()
    
            if action == OPTIONS_LIST[0]:
                choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                self.buy_coffee(choice)
            elif action == OPTIONS_LIST[1]:
                self.fill_machine()
            elif action == OPTIONS_LIST[2]:
                self.take_money()
            elif action == OPTIONS_LIST[3]:
                self.print_machine_status(self.machine_status)
                print()
            elif action == OPTIONS_LIST[4]:
                break
            
    def status_check(self, coffee_type):
        """Checks if it is enough resources"""
    
        cond1 = self.machine_status["water"] < coffee_type["water"]
        cond2 = self.machine_status['milk'] < coffee_type['milk']
        cond3 = self.machine_status['coffee_beans'] < coffee_type['coffee_beans']
        cond4 = self.machine_status['cups'] == 0
        if cond1:
            print("Sorry, not enough water!")
            print()
            return False
        elif cond2:
            print("Sorry, not enough milk!")
            print()
            return False
        elif cond3:
            print("Sorry, not enough coffee beans!")
            print()
            return False
        elif cond4:
            print("Sorry, not enough disposable cups!")
            print()
            return False
        else:
            print("I have enough resources, making you a coffee!")
            print()
            return True

coffee_machine = CoffeeMachine()
coffee_machine.machine_options(OPTIONS)
        
