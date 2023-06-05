#THIS IS THE MAIN CODE
from Solver import *
from scanManual import *
import copy
import time
from scanner import *
import cv2


class Cube:
    def __init__(self):
        self.faces = {
            'U': [None, None, None, None, None, None, None, None, None],
            'F': [None, None, None, None, None, None, None, None, None],
            'D': [None, None, None, None, None, None, None, None, None],
            'B': [None, None, None, None, None, None, None, None, None],
            'R': [None, None, None, None, None, None, None, None, None],
            'L': [None, None, None, None, None, None, None, None, None],           
        }

#Cubo con todas las caras resueltas
#Este cubo se utilizará para el algoritmo de resolución
solved = Cube()
solved.faces = {
    'U' : ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    'F' : ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    'D' : ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    'B' : ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    'R' : ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    'L' : ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
}

#Cubo con el que hacer pruebas
testCube = Cube()
testCube.faces = {
    'U' : ['B', 'B', 'B', 'B', 'B', 'B', 'R', 'R', 'R'],
    'F' : ['W', 'W', 'W', 'G', 'R', 'R', 'G', 'R', 'R'],
    'D' : ['O', 'G', 'G', 'O', 'G', 'G', 'O', 'G', 'G'],
    'B' : ['B', 'O', 'O', 'B', 'O', 'O', 'Y', 'Y', 'Y'],
    'R' : ['G', 'R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    'L' : ['O', 'O', 'B', 'W', 'W', 'W', 'W', 'W', 'W']
}

#Fución que dibuja todas las caras del cubo
def printCube(cube):
    cleanLine = "+-----------+"
    line = "+---+---+---+"
    whiteSpace = "              "

    # Imprime la cara U
    print(f"{whiteSpace}{cleanLine}")
    print(f"{whiteSpace}| {cube.faces['U'][0]} | {cube.faces['U'][1]} | {cube.faces['U'][2]} |")
    print(f"{whiteSpace}{line}")
    print(f"{whiteSpace}| {cube.faces['U'][3]} | {cube.faces['U'][4]} | {cube.faces['U'][5]} |")
    print(f"{whiteSpace}{line}")
    print(f"{whiteSpace}| {cube.faces['U'][6]} | {cube.faces['U'][7]} | {cube.faces['U'][8]} |")
    print(f"{whiteSpace}{cleanLine}")

    #Imprime las caras L, F, R
    print(f"{cleanLine} {cleanLine} {cleanLine}")
    print(f"| {cube.faces['L'][0]} | {cube.faces['L'][1]} | {cube.faces['L'][2]} | | {cube.faces['F'][0]} | {cube.faces['F'][1]} | {cube.faces['F'][2]} | | {cube.faces['R'][0]} | {cube.faces['R'][1]} | {cube.faces['R'][2]} | ")
    print(f"{line} {line} {line}")
    print(f"| {cube.faces['L'][3]} | {cube.faces['L'][4]} | {cube.faces['L'][5]} | | {cube.faces['F'][3]} | {cube.faces['F'][4]} | {cube.faces['F'][5]} | | {cube.faces['R'][3]} | {cube.faces['R'][4]} | {cube.faces['R'][5]} | ")
    print(f"{line} {line} {line}")
    print(f"| {cube.faces['L'][6]} | {cube.faces['L'][7]} | {cube.faces['L'][8]} | | {cube.faces['F'][6]} | {cube.faces['F'][7]} | {cube.faces['F'][8]} | | {cube.faces['R'][6]} | {cube.faces['R'][7]} | {cube.faces['R'][8]} | ")
    print(f"{cleanLine} {cleanLine} {cleanLine}")
    
    #Imprime las caras D, B
    for i in ['D', 'B']:
        print(f"{whiteSpace}{cleanLine}")
        print(f"{whiteSpace}| {cube.faces[i][0]} | {cube.faces[i][1]} | {cube.faces[i][2]} |")
        print(f"{whiteSpace}{line}")
        print(f"{whiteSpace}| {cube.faces[i][3]} | {cube.faces[i][4]} | {cube.faces[i][5]} |")
        print(f"{whiteSpace}{line}")
        print(f"{whiteSpace}| {cube.faces[i][6]} | {cube.faces[i][7]} | {cube.faces[i][8]} |")
        print(f"{whiteSpace}{cleanLine}")


print("Select RepliCube mode:")
print("- 1: Solve cube")
print("- 2: Reply cube")

exit = False
while(not exit):
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        print("Select scan mode:")
        print("- 1: Auto")
        print("- 2: Manual")
        exit2 = False
        while(not exit2):
            user_input = input("Enter your choice: ")
            if user_input == "1":
                exit2 = True
                cube = Cube()
                scannerMain()
                images = ['CuboU0.jpg', 'CuboU1.jpg', 'CuboU2.jpg', 'CuboU3.jpg','CuboU4.jpg','CuboU5.jpg']
                setColors2(cube, images)

                print("Start solving in...")
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                solve(cube, solved)
                
            elif user_input == "2":
                exit2 = True
                cube = Cube()
                cube = copy.deepcopy(solved)
                setColorsManual(cube)
                print("Start solving in...")
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                solve(cube, solved)
                
            else:
                print("Invalid choice!")
        exit = True
        
        
        
    elif user_input == "2":
        print("Select scan mode:")
        print("- 1: Auto")
        print("- 2: Manual")
        exit2 = False
        while(not exit2):
            user_input = input("Enter your choice: ")
            if user_input == "1":
                exit2 = True
                cube = Cube()
                scannerMain()
                images = ['CuboU0.jpg', 'CuboU1.jpg', 'CuboU2.jpg', 'CuboU3.jpg','CuboU4.jpg','CuboU5.jpg']
                setColors2(cube, images)
                
                print("Put the second cube inside the box")
                time.sleep(3)
                cubeToReply = Cube()
                scannerMain()
                setColors2(cubeToReply, images)
                
                print("Start replicating in...")
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                solve(cube, cubeToReply)
            elif user_input == "2":
                cube = Cube()
                setColorsManual(cube)
                
                cubeToReply = Cube()
                setColorsManual(cubeToReply)
                
                print("Start replicating in...")
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                solve(cube, solved)
            else:
                print("Invalid choice!")
        exit = True
    else:
        print("Invalid choice!")
    
