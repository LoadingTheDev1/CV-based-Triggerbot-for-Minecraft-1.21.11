import ctypes
import time
from pynput import mouse

magenta = 0xEF709F  
pink = 0xFF4DFF  
yellow  = 0x55FFFF  

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()

gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

_active = False
def _on_click(x, y, button, pressed):
    global _active
    if button == mouse.Button.x2: #mouse 5
        _active = pressed

mouse.Listener(on_click=_on_click).start()

sw, sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
mx, my = sw // 2, sh // 2


magentay = None
crity = None

print("hold mouse 5 to scan")

while True:
    if _active:
        hdc = user32.GetDC(0)

        if magentay is None or crity is None:
            
            for offset in range(-50, 50):
                color = gdi32.GetPixel(hdc, mx, my + offset)
                
                if color == magenta and magentay is None:
                    magentay = my + offset
                    print(f"mag y: {magentay} | set offset to: {offset}")
                
                if (color == pink or color == yellow) and crity is None:
                    crity = my + offset
                    print(f"crit y: {crity} | set offset to: {offset}")

        user32.ReleaseDC(0, hdc)
    
    time.sleep(0.01)