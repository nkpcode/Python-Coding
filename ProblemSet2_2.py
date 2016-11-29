balance = 3329
annualInterestRate = 0.2

monthlyinterestrate = (annualInterestRate / 12.0)


month = 0
remainingbalance = balance
payingpermonth = 0
moneypaid = 0
updatedbalance =0
monthlyunpaidbalance = 0


while (remainingbalance > 0):
    remainingbalance = balance
    monthlyunpaidbalance = 0
    payingpermonth = payingpermonth + 0.01
    for month in range(1,13):

        #subtracting the fixed per month amont from the balance
        monthlyunpaidbalance = remainingbalance - payingpermonth
        
        #finding out what the new balance with interest will be
        remainingbalance = monthlyunpaidbalance + \
        (monthlyinterestrate * monthlyunpaidbalance)        
    
print "Lowest Payment: "+str(payingpermonth)
    
