import random
chars = "abcddefghijklmnopqrstuvwxyz12345678910$&@(,.')"
length = int(input('enter the char length'))
password =""
for a in range(length):
 password+=random.choice(chars)
 print(password)
