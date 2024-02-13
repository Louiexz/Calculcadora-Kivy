from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

from operacoes import Operadores

Config.set('graphics', 'resizable', 1)

class Calculator(BoxLayout):
    valores = []

    def pega_tecla(self, valor):
    	retorno = ""
    	
    	if self.valores:
    		ultimo = self.valores[-1]

    		if valor.isdigit() and ultimo.isdigit(): ultimo += valor
    		else: self.valores.append(valor)
    	elif valor.isdigit(): self.valores.append(valor)

    	for v in self.valores: retorno += v + " "
    	self.ids.igual.text = str(retorno)


    def mostra_resultado(self):
        try:
        	resultado = Operadores.pegaOperacao(self.valores)

        	self.valores = [str(resultado)]
        	self.ids.igual.text = str(resultado)
        except Exception as e:
        	print(e)
        	self.limpar_resultado()

    def limpar_resultado(self):
        self.valores = []
        self.ids.igual.text = ""

class CalculatorApp(App):
    icon = "icon/calculadora.png"
    def build(self): return Calculator()
