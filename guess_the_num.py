import random
num=random.randint(1,100)
n=int(input("Guess the number:"))
while num!=n:
    if n>num:
        print("Lower than",n)
    elif n<num:
        print("Higher than",n)
    n=int(input("Enter a number:"))
print(f"Congratulations!, {n} is the secret number")
    