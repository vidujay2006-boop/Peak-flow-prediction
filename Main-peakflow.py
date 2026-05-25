print("-- Peak Flow Predictor -- ") 
print("\nThis systme is designed to show your % produced based on your predicted PFT (Peak Flow test) blow in L/Min (Litres per min)")

def askGender():
    gen=input("Enter your gender ('m'/'f'): ")
    if gen == 'm'.lower():
        print("You are a male")
        askAge()
    elif gen == 'f'.lower(): 
        print("You are female")
        askAge()

    else: 
        print("Enter a valid gender (m or f) ")
        askGender()



def askAge():
    try:
        age = int(input("Please enter your age: "))
        if age <= 0:
            print("Enter a valid age")
            askAge()
        else:
            print("Test complete")
    except ValueError:
        print("Error: enter a number only")
        askAge()

askGender()