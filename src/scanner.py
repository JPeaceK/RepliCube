import os
#import cv2
import numpy as np
from PIL import Image
from collections import Counter
from push import *
from move_ import *
from move import *
from rotate import *
from rotate_ import *

#images = ["Images/CubeU0.jpg", "Images/CubeF0.jpg", "Images/CubeD0.jpg", "Images/CubeB0.jpg", "Images/CubeR0.jpg", "Images/CubeL0.jpg"]
images = ['images\CuboU0.jpg', 'images\CuboU1.jpg', 'images\CuboU2.jpg', 'images\CuboU3.jpg','images\CuboU4.jpg','images\CuboU5.jpg']
comando = "raspistill -o "

def scannerMain():
    os.system(comando + images[0])
    pushMain()
    os.system(comando + images[1])
    pushMain()
    os.system(comando + images[2])
    pushMain()
    os.system(comando + images[3])
    pushMain()
    rotateMain()
    pushMain()
    os.system(comando + images[4])
    pushMain()
    pushMain()
    rotate_Main()
    rotate_Main()
    os.system(comando + images[5])
    pushMain()
    pushMain()
    pushMain()
    rotateMain()

def recortar_imagen(rutas_images):
    # Coordenadas de las esquinas (superior izquierda, inferior derecha)
    esquina_superior_izquierda = (1264, 1119)
    esquina_inferior_derecha = (2340, 2234)

    #imagen = Image.open(ruta_imagen)
    #imagen_recortada = imagen.crop((esquina_superior_izquierda[0], esquina_superior_izquierda[1],
    #                                esquina_inferior_derecha[0], esquina_inferior_derecha[1]))
   
    imagenes_recortadas = []

    for image in rutas_images:
        imagen = Image.open(image)
        imagen_recortada = imagen.crop((esquina_superior_izquierda[0], esquina_superior_izquierda[1],
                                    esquina_inferior_derecha[0], esquina_inferior_derecha[1]))
     
        imagenes_recortadas.append(imagen_recortada)
        
        # Guardar la imagen recortada
        images_recortadas_rutes = ['images\zoom\CuboU0.jpg', 'images\zoom\CuboU1.jpg', 'images\zoom\CuboU2.jpg', 'images\zoom\CuboU3.jpg','images\zoom\CuboU4.jpg','images\zoom\CuboU5.jpg']
        k = 0
        for im in imagenes_recortadas:
            im.save(images_recortadas_rutes[k])
            k = k + 1
    
    return images_recortadas_rutes



def obtener_color(pixel_hsv):
    hue = pixel_hsv[0]
    saturation = pixel_hsv[1]
    value = pixel_hsv[2]

    # Rangos con margen
    margen = 10

    if (0 <= hue < 8 + margen or 172 - margen <= hue <= 180) and saturation > 100:
        return "R"
    elif 8 - margen <= hue < 25 + margen and saturation > 100 and value > 50:
        return "Y"    
    elif 40 - margen <= hue < 75 + margen and saturation > 50:
        return "G"
    elif 100 - margen <= hue < 130 + margen and saturation > 100:
        return "B"
    elif 0 <= hue < 8 + margen and saturation <= 100 and value > 180:
        return "W"
    else:
        return "W"

# Obtener los píxeles vecinos para cada uno de los 9 píxeles proporcionados
def obtener_pixeles_vecinos(imagen_hsv, coordenadas):
    pixeles_vecinos = []
    for x, y in coordenadas:
        pixeles_interes = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                pixel = imagen_hsv[y + i, x + j]
                pixeles_interes.append(pixel)
        pixeles_vecinos.append(pixeles_interes)
    return pixeles_vecinos


def get_face_colors(image_path):
    
    coordenadas = [(248, 359), (476, 301), (696, 236), (319, 602), (556, 521), (790, 463), (385, 850), (639, 786), (876, 703)] 

    imagen = cv2.imread(image_path)
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    pixeles_vecinos = obtener_pixeles_vecinos(imagen_hsv, coordenadas) #Seleccionamos pixeles vecinos para reducir la possibilidad de error
   
    pixel_colors = []
    face_colors_aux = []

    for i, pixeles_interes in enumerate(pixeles_vecinos):
        for j, pixel_hsv in enumerate(pixeles_interes):
            color = obtener_color(pixel_hsv)

            if color == "R":
                if (
                    (160 <= pixel_hsv[0] <= 180) and
                    (pixel_hsv[1] >= 220) and
                    (pixel_hsv[2] >= 150)
                ):
                    color = "R"
                else:
                    color = "O"

            
            if color == "B":
                if (
                    80 <= pixel_hsv[1] <= 130
                ):
                    color = "W"
                else:
                    color = "B"

            pixel_colors.append(color)

        conteo = Counter(pixel_colors)
        pixel = conteo.most_common(1)[0][0] #Escogemos el color mas repetido de los pixeles vecinos
        pixel_colors = []
        face_colors_aux.append(pixel)

    face_colors = [face_colors_aux[2], face_colors_aux[5], face_colors_aux[8], face_colors_aux[1], face_colors_aux[4], face_colors_aux[7], face_colors_aux[0], face_colors_aux[3], face_colors_aux[6]]

    return face_colors

def setColors2(cube, images):
    i = 0
    j = 0
    imagenes_recortadas = recortar_imagen(images)
    for face, values in cube.faces.items():       
        face_colors = get_face_colors(imagenes_recortadas[i])
        i = i + 1
        for color in face_colors:
            cube.faces[face][j] = color
            j = j + 1
        j = 0
            
    

def setColors(cube):
    for face in cube.faces:
        
        for i in range(9):
            color = input(f"Enter the color for position {i+1} of face {face}: ")
            cube.faces[face][i] = color
            
    print(cube.faces['U'])
