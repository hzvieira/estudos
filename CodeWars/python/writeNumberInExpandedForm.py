'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
'''
def expanded_form(num):
    string = ''
    for mult, dezena in zip(range(len(str(num)), 0, -1), str(num)):
        if int(dezena) == 0:
            if(mult == 1):
                string = string[:-3]
            continue
        string += dezena
        for zero in range(mult - 1, 0, -1):
            string += '0'
        if mult != 1:
            string += ' + '
    return string

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')