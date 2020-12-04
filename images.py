from PIL import Image, ImageFilter

img = Image.open('./Imagens/Woodstock.png')

print('\nImprime o endereço na memória onde está a imagem:')
print(img)

print('\nImprime o formato da imagem:')
print(img.format)

print('\nImprime o tamanho da imagem:')
print(img.size)

print('\nImprime como é colorida a imagem:')
print(img.mode)

print('\nImprime dir a imagem:')
print(dir(img))

print('---> Altera formatação da imagem e converte para uma outra extensão e tipo. Gera um arquivo novo.')

print('\nImprime a imagem borrada. Tipo BLUR.')
img2 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img2.filter(ImageFilter.BLUR)
filtered_img.save("./Imagens/blur.png", 'png')

print('\nEstabilizador de imagem. Tipo SMOOTH.')
img3 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img3.filter(ImageFilter.SMOOTH)
filtered_img.save("./Imagens/smooth.png", 'png')

print('\nEnvelhece a imagem. Tipo SHARPEN.')
img4 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img4.filter(ImageFilter.SHARPEN)
filtered_img.save("./Imagens/sharpen.png", 'png')

print('\nConverte imagem para cinza. ')
img5 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img5.convert('L')
filtered_img.save("./Imagens/grey.png", 'png')

print('\nSomente mostra a imagem alterada. Não cria um novo arquivo. ')
img6 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img5.convert('L')
#filtered_img.show()

print('\nRotaciona a imagem em noventa graus.')
img7 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img7.convert('L')
crooked = filtered_img.rotate(90)
crooked.save("./Imagens/grey_90.png", 'png')

print('\nResize da imagem.')
img8 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img8.convert('L')
resize = filtered_img.resize((100,100))
resize.save("./Imagens/grey_resize.png", 'png')

print('\nCrop da imagem.')
img9 = Image.open('./Imagens/Woodstock_casinha.jpg')
filtered_img = img9.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("./Imagens/grey_crop.png", 'png')

print('\nRecalcula o tamanho da imagem para não ficar distorcida. Thumbnail.')
img10 = Image.open('./Imagens/Woodstock_casinha.jpg')
img10.thumbnail((100,50))
img10.save('./Imagens/thumbnail.jpg')

