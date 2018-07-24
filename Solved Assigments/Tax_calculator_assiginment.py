#assignment 1

"""
Aurthor:Prathmesh Agrawal
Batch:Feb 2018
Assigment:
annual income,investment by person
taxable income=annual income - investment
if loan then new tax amt= oldTax- principle
>2.5 no tax
between 2.5 and <5 then 10% between 5 and <10 then 20% else 30%
"""

annualIncome=int(input("Enter your Annual Income: "))
investment=int(input("Enter your Investment this year: "))
loanCh=input("Do you have Taken loan this year?(y/n): ")

if loanCh.upper()=="Y":
    loanAmount=int(input("Enter Your loan amount: "))
else:
    loanAmount=0
taxAmount=annualIncome-investment-loanAmount
if taxAmount>250000:
    if taxAmount<500000:
        tax=(taxAmount-250000)*0.10
    elif taxAmount<1000000:
        tax=(250000*0.10)+((taxAmount-500000)*0.20)
        print((taxAmount-500000)*0.20)
    else:
        tax=(250000*0.10)+(500000*0.20)+(taxAmount-1000000)*0.30
        print((taxAmount-1000000)*0.30)
            
else:
    tax=0
print("your applicable tax amount is",taxAmount,"and tax is",tax)
    
