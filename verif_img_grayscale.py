import PIL.Image
import numpy
import torch

#print ('Pillow Version: ', PIL.__version__)

fp = "./Sans titre.png"
size = 28,28
rgb_weights = [.2989, .5870, .1140]
#print("Donnez le lien du fichier image :")
image = Image.open(fp)
display(image)
print(image)
img2 = image.resize(size)
img2.save("2.png")
display(img2)
print(img2)
image = img2
#print(image.format)
#print(image.size)
#print(image.mode)
rgb_matrix = numpy.asarray(image)
tensor = numpy.dot(rgb_matrix,rgb_weights)
#display(tensor)
new_im = Image.fromarray(tensor)
new_im = new_im.convert("L")
display(new_im)
