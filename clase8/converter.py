sourceNum = int(input("Enter source number in decimal?"))
targetRadix = int(input ("Enter target radix 2 or 16?"))

if(targetRadix == 2): # Checking the value of targetRadix
    print(bin(sourceNum))
else:
    if(targetRadix == 16):
        print(hex(sourceNum))
    else:
        print("You have entered a wrong target radix",targetRadix)