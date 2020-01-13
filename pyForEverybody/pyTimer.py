import time
import os

from click.termui import clear
while True:
  localtime = time.localtime()
  result = time.strftime("%a %I:%M:%S %p", localtime)
  print(result)
  time.sleep(1)
  os.system('cls')
  