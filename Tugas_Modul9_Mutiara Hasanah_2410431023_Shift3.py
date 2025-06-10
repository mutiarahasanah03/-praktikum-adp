import os
import time
from termcolor import cprint

teks = "Happy Eid         " * 3
langkah = 20
delay = 0.3
durasi = 20
teks_scroller = " " * langkah + teks
n = int(durasi/delay)

for i in range(n):
    os.system('cls')
    cprint('-'*20, 'blue', attrs=['bold'])
    tampilan = teks_scroller[i:i+20]

    if i % 2 == 0:
        cprint(tampilan, 'yellow',attrs=["dark"])
    else:
        cprint(tampilan, 'yellow',attrs=["bold"])
    cprint('-'*20, 'blue', attrs=['bold'])
    time.sleep(delay)