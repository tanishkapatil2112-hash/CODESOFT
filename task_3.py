import random
import string

length_of_string=int(input("Enter the password length"))

characters=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(length_of_string):
    password+=random.choice(characters)

print("DONE WITH THE GENERATION OF PASSWORD",password)