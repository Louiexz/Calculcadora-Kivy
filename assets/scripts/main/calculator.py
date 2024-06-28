from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from ..functs.operacoes import Operadores
from ..functs.keyboard_functs import KeyboardFuncts
from kivy.core.window import Window

class Calculator(BoxLayout):
    def __init__(self):
        super(Calculator, self).__init__()
        self.valores = []
        
        # Initialize KeyboardFuncts with self (PianoLayout instance)
        self.keyboard_functs = KeyboardFuncts(object=self)
        self.start_keyboard()
    
    def start_keyboard(self):
        # Request the keyboard and bind the keyboard event handler
        self._keyboard = Window.request_keyboard(self.keyboard_functs._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.keyboard_functs._on_keyboard_down)

    def pega_tecla(self, valor):
        retorno = ""

        if self.valores:
            ultimo = self.valores[-1]
            # Tentar converter valor para float
            try:
                valor_int = int(valor)
                ultimo_float = float(ultimo)
                
                self.valores[-1] = str(ultimo + valor)
            except ValueError:
                # Se não houver um erro ao converter para float, adicionar valor à lista
                try:
                    # Verificar se último pode ser convertido para float
                    ultimo_float = float(ultimo)
                    self.valores.append(str(valor))
                except: pass
                try:
                    # Se não for possível converter último para float, tentar converter valor
                    valor_int = float(valor)
                    self.valores.append(str(valor))
                except: pass

        elif valor.isnumeric(): self.valores.append(str(valor))

        # Atualizar o texto de retorno
        retorno = " ".join(self.valores)
        self.ids.igual.text = retorno

    def mostra_resultado(self):
        try:
            if len(self.valores) >= 3:
                expressao = " ".join(self.valores)
                resultado = str(Operadores.pegaOperacao(expressao))

                self.valores = [resultado]
                self.ids.igual.text = resultado
        except Exception as e:
            print("Erro:", e)
            self.limpar_resultado()

    def limpar_resultado(self):
        self.valores = []
        self.ids.igual.text = ""

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
