# Problem 3: Create a function that takes a string and returns the number (count) of vowels contained within it.
def VowelCount(word):
    count = 0
    for ch in word:
        if ch.lower() in ['a','e,','i','o','u']:
            count += 1
    return count

word = input("Enter a string : ")
print(f'The vowels count in {word} has {VowelCount(word)} Vowels')
