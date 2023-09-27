numInputs = int(input('Enter number of inputs :'))
if(numInputs<2):
    print("Need atleast 2 numbers")
    exit()
maxNum1 = int(input("Enter Number: "))
maxNum2 = int(input("Enter Number: "))

for x in range(2,numInputs):
    num = int(input("Enter Number: "))
    if(int(num)>maxNum1):
        maxNum2 = maxNum1
        maxNum1=int(num)
    elif(int(num)>maxNum2 and int(num)<maxNum1):
        maxNum2 = int(num)
if maxNum1!=maxNum2:
    print(maxNum2)
else:
    print('All values are same, cannot decide second highest')
