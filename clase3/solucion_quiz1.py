hours = int(input ("Enter the total working hours:"))
payRate = int (input ("Enter the hourly pay rate:"))
if (hours <= 40): # If hours are less than or equal to 40
    regPay = hours * payRate # regular pay will be calculated.
    print ("Regular pay:",regPay)
else: # if hours are greater than 40
    regPay = 40 * payRate
    overTime = hours - 40
    increasePay = payRate + (payRate / 2)
    overPay = increasePay * overTime
    print ("Regular pay:",regPay)
    print("Overtime pay:",overPay)
    print ("Total pay:",regPay+overPay)