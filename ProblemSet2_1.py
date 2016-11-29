"""
#Variables being used:
balance
annualInterestRate
monthlyPaymentRate

#required math
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + 
                            (Monthly interest rate x Monthly unpaid balance)

#required output
Month: 1
Minimum monthly payment: 168.52
Remaining balance: 4111.89
"""
#-------------------------------------------
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#to keep track of the month
month = 0

#calculating the monthly interest rate
monthlyInterestRate = (annualInterestRate / 12.0)

#to be used in for-loop
monthlybalance = 0
minimumMonthlyPayment = 0
totalpaid = 0

for month in range (1,13):
         
    minimumMonthlyPayment = round((balance * monthlyPaymentRate),2)
    totalpaid = totalpaid + minimumMonthlyPayment
    updatedBalance = balance - minimumMonthlyPayment
    balance = round((updatedBalance + (updatedBalance * monthlyInterestRate)),2)
    
    print "Month: "+str(month)
    print "Minimum monthly payment: "+str(minimumMonthlyPayment)
    print "Remaining balance:  "+str(balance)
    
print "Total paid: "+str(totalpaid)
print "Remaining balance:  "+str(balance)