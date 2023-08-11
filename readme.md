# RSA Simulator 

## Introduction to RSA and this Project

Welcome to my RSA simulator. RSA is an information encryption method that takes advantage of the difficulty of factoring two extremely large prime numbers. Anyone can encrypt a message using a public key based on two prime numbers. However, their message can only be decrypted by those who have access to the exact prime numbers used. If the prime numbers are large enough, decryption is all but impossible to achieve. 

However, my implementation of RSA is not secure enough to be used in any real-life messaging transactions. Because you should be picking two prime factors that are well below 1000, the numbers are bound to be small enough to break. Therefore, to see how the whole system works, I suggest encoding a fun message, then break it to find the private key ‘d’. Finally, use the private key and the encoded number sequence to decrypt the message and see your original text! Or, even better, start sending encoded messages back and forth with a friend. 

Have Fun! 

## How to Run 

To run the program input "python3 user_rsa.py" on the command line. If the program denies you permission, run "chmod -x ./user_rsa.py" first then try again. 
