#coding:utf-8

#Impressão de bytecode é o código que a maquina virtual do python entede

#C:\dev\excript\app-comerciais-kivy\aulas\Aulas\13-Estapas da Importação\__pycache__
import ferramentas

def func(l):
    print("Fala Galera!")


import dis

dis.dis(func)