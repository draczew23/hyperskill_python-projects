import math, sys
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Credit Calculator Project")

parser.add_argument('--type', help = "Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help = "Monthly payment", type = int)
parser.add_argument('--principal', help = "Credit principal", type = int)
parser.add_argument('--periods', help = "Count of months", type = int)
parser.add_argument('--interest', help = "Credit interest (rate of interest)", type = float)

# Parse the arguments
args = parser.parse_args()

if args.type not in ['annuity', 'diff']:
    print('Incorrect Parameters')
    exit(0)

if args.type == 'diff' and args.payment != None:
    print('Incorrect Parameters')
    exit(0)

args_list = [args.type, args.payment, args.principal, args.periods, args.interest]
#list of parameters

count = 0
for item in args_list:
    if item == None:
        count += 1

if count > 1:
    print('Incorrect Parameters')
    exit(0)

if args_list[1] != None and args_list[1] < 0 or args_list[2] != None and args_list[2] < 0 or args_list[3] != None and args_list[3] < 0 or args_list[4] != None and args_list[4] < 0.0:
    print('Incorrect Ha ha')
    exit(0)

def nominal_int_calc(credit_interest):
    result = credit_interest / (12 * 100)
    return result

def differiented_pay(cred_prin, nom_int_rate, per_numb):
    result_total = 0
    for m in range(1, per_numb + 1):
        result = math.ceil((cred_prin / per_numb) + nom_int_rate * (cred_prin - ((cred_prin * (m - 1)) / per_numb)))
        result_total += result
        print("Month " + str(m) + ": paid out " + str(result))

        overpayment = result_total - args.principal
        print('Overpayment = ', overpayment)

if args.type == 'diff' and args.periods != None and args.principal != None and args.interest != None:
    differiented_pay(args.principal, nominal_int_calc(args.interest), args.periods)

if args.type == 'annuity' and args.payment != None and args.principal != None and args.interest != None:
   
    nominal_interest_rate = nominal_int_calc(args.interest)
    periods = math.log((args.payment / (args.payment - nominal_interest_rate * args.principal)), 1 + nominal_interest_rate)
    rounded_periods = math.ceil(periods)
    
    overpayment = rounded_periods * args.payment - args.principal

    years = 0
    months = 0

    if rounded_periods % 12 == 0:
        years = rounded_periods / 12
        if years == 1:
            print("You need " + str(int(years)) + " year to repay this credit!")
        else:
            print("You need " + str(int(years)) + " years to repay this credit!")
    else:
        years = int(rounded_periods / 12)
        months = rounded_periods % 12

        if years < 1:
            if months == 1:
                print("You need " + str(months) + " month to repay this credit!")
            else:
                print("You need " + str(months) + " months to repay this credit!")
        elif years == 1 and months == 1:
            print("You need " + str(years) + " year and " + str(months) + " month to repay this credit!")
        elif years == 1 and months != 1:
                print("You need " + str(years) + " year and " + str(months) + " months to repay this credit!")
        elif years != 1 and months == 1:
            print("You need " + str(years) + " years and " + str(months) + " month to repay this credit!")
        else:
            print("You need " + str(years) + " years and " + str(months) + " months to repay this credit!")

    print('Overpayment = ', overpayment)

if args.type == 'annuity' and args.periods != None and args.principal != None and args.interest != None:
    
    nominal_interest_rate = nominal_int_calc(args.interest)
    fraction_up = args.principal * nominal_interest_rate * ((1 + nominal_interest_rate) ** args.periods)
    fraction_down = (1 + nominal_interest_rate) ** args.periods - 1

    annuity_payment = math.ceil(fraction_up / fraction_down)
    overpayment = abs(args.periods * annuity_payment - args.principal)

    print("Your annuity payment = " + str(annuity_payment) + "!")
    print('Overpayment = ', overpayment)

if args.type == 'annuity' and args.periods != None and args.payment != None and args.interest != None:
    
    nominal_interest_rate = nominal_int_calc(args.interest)
    fraction_up = nominal_interest_rate * ((1 + nominal_interest_rate) ** args.periods)
    fraction_down = (1 + nominal_interest_rate) ** args.periods - 1

    credit_principal = int(args.payment / (fraction_up / fraction_down))
    overpayment = args.periods * args.payment - credit_principal

    print("Your credit principal = " + str(credit_principal) + "!")
    print('Overpayment = ', overpayment)
