'''
    Simple, remove the spaces from the string, then return the resultant string.
'''
def no_space(x):
    newString = ""
    for letra in x:
        if letra != " ":
            newString += letra
    return newString

# Boas práticas
def no_space(x):
    return x.replace(' ' ,'')