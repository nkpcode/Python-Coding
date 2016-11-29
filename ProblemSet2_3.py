balance = 3329
annualInterestRate = 0.2

monthlyinterestrate = (annualInterestRate / 12.0)
lower = balance/12.0
upper = balance * ((1+monthlyinterestrate)**12) /12.0
bisection = 0

month = 0
remainingbalance = balance
payingpermonth = 0
moneypaid = 0
updatedbalance =0
monthlyunpaidbalance = 0


while (abs(remainingbalance) > 0.01):
    remainingbalance = balance
    monthlyunpaidbalance = 0
#    payingpermonth = payingpermonth + 0.01
    bisection = (upper+lower)/2.0
 #   print "lower "+str(lower)
#    print "bisection"+str(bisection)
#   print "higher "+str(higher)
    payingpermonth = bisection
    
        
    for month in range(1,13):

        #subtracting the fixed per month amont from the balance
        monthlyunpaidbalance = remainingbalance - payingpermonth
        
        #finding out what the new balance with interest will be
        remainingbalance = monthlyunpaidbalance + \
        (monthlyinterestrate * monthlyunpaidbalance)
                
#    print "remainingbalance"+str(remainingbalance)
#    print "payingpermonth"+str(payingpermonth)
    
    
    if(remainingbalance > 0):
        lower = bisection
#        print "lower "+str(lower)
    elif(remainingbalance < 0):
        
        upper = bisection
 #       print "higher "+str(higher)
        
    if(abs(remainingbalance) <= 0.01):
        break
        
    
print "Lowest Payment: "+str(round(payingpermonth,2))
    
