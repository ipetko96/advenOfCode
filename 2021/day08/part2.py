import re
from itertools import permutations

defaultRules = {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}
# defaultSemiRules = {'a': 0, 'b': 6, 'c': 0, 'd': 0, 'e': 4, 'f': 9, 'g': 0}
mapa = defaultRules.fromkeys(defaultRules, '')


def getNumber(mapa, cypher):
    schema = {0: [mapa['a'], mapa['b'], mapa['c'], mapa['e'], mapa['f'], mapa['g']],
              1: [mapa['c'], mapa['f']],
              2: [mapa['a'], mapa['c'], mapa['d'], mapa['e'], mapa['g']],
              3: [mapa['a'], mapa['c'], mapa['d'], mapa['f'], mapa['g']],
              4: [mapa['b'], mapa['c'], mapa['d'], mapa['f']],
              5: [mapa['a'], mapa['b'], mapa['d'], mapa['f'], mapa['g']],
              6: [mapa['a'], mapa['b'], mapa['d'], mapa['e'], mapa['f'], mapa['g']],
              7: [mapa['a'], mapa['c'], mapa['f']],
              8: [mapa['a'], mapa['b'], mapa['c'], mapa['d'], mapa['e'], mapa['f'], mapa['g']],
              9: [mapa['a'], mapa['b'], mapa['c'], mapa['d'], mapa['f'], mapa['g']]}
    translate = defaultRules.fromkeys(schema, '')
    for i in schema:
        translate[i] = ''.join(sorted(schema[i]))
    for i in translate:
        if translate[i] == ''.join(sorted(cypher)):
            return i


# def createMap(matchGroup):
#     pocet = defaultRules.fromkeys(defaultSemiRules, 0)
#     mapa = defaultRules.fromkeys(defaultSemiRules, '')
#     newRules = defaultSemiRules
#     for segment in matchGroup:
#         if segment == 'a' or segment == 'c' or segment == 'd' or segment == 'g':
#             continue
#         else:
#             pocet[segment] += matchGroup.count(segment)
#     for i in mapa:
#         index = list(newRules.keys())[list(newRules.values()).index(pocet[i])]
#         mapa[i] = index
#         newRules.pop(index)
#         pocet.pop(i)
#     return newRules


with open('2021\\day08\\tinput', 'r') as file:
    perms = [''.join(p) for p in permutations('abcdefg')]
    for line in file:
        match = re.match(
            r'(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s\|\s(\w+)\s(\w+)\s(\w+)\s(\w+)', line)
        decoded = ''
        for combination in perms:
            mapa['a'] = combination[0]
            mapa['b'] = combination[1]
            mapa['c'] = combination[2]
            mapa['d'] = combination[3]
            mapa['e'] = combination[4]
            mapa['f'] = combination[5]
            mapa['g'] = combination[6]
            for i in range(1, 10):
                number = match.group(i)
                decoded += str(getNumber(mapa, number))
                if 'None' not in decoded and len(decoded) == 10:
                    print()
                if 'None' in decoded:
                    decoded = ''
                    break
        print(decoded)
        # pocet = defaultRules.fromkeys(defaultRules, 0)
        # mapa = defaultRules.fromkeys(defaultRules, '')
        # newRules = defaultRules
        # for i in range(1, 11):
        #     number = match.group(i)
        #     for segment in number:
        #         pocet[segment] += number.count(segment)
        # for i in mapa:
        #     index = list(newRules.keys())[
        #         list(newRules.values()).index(pocet[i])]
        #     mapa[i] = index
        #     newRules.pop(index)
        #     pocet.pop(i)
        #     decoded = ''
        # createMap(match.group(1))
        # for i in range(11, 15):
        #     number = match.group(i)
        #     decoded += str(getNumber(mapa, number))
        # print()
