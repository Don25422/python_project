# A program to check whether a year is a leap year or not
year = 2012

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
else:
        print(year, "is not a leap year")

#  A program to check whether a letter is a consonant or vowel
letter = "a"

if letter in 'aeiou':
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")