sent=input("Enter a sentance :")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel_count=0
words=0
reverse=''
for i in sent:
    if i in vowels:
        vowel_count+=1
    words+=1
for j in sent[::-1]:
    reverse+=j
if sent==reverse:
    print(sent,"is palindrome")
else:
    print(sent,"is not palindrome")
print(sent,"contains",vowel_count,"Vowel letters")
print(sent,"contain",words,"words")
print(sent,"'s reversed word is",reverse)