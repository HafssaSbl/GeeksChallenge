user_word = input("Entrez un mot : ")

result = ""

for char in user_word:
    if len(result) == 0 or char != result[-1]:
        result += char

print("Mot sans doublons consécutifs :", result)
