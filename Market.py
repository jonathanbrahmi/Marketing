# This code is write by jonathan brahmi

import os
import time
import platform
from tqdm import tqdm

logo = '''

            8888888888888888888888
          88        88   88       88
        888       888    888       888
       888        888    888        888
       888        888    888        888
88888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888 
88888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888
  888888888888888888888888888888888888888
     888888888888888888888888888888888

'''

menus = '''

      Tomato = 3 NIS
      cucumber = 2 NIS
      coca coloa = 5 NIS
      chicken = 20 NIS per kg

'''

for i in tqdm(range(10)):
    time.sleep(0.50)

print("[*]Developer on python 3.9")
print("[*]Developer by Jonathan brahmi")
print("[*]Calculator minus operator for Windows 10")
print("[*]Runing on processor", platform.processor())
print("[*]Runing on machine", platform.machine())

print(logo)
print(menus)

print("------------\n")
tomato = int(input("Enter how many tomato>"))
cucumber = int(input("Enter how many cucumber>"))
cola = int(input("Enter how many cola>"))
chicken = int(input("Enter how many chicken>"))
print("------------\n")

print("\nSummary of your order:\n------------\ntomato:" + str(tomato) + "\ncucumbers" + str(cucumber) + "\ncola" + str(
    cola) + "\nchicken" + str(chicken))

sum1 = tomato * 3
sum2 = cucumber * 2
sum3 = cola * 5
sum4 = chicken * 20
summary = sum1 + sum2 + sum3 + sum4

for i in tqdm(range(10)):
    time.sleep(0.50)

print("\n------------")
print("\n You have to pay " + str(summary) + " NIS without VAT")
print("\n You have to pay " + str(summary * 1.17) + " NIS with VAT")
print("------------\n")

os.system("pause")