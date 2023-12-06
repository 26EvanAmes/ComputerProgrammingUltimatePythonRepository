def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False
print(is_alliteration("and", "apple"))

def count_vowels(word):
    vowels = 0
    for letters in word:
        if letters in "aeiou":
            vowels = vowels + 1
    return vowels
print(count_vowels("hello grady carlson"))

def count_numbers(string):
    digits = 0
    for parts in string:
        if parts in "1234567890":
            digits = digits + 1
    return digits
print(count_numbers("abc123"))

def count_target_letters(word, char):
    samechars = 0
    for letters in word:
        if letters in char:
            samechars = samechars + 1
    return samechars
print(count_target_letters("a", "abc123 grady a3a4a5"))

def in_alphabetical_order(word):
    alphabetical = True
    first = "a"
    for letters in word:
        if letters < first:
            alphabetical = False
        else:
            first = letters
    return alphabetical
print(in_alphabetical_order("abcder"))

def alternate_case(word):
    casechange = True
    result = ""
    for letters in word:
        if casechange == False:
            casechange = True
            result = result + letters
        elif casechange == True:
            letters = letters.upper()
            result = result + letters
            casechange = False
    return result
print(alternate_case("python"))

def remove_vowels(word):
    result = ""
    for letters in  word:
        if letters in "aeiou":
            pass
        else:
            result = result + letters
    return result
print(remove_vowels("python"))

def to_camel_case(phrase):
    uppercase = False
    result = ""
    for chars in phrase:
        if uppercase == True:
            chars = chars.upper()
            result = result + chars
            uppercase = False
        else:
            if chars in " ":
                uppercase = True
            else:
                result = result + chars
    return result
print(to_camel_case("a very useful pot"))

def to_snake_case(phrase):
    result = ""
    for chars in phrase:
        if chars in " ":
            chars = "_"
            result = result + chars
        else:
            result = result + chars
    return result
print(to_snake_case("a very useful pot"))
