import ctypes
import time
import random
from pynput import mouse

MAG_Y = 45  
CRT_Y = -24  

HEX_MAGENTA = 0xEF709F 
HEX_PINK    = 0xFF4DFF 
HEX_YELLOW  = 0x55FFFF 

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()

gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

def _click():
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    time.sleep(random.uniform(0.01, 0.02))
    user32.mouse_event(0x0004, 0, 0, 0, 0)

_active = False
def _on_click(x, y, button, pressed):
    global _active
    if button == mouse.Button.x2: _active = pressed

mouse.Listener(on_click=_on_click).start()

sw, sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
mx, my = sw // 2, sh // 2
T_PX, C_PX = (mx, my + MAG_Y), (mx, my + CRT_Y)

print("bot açık")

while True:
    if _active:
        hdc = user32.GetDC(0)
        target = gdi32.GetPixel(hdc, *T_PX)
        crit = gdi32.GetPixel(hdc, *C_PX)
        user32.ReleaseDC(0, hdc)

        if target == HEX_MAGENTA:
            # havada
            if crit == HEX_PINK:
                _click()
                time.sleep(random.uniform(0.63, 0.66)) # cd
            elif crit == HEX_YELLOW:
                # tıklama oc
                pass
            else:
                # yürüme
                # Standart
                _click()
                time.sleep(random.uniform(0.12, 0.15))

    time.sleep(0.0001)