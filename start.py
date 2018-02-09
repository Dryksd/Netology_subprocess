import subprocess
import os
import sys

os.makedirs((os.getcwd())+'/Result', exist_ok=True) # создали директорию для foto


files = os.listdir(os.getcwd()+'/Source')  # список с foto


p = subprocess.Popen('convert.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE)


def Aim_To_Result ():
    for i in files:
        p.stdin.write(bytes((i),'utf-8'))





