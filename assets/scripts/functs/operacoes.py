import re
import math

class Operadores:
    def __init__(self):
        self.soma = lambda a, b: float(a) + float(b)
        self.subtracao = lambda a, b: float(a) - float(b)
        self.multiplicacao = lambda a, b: float(a) * float(b)
        self.divisao = lambda a, b: float(a) / float(b) if float(b) != 0 else float('inf')
        self.inteiro = lambda a, b: float(a) // float(b)
        self.quadrado = lambda a, b: float(a) ** float(b)
        self.raiz_quadrada = lambda a: math.sqrt(float(a))

    @staticmethod
    def pegaOperacao(expressao):
        valores = []
        operators = []

        # Splitting the expression into numbers and operators
        partes = re.findall(r'[+\-*/^()]|\d+\.\d+|\d+', expressao)

        for parte in partes:
            if parte.replace('.', '').isdigit(): valores.append(float(parte))
            else: operators.append(parte)

        # Initialize total with the first operand
        total = valores[0]

        # Iterate through operators and operands to perform calculations
        for i, operador in enumerate(operators):
            valor = valores[i + 1]

            if operador == '+':
                total = Operadores().soma(total, valor)
            elif operador == '-':
                total = Operadores().subtracao(total, valor)
            elif operador == '/':
                total = Operadores().divisao(total, valor)
            elif operador == '*':
                total = Operadores().multiplicacao(total, valor)
            elif operador == '^':
                total = Operadores().quadrado(total, valor)
            # Add more operations as needed

        return total
