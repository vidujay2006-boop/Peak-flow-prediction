print("-- Peak Flow Predictor -- ") 
print("\nThis systme is designed to show your % produced based on your predicted PFT (Peak Flow test) blow in L/Min (Litres per min)")

def askGender():
    gen=input("Enter your gender ('m'/'f'): ")
    if gen == 'm'.lower():
        print("You are a male")
        askAgeMale()
    elif gen == 'f'.lower(): 
        print("You are female")
        askAgeMale()

    else: 
        print("Enter a valid gender (m or f) ")
        askGender()



def askAgeMale():
    try:
        age = int(input("Please enter your age: "))
        if age <= 0:
            print("Enter a valid age")
            askAgeMale()
        else:
            print("Test complete")
    except ValueError:
        print("Error: enter a number only")
        askAgeMale()

askGender()

def askHeight(): 
    option=int(input("Enter your height, do you choose to enter in inches (1) or cm (2): ")
               if option == 1: 
                   height_inches=("Eneter your height in inches: ")
                   final_hight = height_inches * 2.54
                   
