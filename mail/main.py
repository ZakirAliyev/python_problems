import pyautogui
import time


def yazdir(coordinate, metin, sayi):
    pyautogui.click(coordinate)

    for _ in range(sayi):
        pyautogui.typewrite(metin)
        pyautogui.press('enter')
        time.sleep(0.1)


konum = (481, 695)
metin = "Eleme onueme onu"
tekrar_sayisi = 1000

yazdir(konum, metin, tekrar_sayisi)
