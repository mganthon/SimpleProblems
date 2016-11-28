n = input("Enter a number.\n--> ")
while True :    
    print("Would you like to compute the sum or poduct?\n")
    option = raw_input("(S\P) -->").upper()
    if option == "S" or "P" :
        break
    print("unknon option:\n")

if option == "S" :
    sum = 0
    for i in range(1,n+1):
            sum += i 
    print("sum: " + str(sum))
elif option == "P" :
    product = 1
    for i in range(1,n+1):
        product *= i 
    print("product: " + str(product))