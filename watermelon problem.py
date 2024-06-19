wi=int(input("enter the weight of the watermelon:"))

if(wi%2!=0 or wi==2):
    print("No,it is odd")
else:
    x=wi/2
    if(x%2==0):
        print("Yes,in this case 1st friend gets ",x,"kilo's and 2nd friend gets ",x,"kilo's")

    else:
        print("Yes,in this case 1st friend gets ",x-1,"kilo's and 2nd friend gets ",x+1,"kilo's")

