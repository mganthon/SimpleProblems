n = input("Enter a number.\n--> ")
sum = 0
for i in range(1,n+1):
    if (i % 5 == 0 or i % 3 == 0) : 
        sum += i 
print("sum: " + str(sum))