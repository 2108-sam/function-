def vowel(message):
    """Counts the vowels in a string"""
    VOWEL = "aeiou"
    total = 0

    for letter in message:
        if letter.lower() in VOWEL:
            total += 1

    return total


text = input("Enter your message: ")
result = vowel(text)
print(f"The total number of vowels are {result}")