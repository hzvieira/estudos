# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    #go for it
    novoTexto = ''
    palavras = text.split(" ")
    
    for num, palavra in zip(range(0, len(palavras)), palavras):
        
        for char in range(0, len(palavra)):
            novoTexto = novoTexto + palavra[len(palavra) - 1 - char]
        
        if len(palavras) != num + 1:
            novoTexto += ' '
    
    return novoTexto