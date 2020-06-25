'''Normando de Campos Amazonas Filho, 11561949
Image Processing, SCC0251_Turma01_1Sem_2020_ET
Assignment 1: intensity transformations
https://github.com/normandoamazonas/Assignment1'''



import numpy as np
import matplotlib.pyplot as plt
import imageio as imageio

'''Functions definitions'''

#Error from image reference to processed image
def rmse(im,ref):  
    erro = np.sqrt(np.sum(np.square(im.astype(float) - ref.astype(float))))
    return erro
    
#Inversion of intensity values 
def metodo1(input_img):
  im2=255-input_img
  return im2
  
#Contrast modulation
def metodo2(input_img):
  a=np.min(input_img)#a is the lowest image intensity value
  b=np.max(input_img) #b the highest image intensity value
  im2=(input_img-a)*(float(d-c)/float(b-a))+c #c and d are the parameters of the new lowest and highest values, respectively
  return im2
  
#Logarithmic Function 
def metodo3 (input_img):
   R = float(np.max (input_img)) #R is the highest image intensity value   
   im2= 255.0 * ((np.log2(1.0+input_img))/(np.log2(1.0+R)))
   return im2 
   
#Gamma adjustment
def metodo4 (input_img, W, milambda):
   im2= W*(input_img**milambda) #milambda is the gamma parameter 
   return im2

'''Parameters input'''   
filename = str(input()).rstrip()
method = int(input()) # 1 2 3 4
save = int(input()) #0 1

input_img = imageio.imread(filename)


if method == 1:
  im2=metodo1(input_img)

if method == 2:
  c = int(input())
  d = int(input())
  im2=metodo2(input_img)

if method == 3:
  im2= metodo3(input_img)

 
if method == 4:
  W = int(input())
  milambda = float(input())
  im2 = metodo4 (input_img, W, milambda)

  
if save == 1:
  im2 = im2.astype(np.uint8) #to avoid warnings
  imageio.imwrite("output_img.png",im2)

  
erro=rmse(im2,input_img)
print(round(erro,4))

