class Operadores:
	soma = lambda a, b, c, d: c(a) + d(b)
	subtracao = lambda a, b, c, d: c(a) - d(b)
	multiplicacao = lambda a, b, c, d: c(a) * d(b)
	divisao = lambda a, b, c, d: c(a) / d(b)
	inteiro = lambda a, b, c, d: c(a) // d(b)
	quadrado = lambda a, b, c, d: c(a) ** d(b)

	def is_float(string):
		try:
			float_value = float(string)
			return True
		except ValueError: return False

	def pegaTipo(valorUm, valorDois):
		um, dois = int, int

		if Operadores.is_float(valorUm): um = float
		elif Operadores.is_float(valorDois): dois = float

		return [um, dois]

	@classmethod
	def pegaOperacao(cls, valores):
		total = ""
		tipos = Operadores.pegaTipo(valores[0], valores[2])

		for v in valores:
		    if v == '+': total = cls.soma(valores[0], valores[2], tipos[0], tipos[1])
		    elif v == '-': total = cls.subtracao(valores[0], valores[2], tipos[0], tipos[1])
		    elif v == '÷': total = cls.divisao(valores[0], valores[2], tipos[0], tipos[1])
		    elif v == 'x': total = cls.multiplicacao(valores[0], valores[2], tipos[0], tipos[1])

		if total != None: return total
