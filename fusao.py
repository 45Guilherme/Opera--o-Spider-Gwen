

import rarfile

rarfile.UNRAR_TOOL = "UnRAR.exe"

imagens_extraidas = []


with rarfile.RarFile("Homem-aranha Noir -2008.cbr") as gibi:
    imagens = gibi.namelist()
    for imagem in imagens:
       if imagem.endswith(".jpg") or imagem.endswith(".png"):
           imagens_extraidas.append(imagem)