'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''

def is_isogram(string):
    #your code here
    string = string.lower()
    print(string)
    for index, letra in enumerate(string):
        for i, caracter in enumerate(string):
            if (letra == caracter and index != i):
                return False
 
    return True