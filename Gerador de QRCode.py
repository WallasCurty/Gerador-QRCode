#Bibliotecas necessárias

#pip install pyqrcode
# pip install pypng

import pyqrcode 
import png 
from pyqrcode import QRCode

print("--------------- Gerador de QRCode ---------------------")

#Link desejado para o QRCode
QRString = input('Digite o link que deseja gerar o QRcode: ')

# Monta o QRCode 
url = pyqrcode.create(QRString)

#Salva o QRCode gerado no local que se deseja 
url.png(r'qr.png', scale=8)