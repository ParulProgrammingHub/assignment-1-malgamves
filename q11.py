#Q11

def compound_interest(principle,time,rate) :
    a = ( 1 + (rate/100))**t
    intrst = principle*a - principle 
    print("Compound Interest is %d" %intrst)




prin = input("Enter the Principle:")
time = float(input("Enter the Time:"))
rate = float(input("Enter the Rate:"))
simple_interest(prin,time,rate)
