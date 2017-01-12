def format_token(token):
    token_word = token.split('|')[0]
    token_class = token.split('|')[1]

    if token_word + '\n' in open("query.txt", encoding='UTF-8').readlines():
        id_of_token = open("query.txt", encoding='UTF-8').readlines().index(token_word + '\n')
    else:
        file = open("query.txt", 'a', encoding='UTF-8')
        file.write(token_word + '\n')
        file.close()
        id_of_token = open("query.txt", encoding='UTF-8').readlines().index(token_word + '\n')
    if token_class + '\n' in open("slots.txt", encoding='UTF-8').readlines():
        _class = token_class
        id_of_class = open("slots.txt", encoding='UTF-8').readlines().index(token_class + '\n')
    else:
        _class, id_of_class = 0, len(open("slots.txt", encoding='UTF-8').readlines()) - 1
    return id_of_token, token_word, id_of_class, _class


def create_token_line(_id, id_of_token, token, id_of_class, _class):
    return "{0:4}|S0 {1:3}:1 |# {2:31}|S2 {3:3}:1|# {4}".format(_id, id_of_token, token, id_of_class, _class)


#sentence = 'расходы|S рязанская|L-location область|O на|O образование|S-education в|O 2016|T'


def tokenize(sentence_string, id_):
    result_multiline_string = ''
    id_bos = open("query.txt", encoding='UTF-8').readlines().index('BOS' + '\n')
    id_eos = open("query.txt", encoding='UTF-8').readlines().index('EOS' + '\n')
    bos_string = '{0:4}|S0 {1:3}:1 |# BOS                            |S2  32:1|# 0\n'.format(id_, id_bos)
    eos_string = '{0:4}|S0 {1:3}:1 |# EOS                            |S2  32:1|# 0\n'.format(id_, id_eos)
    tokens = sentence_string.split(' ')
    for token in tokens:
        result_multiline_string += create_token_line(id_, *format_token(token)) + '\n'

    return bos_string + result_multiline_string + eos_string

def sort_query():
    lines = open("query.txt", "r", encoding='UTF-8').readlines()
    lines.sort()
    file = open("query.txt", "w", encoding='UTF-8')
    file.writelines(lines)
    file.close()


i = 1
for string in open('sent.txt', encoding='UTF-8',mode='r').readlines():
    print(tokenize(string, i))
    i += 1
sort_query()
