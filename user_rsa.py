import re 

def Convert_Text(_string):
    integer_list = []
    
    for i in range(len(_string)):
        character = _string[i] 
        uni_code = ord(character)
        integer_list.append(uni_code)
    
    #for the number of characters in the string 
        # pick the character at point "i" and assign it the value "character"
        # convert that character to an integer 
        # append the integer to the interger_list
    
    return integer_list


def Convert_Num(_list):
    _string = ''
    for i in _list:
        _string += chr(i)
        
    # For each integer in _list
        # convert the integer back to it's equivlant character and add it to _sting 
        
    return _string



def FME(a,n,b): # 'a' will be repeatably squared. 'n' will be converted to binary. 
        result = 1 
        square = a
    
        while (n > 0): #start of loop to convert 'n' to binary
            k = n % 2  # extracts the LSD 
            if (k == 1): 
                result = (result * square) % b 
            square = (square * square) % b # square multiplies itself mod b, if the remainder of k is 0
            n = n // 2 # must divide by two, remainder is 'floored, in order to break out of loop
            
        return result
    

def Euclidean_Alg(a, b):
    x = a 
    y = b
    while (y != 0):
        r = x % y 
        x = y 
        y = r
        
    # while the remainder is quotient is equal to zero 
        # find the mod of the first two integers and capture the remainder in 'r' 
        # update x's value to y's
        # update y's value to the remainder's 
        
        
    return x     

def Find_Public_Key_e(p, q):
    
    
    e = 1 # initailize e to 1 
    n = ((p-1)*(q-1))
    x = 0
    while (x != 1): # if x (which is the gcd of n,e) is found, the program will stop 
        if (e != p and e != q): # make sure e is not equal to p or q
            e = e + 1 # increases e by 1 

            x = Euclidean_Alg(n,e) #finds the GCD of n and e
    
    return e


def Find_Private_Key_d(e, p, q):
   
    m = e
    n_0 = ((p-1)*(q-1))
    n = ((p-1)*(q-1))
    
    (s1,t1) = (1,0) # initialize the value of m = 1(m) + 0(n)
    (s2,t2) = (0,1) # intialize the value of n = 0(m) + 1(m) 
    while (n > 0): 
        k = m % n 
        q = m // n

        m = n  
        n = k 
        (s1_hat,t1_hat) = (s2,t2) #the Bezout coefficients assigned from n to m prime
        (s2_hat,t2_hat) = (s1 - (q * s2)),(t1 - (q * t2)) # thw Bezout coefficients assigned from k (m mod n) to n prime 

        (s1,t1) = (s1_hat, t1_hat) 
        (s2,t2) = (s2_hat, t2_hat)
        
    print(s1) 
    if (s1 < 0): # check to make sure that our 'd' is not a negative int
        while (s1 < 0):
            s1 = s1 + n_0 # add modulo n prime until we reach a postive int
            
    return s1 # s1 should be our inverse 'd'

def Encode(n, e, message):
    
    int_list = Convert_Text(message) # calls the function Convert_Text and passes in a string.
                                     # the return of the function is capture by value int_list 
    cipher_text = []
    for i in range(len(int_list)): 
        code = FME(int_list[i],e,n)
        cipher_text.append(code) 
    
    #for each element in the range of int_list 
        #call the FME function, passing the element at "i", along with the parameters n and the public key 'e' 
        # the return of the funtion is assigned to the varible code
        # append that result to the cipher_text list 
    
    
    return cipher_text


def Decode(n, d, cipher_text):
    
    message = ''
    decode = [ ]
    
    for i in range(len(cipher_text)):
        code = FME(cipher_text[i], d, n)
        decode.append(code)
    # for an element in the range of cipher_text
        # call the FME function again with the element at 'i' in cipher_text. Also passing the private key 'd' and n 
        # return the results of the FME function and assign the value to "code"
        # append the converted int to a new list "decode"
    
    message = Convert_Num(decode) 
    
    # after the for loop has fully completed, call the Convert_Num function with the decode list as a parameter 
    # return the results from the Convert_Num function and assign the value to the string messages 
    
    
    return message


def factorize(n,e):
    # n is a number, return the smallest factor of n
    
    for i in range(2,n-1):
        if n % i == 0:
            p = i 
            q = n / p 
            d = Find_Private_Key_d(e, p, q)
            return d
    # for an element leading up to the value of n
        # if n can be divided by and element without producing a remainder 
            # that element is assigned to p 
            # q is assigned to n divided by the new p 
            # the we run the function that gives us a the senders private key 
            # return the private key found 
         
    return False 

##### ^ Initial Code ^ ######

def user_menu(): ##  prints out options for the user to implement diffrent aspects of the RNA process
    print("**************************")
    print("Welcome Gentle Encrypter!")
    print("**************************")
    print("\nWhat are we doing with your senitive infomation today?")
    
    print("\n 1. Encrypt Message")
    print(" 2. Decrypt Message")
    print(" 3. Break a Code")
    print(" 4. Quit Menu") 
    print("\n")
    

def prime_check(n): # like the factorize function, with a few modifications 
                    # will determine if value is a prime number or not 
    
    for i in range(2,n-1):
        if n % i == 0:
            return False 
    
    #for an element in the every number leading up to n 
        # if dividing n by an element outputs no remainder, n must not be a prime number 
    
    return True  

    
    
def get_pq(): # gives user sufficient p and q values
    print("\nFirst things first, give me two prime numbers: p and q")
    print("\nALSO!!! Keep in mind I need your p to be smaller than your q")
    
    prime_p = True
    prime_q = True
    user_p = int(input("\nGive me a Prime Number, p -> ")) 
                 
    while (prime_p == True):
        valid_p = prime_check(user_p) #runs the prime check function, testing whether the 'p' enter by user is a prime number 
        if (valid_p == True): # if the users 'p' is a valid prime number, end while loop
            print("\nNice work! p is a valid prime number!")   
            prime_p = False
        elif (valid_p == False): # if the users 'p' is not a valid prime number, make them enter a diffrent 'p' to test again 
            print("\nOpps..that's is not a valid prime number...try again")
            user_p = int(input("\nGive me a Prime Number, p -> ")) 
        
    
       
     
    print("\nGREAT! Now give me a prime number 'q', that is larger than 'p'") 
    user_q = int(input("\nGive me a Prime Number, q -> "))
    while (prime_q == True):          
         
        valid_q = prime_check(user_q)  # runs check to make sure the q entered is a valid prime number
        if (valid_q == True): # if the check prime function returns true
            if(user_q > user_p):  # if the value for 'q' is greater than the value of 'p' 
                print("\nNice work! q is a valid prime number and is larger than p.")
                return user_p, user_q # return valid p and q values 
            
            else: # else make them re-enter prime 'q' that is greater than 'p' 
                print("\nDid you make sure it was larger than p?")
                print("\nLets try again!")
                user_q = int(input("\nGive me a Prime Number, q ->  "))

        else: # the check prime function returns false
            print("\nHmmm, that's not a valid prime number.")
            print("\nLets try again!")
            user_q = int(input("\nGive me a Prime Number, q -> ")) # gives users another chance to enter a valid 'q'


def user_encode(p,q): # gives users a Public key and the value of n 
    print("\nThis is your 'p':", p, "and this is your 'q':", q)                          
    print("\nLet's multiply", p, "and", q, "to get your 'n'")
    n = p * q  # get the value of n by multiplying p and q
    print("\nEureka! Your 'n' is:", n)
    print("\nNow let's use your values to establish a Public Key.. give me a moment...")
    e = Find_Public_Key_e(p,q) # returns the users public key 
    print("\nOK, your Public Key is:", e)
        
    return n, e 
    
 
    
    
def brackets(message): # checking to make sure the encoded message was not entered with brackets included 

    brackets = re.compile(r'[\[\]]') # assign brackets to check for [ and ] characters 
    return len(re.findall(brackets, message)) # returns the number of times the ([ ]) characters were found in the passed message

def readable(message): # checking to make sure the coded message passed to decryption  
                       # does not look like this: ଟсȢऩޟɽ୳ޟ׶щ७৹ޟدȢ߂щ৹ɽऩщޟƬщ߂ɽщޟ˾७щऩщ֤
    
    text = re.compile(r'[a-zA-Z0-9\^\$\.[\]\{\}\-\?\*\+\(\)\|\\!@#%&=]') # text is assigned to check a message for all 
                                                                         # legal characters in a message
    return len(re.findall(text, message)) # returns the number of times a legal character was found in the message


def user_message(n,e): # passes in the users Public key and n value, returns their encoded message
    message = input("\nIt's finally time to write your secret message....have at it! -> ") # user gets to write their own message
    
    encrypt = Encode(n, e, message)  # returns the users encoded message 
    
    print("\nSuccess! Here is your encoded message....",encrypt) 
    
    return 0; 
    
                       
def main():
    
    menu_open = True 

    user_menu() # presents users with the menu 
    user_pick = int(input("Pick a menu item! -> "))  # allows users to pick a menu item 
    
    
    
    while (menu_open == True): 
        if (user_pick < 1 or user_pick > 4): # if the user picks a value that's out of range, 
                                             # they're given a chance to pick again 
            
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Invalid Selection: Select an item within range")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("")
            user_menu()
            user_pick = int(input("Pick a menu item!: ")) 
        
        elif (user_pick == 4): # the user is asking to exit the program gracefully 
        
            print("\nThanks for stopping by! And remember [3243, 2421, 9547, 2101, 2344. 8573] !!") 
            print("\nEnding program ....") 
            menu_open = False 

        elif (user_pick == 1): # the user want to encode a message   
            print("\nOK, sure! Why not. But before we can encode your 'secret' message....we need to establish a few things...") 
            
            user_input = input("\nDo you already have an Public Key and 'n'? (y for Yes) (n for No) -> ")
                         # if yes then the program gets to skip a few steps 
                
            if (user_input == "n"): # the user entered no, they do not have these values
                p, q = get_pq() # call this function to get the user's p and q
                n, e = user_encode(p,q) # using the returned p and q, get the users public key and e value 
                user_message(n, e) # using the public key and e value, the user can now encode the function 
                menu_open = False # end the program gracefully 
                
            elif(user_input == "y"): # we don't have to call the get_pq or user_encode function 
                n = int(input("\nWhat is your 'n'? -> "))
                e = int(input("\nWhat is your Public Key? -> ")) 
                user_message(n, e) # after the user manually gives us the values of n and e, we ask them to create a message
                menu_open = False
            else: # the user input something other than y or n 
                 print("\nThat was not a valid answer, try again..") 
                 user_menu()
                 user_pick = int(input("\nPick a menu item! ->  ")) # returns to main menu 
        
            
        elif (user_pick == 2): # user wants to decrypt a message
            print("\nSo....you found a secret message, and you don't know what to do with it! Ok, lets take a look!") 
        
            have_d = input("Do you know your senders Private Key 'd'? (y for Yes) (n for No) -> ") 
        
            if (have_d == "n"): # the user needs to factorize the senders 'n' to find the Private key 
                print("\nDarn!, then select menu item 3, and we'll try and break your code") # they can do this in menu item 3
                user_menu()

                user_pick = int(input("\nPick a menu item! -> "))  
                
            elif (have_d == "y"):  # runs them through the process of decryption 
                d = int(input("\nGreat! What is the Private Key 'd'? -> ")) 
                n = int(input("\nNow what is the senders 'n'? -> ")) 
                        
                input_message = input("\nNow we're cooking, input the sender's message and I'll translate it for you!...INPUT WITHOUT BRACKETS!! -> ")
                # we don't want the user to input the message with brackets 
                # because it will mess up the transition from a string list to an int list
                
                result = brackets(input_message) # runs the bracket function and assigns result with the number of 
                                                 # brackets found in the user's input 
                
                if (result != 0): # we don't want any brackets passed through in the users coded message  
                    print("\nYour input has brackets!!! Please Summit input WITHOUT BRACKETS") 
                    user_pick = int(input("\nPick a menu item! -> ")) 
                    user_menu()

                
                else: # the user did not have any brackets passed through in their coded message
                     # the users input is one long string, to read it, we need to convert it into a int list
                        
                    message = input_message.split(",") # split into a list of strings, finding each element by comma 
                    sender_code = []

                    for i in message:
                        sender_code.append(int(i))
                        
                        # for an element in the user list of strings
                        # convert that element into an int, and add it to a new list 

                    decrypt = Decode(n, d, sender_code) # we can now correctly pass the message through the decoder 
                                        
                    read = readable(decrypt) # if the message looks like this: ଟсȢऩޟɽ୳ޟ׶щ७৹ޟدȢ߂щ৹ɽऩщޟƬщ߂ɽщޟ˾७щऩщ֤
                                            # we want to warn the user that there's likly a miscalculation in one of their values
                    if (read == 0): #if there is not a single legal character in the transplated message
                                    # it likly looks something like this...ଟсȢऩޟɽ୳ޟ׶щ७৹ޟدȢ߂щ৹ɽऩщޟƬщ߂ɽщޟ˾७щऩщ֤
                        print("\nThe message could not be translated! Make sure all of your values are correct") 
                        user_pick = int(input("\nPick a menu item! -> ")) # force the user to redo the process
                        user_menu()
                    
                
                    else: # the message contain legal characters. May or maynot make sense 
                        print("\nYour message says:", decrypt) 
                        menu_open = False
            else: # the user enter something else than 'y' or 'n' 
                print("\nYes? No? Maybe so...well which one is it?!!")
                user_menu()
                user_pick = int(input("\nPick a menu item! -> ")) # return to menu 

                        
                              
        elif (user_pick == 3): # the user does not know the senders private key and needs to break the code 
            print("\nTo break the code, and find the Private Key, I'll need the senders 'n' and Public Key!") 
            
            n = int(input("\nWhat is the senders 'n'? -> "))
            e = int(input("\nWhat is the senders 'Public Key'? -> ")) 
            
            d =  factorize(n,e) # runs the factorize function with a few modifications from the original 
                    
            print("\nCode Broken! The Private Key is:", d) 
            
            menu_open = False
            
            
        
            
          
    
if __name__ == '__main__': 
    main()
