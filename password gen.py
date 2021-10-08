import random
import string
print("hello sir welcome to the password generator programme")

len = int(input('Enter the length of password please '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all,len)
password = "".join(temp)
print(password)
