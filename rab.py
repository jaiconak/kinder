import random



import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

 # this will create an empty list 
password_list = []

def pwGen(nr_letters,nr_numbers,nr_symbols):
    try:
        
        # Todo 1 we need to loop for how many letters (nr_letters) they wanted
        for i in range(nr_letters): #<-0 theres no need to declare 0 in the arguments
            password_list.append(random.choice(letters)) #PULL FROM THE LIST OF CHARACTERS DECLARED******************
        for i in range(nr_numbers): #3 would be your starting point and nr_number would be your max
            password_list.append(random.choice(numbers))
        for i in range(nr_symbols):
            password_list.append(random.choice(symbols))
            return password_list
    except Exception as e:
        print (f"MUST BE A VALID INT! NO FLOATS NO STRINGS NO CHARACTERS! {e}")

        


def main ():
    print("Welcome to the PyPassword Generator!")
    numLetters = int(input("How many letters would you like in your password?\n"))
    numSymbols = int(input(f"How many symbols would you like?\n"))
    numNumbers = int(input(f"How many numbers would you like?\n"))
    passwordGenerator = pwGen(numLetters,numNumbers,numSymbols)
    
    print(passwordGenerator)


if __name__=="__main__":
    main()





