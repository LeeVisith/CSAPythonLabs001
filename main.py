#App 1

user_input = input("Enter a word: ")
double = (char * 2 for char in user_input)
output = ''.join(double)

print(f"{output}")

#App 2

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_range = input("Enter a range of letters: ")

start, end = alphabet_range.split('-')
first = alphabet.index(start.lower())
last = alphabet.index(end.lower())

letter = ''.join(alphabet[first:last+1])

if start.isupper() and end.isupper():
    result = letter.upper()
else:
    result = letter
print(result)
