print("Welcome to our Store \n")

sum=0
while True:
    userInput=input("Enter the item price or press q for quit \n")
    if userInput!='q':
        sum=sum+int(userInput)
        print('Yout total order value :',sum)
    
    else:
        print("Thanks for shopping with us ")
        break
        