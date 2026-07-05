import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class CalculadoraRitmo(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Inputs del usuario
        self.dist_total_input = toga.TextInput(placeholder='Ej: 10 (Km o Metros)', style=Pack(flex=1))
        self.tiempo_input = toga.TextInput(placeholder='Ej: 45 (Minutos totales)', style=Pack(flex=1))
        self.dist_vuelta_input = toga.TextInput(placeholder='Ej: 1 (Km o Metros)', style=Pack(flex=1))
        
        # Etiqueta de resultado
        self.resultado_label = toga.Label('Resultado: Esperando datos...', style=Pack(padding=(10, 0)))

        # Botón de cálculo
        btn_calcular = toga.Button('Calcular Ritmo', on_press=self.calcular_logica, style=Pack(padding=5))

        # Añadir elementos a la pantalla
        main_box.add(toga.Label('Distancia Total:'))
        main_box.add(self.dist_total_input)
        main_box.add(toga.Label('Tiempo Total en Minutos:'))
        main_box.add(self.tiempo_input)
        main_box.add(toga.Label('Distancia por Vuelta:'))
        main_box.add(self.dist_vuelta_input)
        main_box.add(btn_calcular)
        main_box.add(self.resultado_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calcular_logica(self, widget):
        try:
            d_total = float(self.dist_total_input.value)
            tiempo_min = float(self.tiempo_input.value)
            d_vuelta = float(self.dist_vuelta_input.value)

            if d_vuelta <= 0 or d_total <= 0:
                self.resultado_label.text = "Error: Las distancias deben ser > 0"
                return

            vueltas = d_total / d_vuelta
            t_vuelta_min = tiempo_min / vueltas
            
            minutos = int(t_vuelta_min)
            segundos = round((t_vuelta_min - minutos) * 60)

            if segundos == 60:
                minutos += 1
                segundos = 0

            self.resultado_label.text = f"Vueltas: {round(vueltas, 2)} | Ritmo: {minutos}m {segundos:02d}s"
        except ValueError:
            self.resultado_label.text = "Error: Introduce solo números válidos."

def main():
    return CalculadoraRitmo()

