import csv
f  = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close
def number_of_vowels(wordlist):
    current_vowels = 0
    most_vowels = 0
    most_vowels_word = ""
    for word in wordlist:
        for letters in word:
            if letters in "aeiou":
                current_vowels = current_vowels + 1
        if current_vowels > most_vowels:
            most_vowels = current_vowels
            current_vowels = 0
            most_vowels_word = word
 #           print(most_vowels_word)
        else:
            current_vowels = 0
    return most_vowels_word
print(number_of_vowels(words))

def average_word_length(wordlist):
    sum = 0
    divisor = 0
    for word in wordlist:
        sum = sum + len(word)
        divisor = divisor + 1
    return sum/divisor
print(average_word_length(words))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
As = 0
bs = 0
cs = 0
ds = 0
fs = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    if  percent >= 90:
        As = As + 1
    elif percent >= 80 and percent <= 90:
        bs = bs + 1
    elif percent >= 70 and percent <= 80:
        cs = cs + 1
    elif percent >= 60 and percent <= 70:
        ds = ds + 1
    else:
        fs = fs + 1
print(As, bs, cs, ds, fs)
f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
freshmen_sum = 0
freshmen_divisor = 0
sophmores_sum = 0
sophmores_divisor = 0
juniors_sum = 0
juniors_divisor = 0
seniors_sum = 0
seniors_divisor = 0
for row in reader:
    name, gradelevel, percent = row
    gradelevel = int(gradelevel)
    percent = int(percent)
    if gradelevel == 9:
        freshmen_sum = freshmen_sum + percent
        freshmen_divisor = freshmen_divisor + 1
    elif gradelevel == 10:
        sophmores_sum = sophmores_sum + percent
        sophmores_divisor = sophmores_divisor + 1
    elif gradelevel == 11:
        juniors_sum = juniors_sum + percent
        juniors_divisor = juniors_divisor + 1
    elif gradelevel == 12:
        seniors_sum = seniors_sum + percent
        seniors_divisor = seniors_divisor + 1
    else:
        print("error", gradelevel)
print((freshmen_sum/freshmen_divisor),(sophmores_sum/sophmores_divisor),(juniors_sum/juniors_divisor),(seniors_sum/seniors_divisor))
f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
for row in reader:
    name, gradelevel, percent = row
    gradelevel = int(gradelevel)
    percent = int(percent)
    if gradelevel == 12 and percent <= 60:
        print(name)




f.close()