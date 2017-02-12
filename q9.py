#Q9

def result(per):
    if per < 35:
        print "Fail"
    else:
        print "Pass"


#Assuming test marks are out of 50
sums = 0
for i in range(5):
    mark = input("Enter result")

for i in range(5):
    sums = mark + sums
   
mean = sums/5

per = float((mean*100)/50)
print per
result(per)
