# Katelyn Curtiss 
# January 13 2024
# Local Scope Challenges

def greet(fname):
    print(f'Hello {fname}.')


def count_vowels(word, vowel):
    vowels= "aeiou"
    count = 0

    for char in word:
        if char.lower() in vowel:
            count += 1
            return count 
        
result = count_vowels("Goldfish")
print(f"The number of vowels in 'Goldfish' is {result}")
