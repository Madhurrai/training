n=int(input(f'Enter the number of inputs: '))
largest= None
i=0
while i<n:
    num=int(input(f'Enter the numbers'))
    if largest is None or num>largest:
        largest=num
    i=i+1
print(f'The largest number is',largest)

