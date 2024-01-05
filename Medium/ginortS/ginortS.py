# Enter your code here. Read input from STDIN. Print output to STDOUT
odddigits = []
evendigits=[]
uppercase_letters = []
lowercase_letters = []

S=input()

for char in S:
    if char.isdigit():
        if int(char) % 2 == 0:
            evendigits.append(char)
        elif int(char) % 2 !=0:
            odddigits.append(char)
    elif char.isupper():
        uppercase_letters.append(char)
    elif char.islower():
        lowercase_letters.append(char)

odddigits=sorted(odddigits)
evendigits=sorted(evendigits)
uppercase_letters=sorted(uppercase_letters, key= lambda x: x.upper())
lowercase_letters=sorted(lowercase_letters, key= lambda x: x.lower())
odddigits=''.join(odddigits)
evendigits=''.join(evendigits)
lowercase_letters=''.join(lowercase_letters)
uppercase_letters=''.join(uppercase_letters)

print(lowercase_letters+uppercase_letters+odddigits+evendigits)