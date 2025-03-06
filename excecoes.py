print("Exemplo de captura de excções")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro: {e}")
    raise ValueError("Tipo de Variável incompativel")
else :
    print(f"Resultado: {resultado}")