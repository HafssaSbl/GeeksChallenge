word = input("Entrez un mot : ")

letter_indexes = {}

for index, letter in enumerate(word):
    letter = str(letter)
    
    if letter in letter_indexes:
        letter_indexes[letter].append(index)
    else:
        letter_indexes[letter] = [index]

print(letter_indexes)
