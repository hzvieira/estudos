'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''
def high(x):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pontuacao, pontuacaoMaiorPalavra, maiorPalavra = 0, 0, ''
    for palavra in x.split(" "):
        pontuacao = 0
        for letra in palavra:
            pontuacao += alfabeto.index(letra) + 1
        if (pontuacao > pontuacaoMaiorPalavra):
            pontuacaoMaiorPalavra = pontuacao
            maiorPalavra = palavra
    return maiorPalavra
