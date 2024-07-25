class KeyboardFuncts:
    def __init__(self, object):
        self._keyboard = None
        self.operators = {'+', '-', '÷', 'x'}  # Assuming these are valid musical notes
        self.object = object  # Assuming PianoLayout is the class or object to play notes

    def _keyboard_closed(self):
        # Unbind the keyboard event handler
        if self._keyboard:
            self._keyboard.unbind(on_key_down=self._on_keyboard_down)
            self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        key_pressed = keycode[1]

        # Check if the pressed key is a valid musical note
        if key_pressed.lower() in self.operators or key_pressed.isnumeric():
            try: self.object.pega_tecla(key_pressed)
            except Exception as e: print(f"Error getting key: {e}")
            
        elif key_pressed == "delete": self.object.limpar_resultado()
        elif key_pressed == "enter": self.object.mostra_resultado()
