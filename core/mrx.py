import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)
delay_print
delay_print("\033[1;91m    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ \033[1;93m░░   ░▒ ░\n")
delay_print("\033[1;91m  ░        ░░   ░   ░   ▒   ░░          ░     ░░   ░     \033[1;93m░    ░\n")
delay_print("\033[1;91m            ░           ░  ░            ░  ░   ░         \033[1;93m░    ░\n")
delay_print("\033[1;92m               Developed by: '\033[1;9MrSec80-\033[1;93mX\033[1;92m'   v_1.88           \033[1;92m")
print('\033[1;92m')
