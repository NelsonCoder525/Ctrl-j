import pyautogui
import time

REPETICOES = 1403
INTERVALO = 0.2

print(f"Iniciando em 5 segundos... ({REPETICOES} repeticoes)")
time.sleep(5)

for i in range(REPETICOES):
    pyautogui.hotkey('ctrl', 'j')
    time.sleep(INTERVALO)
    if (i + 1) % 100 == 0:
        print(f"{i + 1}/{REPETICOES} concluidos...")

print("Finalizado!")
