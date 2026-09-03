word = input("Enter a word: ")

print("Letters:")

for letter in word:
    print(letter)

print("Numbered letters:")

counter = 1

for letter in word:
    print(f"{counter}. {letter}")
    counter = counter + 1

print(f"The word has {len(word)} letters.")