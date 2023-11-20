print("\nRate the following from a scale of 1 - 10:\n")
loan_size = int(input('How Large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))
print()

loan_approved = False

if loan_size >= 5:
    if (credit_history >= 7 and income >= 7):
        loan_approved = True
    elif (credit_history >= 7 or income >= 7) and down_payment >= 5:
        loan_approved = True
    else:
        loan_approved = False
        
if loan_size <= 5:
    if credit_history < 4:
        loan_approved = False
    elif income >= 7 or down_payment >= 7:
        loan_approved = True
    elif income >= 4 and down_payment >= 4:
        loan_approved = True
    else: 
        loan_approved = False
        
if loan_approved:
    print('Loan approved')
else:
    print("Loan not approved.")
    print()