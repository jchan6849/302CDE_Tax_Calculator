import sys
import os

def progressive(income1, income2, method):
    if method == "alone":
        mpf1 = income1 * 0.05
        if mpf1 > 18000:
            mpf1 = 18000
        income_net = income1 - mpf1 - 132000

    if method == "joint":
        mpf1 = income1 * 0.05
        if mpf1 > 18000:
            mpf1 = 18000
        mpf2 = income2 * 0.05
        if mpf2 > 18000:
            mpf2 = 18000
        income_net = income1 + income2 - mpf1 - mpf2 - 264000

    if income_net <= 0:
        tax_p = 0
    elif income_net <= 50000:
        tax_p = income_net * 0.02
    elif income_net <= 100000:
        tax_p = (income_net - 50000) * 0.06 + 1000
    elif income_net <= 150000:
        tax_p = (income_net - 100000) * 0.10 + 4000
    elif income_net <= 200000:
        tax_p = (income_net - 150000) * 0.14 + 9000
    else:
        tax_p = (income_net - 200000) * 0.17 + 16000

    return tax_p

def standard(income1, income2):
    mpf1 = income1 * 0.05
    if mpf1 > 18000:
        mpf1 = 18000
    mpf2 = income2 * 0.05
    if mpf2 > 18000:
        mpf2 = 18000

    tax_s = (income1 - mpf1 + income2 - mpf2) * 0.15
    return tax_s

def single_tax(income):
        tax_p = int(progressive(income, 0, "alone"))
        tax_s = int(standard(income, 0))
        mpf = int(income * 0.05)
        print(f"Your MPF mandatory contribution = {mpf}")
        if tax_p == 0:
            print("Tax Payable By You = 0")
        elif tax_s < tax_p:
            print(f"Tax Payable By You (At Standard Rate) = {tax_s}")
        else:
            print(f"Tax Payable By You (At Progressive Rate) = {tax_p}")
        return mpf, tax_p, tax_s

def married_tax(income1, income2):
        tax_p1 = int(progressive(income1, 0, "alone"))
        tax_s1 = int(standard(income1, 0))
        if tax_p1 == 0:
             sep1 = 0
        elif tax_s1 < tax_p1:
            sep1 = tax_s1
        else:
            sep1 = tax_p1
        tax_p2 = int(progressive(income2, 0, "alone"))
        tax_s2 = int(standard(income2, 0))
        if tax_p2 == 0:
             sep2 = 0
        elif tax_s2 < tax_p2:
            sep2 = tax_s2
        else:
            sep2 = tax_p2
        sep = sep1 + sep2
        tax_p_joint = int(progressive(income1, income2, "joint"))
        tax_s_joint = int(standard(income1, income2))
        if tax_p_joint == 0:
            joint = 0
        elif tax_s_joint < tax_p_joint:
            joint = tax_s_joint
        else:
            joint = tax_p_joint
        mpf1 = int(income1 * 0.05)
        mpf2 = int(income2 * 0.05)
        print(f"Your MPF mandatory contribution = {mpf1}")
        print(f"Your spouse's MPF mandatory contribution = {mpf2}")
        print(f"Tax Payable By You and Your Spouse (Under Joint Assessment) = {joint}")
        print(f"Tax Payable By You and Your Spouse (Under Separate Taxation) = {sep}")
        if joint < sep:
            print(f"Joint Assessment is recommended!")
        else:
            print(f"Separate Taxation is recommended!")
        return mpf1, mpf2, joint, sep
    
def main():
    while True:
        status = input("Please tell me you are Single or Married? \n").strip().lower()

        if status in ["single", "married"]:
            break
        else:
            os.system('cls')
            print("Please enter \"Single\" or \"Married\".")
    if status == "single":
        print("Please enter your income for the year of assessment (Exclude cents).")
        while True:
            try:
                income = int(input())
                if income < 0:
                    raise ValueError
                break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please enter positive integer only.")
                print("Please enter your income for the year of assessment (Exclude cents).")
        single_tax(income)
    elif status == "married":
        print("Please enter your income for the year of assessment (Exclude cents).")
        while True:
            try:
                income1 = int(input())
                if income1 < 0:
                    raise ValueError
                break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please enter positive integer only.")
                print("Please enter your income for the year of assessment (Exclude cents).")
        print("Please enter your spouse's income for the year of assessment (Exclude cents).")
        while True:
            try:
                income2 = int(input())
                if income2 < 0:
                    raise ValueError
                break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please enter positive integer only.")
                print("Please enter your spouse's income for the year of assessment (Exclude cents).")
        married_tax(income1, income2)

if __name__ == "__main__":
    main()
