#!/usr/bin/env python3

import os

def ffmpeg():
    if not os.path.isfile('/usr/bin/ffmpeg'):
        print("O ffmpeg não está instalado, mas vou instalar pra você!\n")
        os.system("sudo apt install ffmpeg")
        os.system("\n")
        print("\nAgora está tudo pronto!\n")   

def separaArqvs(lista, newlist, format):
    for f in lista:
        if f.endswith(format_ori):
            newlist.append(f)
    return newlist


def converter(diretorio, format_ori, format_final):
    os.chdir(diretorio)
    tmparqvs = os.listdir(diretorio)
    arqvs = []
    print(tmparqvs)
    arqvs = separaArqvs(tmparqvs, arqvs, format_ori)
    if not os.path.exists('Convertidos'):
        os.mkdir("Convertidos")
    if not os.path.exists('Originais'):
        os.mkdir("Originais")
    for i in arqvs:
        arqv_ori = i.replace("'", '\\\'').replace(" ", "\ ")
        arqv_final = arqv_ori.replace(format_ori, format_final)
        os.system(f"ffmpeg -i {arqv_ori} {arqv_final}")
        os.system(f"mv {arqv_final} Convertidos")
        os.system(f"mv {arqv_ori} Originais") 


ffmpeg()
        
diretorio = input("Digite onde está os arquivos: ")
format_ori = input("Digite o formato atual dos arquivos: ")
format_final = input("Digite o formato final: ")

converter(diretorio, format_ori, format_final)
print("\nAcabado!!\n")
