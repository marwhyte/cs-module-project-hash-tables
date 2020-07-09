# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
finalHash = {}
letterCount = {}
finalText = ""

with open("ciphertext.txt", encoding="utf-8") as cipherText:
    cipher = cipherText.read()

topLetters = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L",
              "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

for letter in cipher:
    if letter.isalpha():
        if letter not in letterCount:
            letterCount[letter] = 1
        else:
            letterCount[letter] += 1

sortThisList = list(letterCount.items())
sortThisList.sort(reverse=True, key=lambda item: item[1])
print(sortThisList)
for i, element in enumerate(topLetters):
    finalHash[sortThisList[i][0]] = topLetters[i]

for letter in cipher:
    if letter.isalpha():
        finalText += finalHash[letter]
    else:
        finalText += letter
print(finalText)
