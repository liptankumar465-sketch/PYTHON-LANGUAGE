import pattern
#! LIST COMPREHSNIONS:
# ?----------------------------------------------------------------
pattern.line()
# todo: Example: Orgnaige a list
domains = ['www.google.com', 'openai.com',
           'localhost', 'WWW.DATAWITHBARAAN.COM']

cleaned = [
    d.lower().replace('www.', '') #? Data Trans --> 3
    for d in domains              #? Loop       --> 1
    if '.' in d                   #? Filter     --> 2
]

print('Original Domain: ', domains)
print('Cleaned Domain: ', cleaned)
