
sum=0
while True:
    numbers=input("enter numbers = ")
    if numbers =='exit':
        print(sum)
        break
    else:
        sum+=int(numbers)