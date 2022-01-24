gloss = {}
gloss['variable'] = "It stores values"
gloss['datatypes'] = "It is typess of data like int"
gloss['class'] = 'collection of objects'

print(f'\nDictionary\n = {gloss}')

for i in gloss.keys():
    values = gloss[i]
    print(i, "\n=", values)
