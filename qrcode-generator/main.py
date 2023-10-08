import qrcode


data = input('QRCODE content: ')
name = input('Name QRCODE: ')
img = qrcode.make(data)
img.save(f'C:/Users/Luann/Documents/{name}.png')
print('QRCODE Saved successfully!')
