print("Exemplo de importação de módulos")

# Importando o módulo math
from math import sqrt

print(sqrt(16))

import meu_modulo

# Utilizando a função do módulo
msg = meu_modulo.saudacao("shiro")
resultado = meu_modulo.dobro(5)

print(msg)
print(resultado)