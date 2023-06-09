import tokenize
from io import BytesIO

code = '''
for i in range(5):
    print(i)
'''

# Conversion du code en un flux de bytes
code_bytes = code.encode('utf-8')

# Création d'un générateur de tokens
tokens = tokenize.tokenize(BytesIO(code_bytes).readline)

# Parcours des tokens et affichage
for token in tokens:
    print(token)