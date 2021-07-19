import qrcode
print("Processi....")


link = input("Type your text here: ")


img = qrcode.make(f'{link}')
img.save("Qrcode.png")

print(f'Complate. \n Qrcode is saved as: Qrcode.png')