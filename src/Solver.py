import copy
from push import *
from move import *
from move_ import *
from rotate import *
from rotate_ import *

#Scanner manual
def setColors(cube):
    for face in cube.faces:
        for i in range(9):
            color = input(f"Enter the color for position {i+1} of face {face}: ")
            cube.faces[face][i] = color

#Mostrar estado del cubo
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
        
        
def push(cube):
    pushMain()
    aux = cube.faces['U']
    cube.faces['U'] = cube.faces['F']
    cube.faces['F'] = cube.faces['D']
    cube.faces['D'] = cube.faces['B']
    cube.faces['B'] = aux
    
    aux = cube.faces['L'][0]
    cube.faces['L'][0] = cube.faces['L'][2]
    cube.faces['L'][2] = cube.faces['L'][8]
    cube.faces['L'][8] = cube.faces['L'][6]
    cube.faces['L'][6] = aux
    aux = cube.faces['L'][1]
    cube.faces['L'][1] = cube.faces['L'][5]
    cube.faces['L'][5] = cube.faces['L'][7]
    cube.faces['L'][7] = cube.faces['L'][3]
    cube.faces['L'][3] = aux
    
    aux = cube.faces['R'][0]
    cube.faces['R'][0] = cube.faces['R'][6]
    cube.faces['R'][6] = cube.faces['R'][8]
    cube.faces['R'][8] = cube.faces['R'][2]
    cube.faces['R'][2] = aux
    aux = cube.faces['R'][1]
    cube.faces['R'][1] = cube.faces['R'][3]
    cube.faces['R'][3] = cube.faces['R'][7]
    cube.faces['R'][7] = cube.faces['R'][5]
    cube.faces['R'][5] = aux
    
    
def rotate(cube):
    rotateMain()
    aux = cube.faces['F']
    cube.faces['F'] = cube.faces['R']
    cube.faces['R'] = cube.faces['B']
    cube.faces['B'] = cube.faces['L']
    cube.faces['L'] = aux
    
    aux = cube.faces['U'][0]
    cube.faces['U'][0] = cube.faces['U'][6]
    cube.faces['U'][6] = cube.faces['U'][8]
    cube.faces['U'][8] = cube.faces['U'][2]
    cube.faces['U'][2] = aux
    aux = cube.faces['U'][1]
    cube.faces['U'][1] = cube.faces['U'][3]
    cube.faces['U'][3] = cube.faces['U'][7]
    cube.faces['U'][7] = cube.faces['U'][5]
    cube.faces['U'][5] = aux
    
    aux = cube.faces['D'][0]
    cube.faces['D'][0] = cube.faces['D'][2]
    cube.faces['D'][2] = cube.faces['D'][8]
    cube.faces['D'][8] = cube.faces['D'][6]
    cube.faces['D'][6] = aux
    aux = cube.faces['D'][1]
    cube.faces['D'][1] = cube.faces['D'][5]
    cube.faces['D'][5] = cube.faces['D'][7]
    cube.faces['D'][7] = cube.faces['D'][3]
    cube.faces['D'][3] = aux
    
    aux = cube.faces['R'][0]
    cube.faces['R'][0] = cube.faces['R'][8]
    cube.faces['R'][8] = aux
    aux = cube.faces['R'][2]
    cube.faces['R'][2] = cube.faces['R'][6]
    cube.faces['R'][6] = aux
    aux = cube.faces['R'][1]
    cube.faces['R'][1] = cube.faces['R'][7]
    cube.faces['R'][7] = aux
    aux = cube.faces['R'][3]
    cube.faces['R'][3] = cube.faces['R'][5]
    cube.faces['R'][5] = aux
    
    aux = cube.faces['B'][0]
    cube.faces['B'][0] = cube.faces['B'][8]
    cube.faces['B'][8] = aux
    aux = cube.faces['B'][2]
    cube.faces['B'][2] = cube.faces['B'][6]
    cube.faces['B'][6] = aux
    aux = cube.faces['B'][1]
    cube.faces['B'][1] = cube.faces['B'][7]
    cube.faces['B'][7] = aux
    aux = cube.faces['B'][3]
    cube.faces['B'][3] = cube.faces['B'][5]
    cube.faces['B'][5] = aux

def rotate_(cube):
    rotate_Main()
    aux = cube.faces['F']
    cube.faces['F'] = cube.faces['L']
    cube.faces['L'] = cube.faces['B']
    cube.faces['B'] = cube.faces['R']
    cube.faces['R'] = aux
    
    aux = cube.faces['U'][0]
    cube.faces['U'][0] = cube.faces['U'][2]
    cube.faces['U'][2] = cube.faces['U'][8]
    cube.faces['U'][8] = cube.faces['U'][6]
    cube.faces['U'][6] = aux
    aux = cube.faces['U'][1]
    cube.faces['U'][1] = cube.faces['U'][5]
    cube.faces['U'][5] = cube.faces['U'][7]
    cube.faces['U'][7] = cube.faces['U'][3]
    cube.faces['U'][3] = aux
    
    aux = cube.faces['D'][0]
    cube.faces['D'][0] = cube.faces['D'][6]
    cube.faces['D'][6] = cube.faces['D'][8]
    cube.faces['D'][8] = cube.faces['D'][2]
    cube.faces['D'][2] = aux
    aux = cube.faces['D'][1]
    cube.faces['D'][1] = cube.faces['D'][3]
    cube.faces['D'][3] = cube.faces['D'][7]
    cube.faces['D'][7] = cube.faces['D'][5]
    cube.faces['D'][5] = aux
    
    aux = cube.faces['L'][0]
    cube.faces['L'][0] = cube.faces['L'][8]
    cube.faces['L'][8] = aux
    aux = cube.faces['L'][2]
    cube.faces['L'][2] = cube.faces['L'][6]
    cube.faces['L'][6] = aux
    aux = cube.faces['L'][1]
    cube.faces['L'][1] = cube.faces['L'][7]
    cube.faces['L'][7] = aux
    aux = cube.faces['L'][3]
    cube.faces['L'][3] = cube.faces['L'][5]
    cube.faces['L'][5] = aux
    
    aux = cube.faces['B'][0]
    cube.faces['B'][0] = cube.faces['B'][8]
    cube.faces['B'][8] = aux
    aux = cube.faces['B'][2]
    cube.faces['B'][2] = cube.faces['B'][6]
    cube.faces['B'][6] = aux
    aux = cube.faces['B'][1]
    cube.faces['B'][1] = cube.faces['B'][7]
    cube.faces['B'][7] = aux
    aux = cube.faces['B'][3]
    cube.faces['B'][3] = cube.faces['B'][5]
    cube.faces['B'][5] = aux
    

def move(cube):
    moveMain()
    aux = cube.faces['F'][6]
    cube.faces['F'][6] = cube.faces['R'][6]
    cube.faces['R'][6] = cube.faces['B'][2]
    cube.faces['B'][2] = cube.faces['L'][6]
    cube.faces['L'][6] = aux
    
    aux = cube.faces['F'][7]
    cube.faces['F'][7] = cube.faces['R'][7]
    cube.faces['R'][7] = cube.faces['B'][1]
    cube.faces['B'][1] = cube.faces['L'][7]
    cube.faces['L'][7] = aux
    
    aux = cube.faces['F'][8]
    cube.faces['F'][8] = cube.faces['R'][8]
    cube.faces['R'][8] = cube.faces['B'][0]
    cube.faces['B'][0] = cube.faces['L'][8]
    cube.faces['L'][8] = aux
    
    aux = cube.faces['D'][0]
    cube.faces['D'][0] = cube.faces['D'][2]
    cube.faces['D'][2] = cube.faces['D'][8]
    cube.faces['D'][8] = cube.faces['D'][6]
    cube.faces['D'][6] = aux
    
    aux = cube.faces['D'][1]
    cube.faces['D'][1] = cube.faces['D'][5]
    cube.faces['D'][5] = cube.faces['D'][7]
    cube.faces['D'][7] =cube.faces['D'][3]
    cube.faces['D'][3] = aux


def move_(cube):
    move_Main()
    aux = cube.faces['F'][6]
    cube.faces['F'][6] = cube.faces['L'][6]
    cube.faces['L'][6] = cube.faces['B'][2]
    cube.faces['B'][2] = cube.faces['R'][6]
    cube.faces['R'][6] = aux
    
    aux = cube.faces['F'][7]
    cube.faces['F'][7] = cube.faces['L'][7]
    cube.faces['L'][7] = cube.faces['B'][1]
    cube.faces['B'][1] = cube.faces['R'][7]
    cube.faces['R'][7] = aux
    
    aux = cube.faces['F'][8]
    cube.faces['F'][8] = cube.faces['L'][8]
    cube.faces['L'][8] = cube.faces['B'][0]
    cube.faces['B'][0] = cube.faces['R'][8]
    cube.faces['R'][8] = aux
    
    aux = cube.faces['D'][0]
    cube.faces['D'][0] = cube.faces['D'][6]
    cube.faces['D'][6] = cube.faces['D'][8]
    cube.faces['D'][8] = cube.faces['D'][2]
    cube.faces['D'][2] = aux
    
    aux = cube.faces['D'][1]
    cube.faces['D'][1] = cube.faces['D'][3]
    cube.faces['D'][3] = cube.faces['D'][7]
    cube.faces['D'][7] = cube.faces['D'][5]
    cube.faces['D'][5] = aux
    
def R(cube):
    print("R")
    rotate_(cube)
    push(cube)
    move_(cube)
    push(cube)
    push(cube)
    push(cube)
    rotate(cube)
    
def R_(cube):
    print("R_")
    rotate_(cube)
    push(cube)
    move(cube)
    push(cube)
    push(cube)
    push(cube)
    rotate(cube)
    
def L(cube):
    print("L")
    rotate(cube)
    push(cube)
    move_(cube)
    push(cube)
    push(cube)
    push(cube)
    rotate_(cube)
    
def L_(cube):
    print("L_")
    rotate(cube)
    push(cube)
    move(cube)
    push(cube)
    push(cube)
    push(cube)
    rotate_(cube)
    
def U(cube):
    print("U")
    push(cube)
    push(cube)
    move_(cube)
    push(cube)
    push(cube)

def U_(cube):
    print("U_")
    push(cube)
    push(cube)
    move(cube)
    push(cube)
    push(cube)
    
def F(cube):
    print("F")
    push(cube)
    push(cube)
    push(cube)
    move_(cube)
    push(cube)
    
def F_(cube):
    print("F_")
    push(cube)
    push(cube)
    push(cube)
    move(cube)
    push(cube)
    
def D(cube):
    print("D")
    move_(cube)

def D_(cube):
    print("D_")
    move(cube)
    
def B(cube):
    print("B")
    push(cube)
    move_(cube)
    push(cube)
    push(cube)
    push(cube)
    
def B_(cube):
    print("B_")
    push(cube)
    move(cube)
    push(cube)
    push(cube)
    push(cube)


def F2L(cube, aux1, aux2, aux3, aux4, aux5):
    if((cube.faces['F'][3] == aux3 or cube.faces['F'][3] == aux4) and (cube.faces['L'][5] == aux3 or cube.faces['L'][5] == aux4)):
        L_(cube)
        U_(cube)
        L(cube)
    if((cube.faces['L'][3] == aux3 and cube.faces['B'][3] == aux4) or (cube.faces['L'][3] == aux4 and cube.faces['B'][3] == aux3)):
        B_(cube)
        U(cube)
        U(cube)
        B(cube)
    if((cube.faces['R'][5] == aux3 and cube.faces['B'][5] == aux4) or ((cube.faces['R'][5] == aux4 and cube.faces['B'][5] == aux3))):
        B(cube)
        U(cube)
        U(cube)
        B_(cube)
    if((cube.faces['F'][6] == aux1 or cube.faces['F'][6] == aux2 or cube.faces['F'][6] == aux5) and (cube.faces['L'][8] == aux1 or cube.faces['L'][8] == aux2 or cube.faces['L'][8] == aux5) and (cube.faces['D'][0] == aux1 or cube.faces['D'][0] == aux2 or cube.faces['D'][0] == aux5)):
        L_(cube)
        U_(cube)
        L(cube)
    if((cube.faces['L'][6] == aux1 or cube.faces['L'][6] == aux2 or cube.faces['L'][6] == aux5) and (cube.faces['B'][0] == aux1 or cube.faces['B'][0] == aux2 or cube.faces['B'][0] == aux5) and (cube.faces['D'][6] == aux1 or cube.faces['D'][6] == aux2 or cube.faces['D'][6] == aux5)):
        B_(cube)
        U_(cube)
        B(cube)
    if((cube.faces['R'][8] == aux1 or cube.faces['R'][8] == aux2 or cube.faces['R'][8] == aux5) and (cube.faces['D'][8] == aux1 or cube.faces['D'][8] == aux2 or cube.faces['D'][8] == aux5) and (cube.faces['B'][2] == aux1 or cube.faces['B'][2] == aux2 or cube.faces['B'][2] == aux5)):
        R_(cube)
        U(cube)
        R(cube)
        U(cube)    
    
    if(cube.faces['F'][8] == aux1 and cube.faces['R'][6] == aux2):
        if(cube.faces['F'][1] == aux3 and cube.faces['U'][7] == aux4):
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
            U_(cube)
            F_(cube)
            U(cube)
            F(cube)
        elif(cube.faces['U'][5] == aux3 and cube.faces['R'][1] == aux4):
            U_(cube)
            F_(cube)
            U(cube)
            F(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux4 and cube.faces['R'][3] == aux3):
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
    elif(cube.faces['F'][1] == aux3 and cube.faces['U'][7] == aux4):
        if(cube.faces['F'][2] == aux1 and cube.faces['U'][8] == aux2 and cube.faces['R'][0] == aux5):
            U_(cube)
            F_(cube)
            U(cube)
            F(cube)
        elif(cube.faces['F'][2] == aux5 and cube.faces['U'][8] == aux1 and cube.faces['R'][0] == aux2):
            D(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
            U_(cube)
            R(cube)
        elif(cube.faces['F'][2] == aux2 and cube.faces['U'][8] == aux5 and cube.faces['R'][0] == aux1):
            F_(cube)
            U(cube)
            U(cube)
            F(cube)
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
        elif(cube.faces['F'][8] == aux2 and cube.faces['R'][6] and cube.faces['D'][2] == aux1):
            F_(cube)
            U(cube)
            F(cube)
            U_(cube)
            F_(cube)
            U(cube)
            F(cube)
    elif(cube.faces['F'][2] == aux5 and cube.faces['U'][8] == aux1 and cube.faces['R'][0] == aux2):
        if(cube.faces['R'][1] == aux4 and cube.faces['U'][5] == aux3):
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['U'][3] == aux4 and cube.faces['L'][1] == aux3):
            F_(cube)
            U_(cube)
            F(cube)
        elif(cube.faces['U'][5] == aux4 and cube.faces['R'][1] == aux3):
            U_(cube)
            R_(cube)
            U(cube)
            U(cube)
            R(cube)
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
        elif(cube.faces['U'][7] == aux3 and cube.faces['F'][1] == aux4):
            F_(cube)
            U(cube)
            F(cube)
            U(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4):
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U(cube)
            U(cube)
            R(cube)
        elif(cube.faces['U'][1] == aux4 and cube.faces['B'][7] == aux3):
            U_(cube)
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
        elif(cube.faces['U'][3] == aux3 and cube.faces['L'][1] == aux4):
            U_(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux3 and cube.faces['R'][3] == aux4):
            U_(cube)
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux4 and cube.faces['R'][3] == aux3):
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
            D(cube)
            R_(cube)
            U_(cube)
            R(cube)
    elif(cube.faces['F'][2] == aux1 and cube.faces['R'][0] == aux5 and cube.faces['U'][8] == aux2):
        if(cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4):
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['F'][1] == aux4 and cube.faces['L'][7] == aux3):
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            U(cube)
        elif(cube.faces['U'][5] == aux4 and cube.faces['R'][1] == aux3):
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
        elif(cube.faces['R'][1] == aux4 and cube.faces['U'][5] == aux3):
            U_(cube)
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['U'][3] == aux4 and cube.faces['L'][1] == aux3):
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
            U(cube)
            U(cube)
            F_(cube)
            U(cube)
            F(cube)
        elif(cube.faces['U'][3] == aux3 and cube.faces['L'][1] == aux4):
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['U'][1] == aux4 and cube.faces['B'][7] == aux3):
            U(cube)
            F_(cube)
            U(cube)
            U(cube)
            F(cube)
            U(cube)
            F_(cube)
            U(cube)
            U(cube)
            F(cube)
        elif(cube.faces['F'][5] == aux3 and cube.faces['R'][3] == aux4):
            U_(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux4 and cube.faces['R'][3] == aux3):
            D(cube)
            R_(cube)
            U_(cube)
            R(cube)
            D_(cube)
            R(cube)
            U(cube)
            R_(cube)
    elif(cube.faces['F'][2] == aux2 and cube.faces['U'][8] == aux5 and cube.faces['R'][0] == aux1):
        if(cube.faces['F'][1] == aux4 and cube.faces['U'][7] == aux3):
            R(cube)
            U(cube)
            R_(cube)
            U(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['U'][5] == aux4 and cube.faces['R'][1] == aux3):
            R(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            F_(cube)
            U(cube)
            U(cube)
            F(cube)
        elif(cube.faces['U'][5] == aux3 and cube.faces['R'][1] == aux4):
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['U'][3] == aux4 and cube.faces['L'][1] == aux3):
            U_(cube)
            F_(cube)
            U(cube)
            U(cube)
            F(cube)
            U_(cube)
            F_(cube)
            U(cube)
            F(cube)
        elif(cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4):
            U(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['U'][3] == aux3 and cube.faces['L'][1] == aux4):
            U(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['U'][1] == aux4 and cube.faces['B'][7] == aux3):
            U(cube)
            U(cube)
            F_(cube)
            U_(cube)
            F(cube)
            U_(cube)
            F_(cube)
            U(cube)
            F(cube)
        elif(cube.faces['F'][5] == aux3 and cube.faces['R'][3] == aux4):
            R(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux4 and cube.faces['R'][3] == aux3):
            R(cube)
            U_(cube)
            R_(cube)
            F_(cube)
            U(cube)
            U(cube)
            F(cube)
    elif(cube.faces['F'][8] == aux5 and cube.faces['R'][6] == aux1 and cube.faces['D'][2] == aux2):
        if(cube.faces['U'][5] == aux3 and cube.faces['R'][1] == aux4):
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['U'][5] == aux4 and cube.faces['R'][1] == aux3):
            U_(cube)
            R(cube)
            U_(cube)
            R_(cube)
            F_(cube)
            U_(cube)
            F(cube)
        elif(cube.faces['F'][5] == aux3 and cube.faces['R'][3] == aux4):
            R(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux4 and cube.faces['R'][3] == aux3):
            F_(cube)
            U(cube)
            F(cube)
            U(cube)
            U(cube)
            R(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
    elif(cube.faces['F'][8] == aux2 and cube.faces['R'][6] == aux5 and cube.faces['D'][2] == aux1):
        if(cube.faces['U'][7] == aux3 and cube.faces['F'][1] == aux4):
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            U(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux3 and cube.faces['R'][3] == aux4):
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            R(cube)
            U(cube)
            U(cube)
            R_(cube)
            U(cube)
            R(cube)
            U_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux4 and cube.faces['R'][3] == aux3):
            R(cube)
            U_(cube)
            R_(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            F_(cube)
            U(cube)
            F(cube)
    else:
        print("sskjnfkdnf")

def orientar(cube):
    B_(cube)
    R_(cube)
    U_(cube)
    R(cube)
    U(cube)
    B(cube)

def permutar(cube):
    R_(cube)
    U_(cube)
    R(cube)
    U_(cube)
    R_(cube)
    U_(cube)
    U_(cube)
    R(cube)
    U_(cube)

def permutarEsquinas(cube):
    R(cube)
    U_(cube)
    L_(cube)
    U(cube)
    R_(cube)
    U_(cube)
    L(cube)
    U(cube)

def sexyMove(cube):
    R_(cube)
    D_(cube)
    R(cube)
    D(cube)

def solve(cube, reach):
    aux = reach.faces['U'][4]
    if (cube.faces['U'][4] != aux):
        print("Setting " + str(aux) + " face on UP")
        if (cube.faces['F'][4] == aux):
            push(cube)
        elif (cube.faces['R'][4] == aux):
            rotate(cube)
            push(cube)
        elif (cube.faces['L'][4] == aux):
            rotate_(cube)
            push(cube)
        elif (cube.faces['B'][4] == aux):
            push(cube)
            push(cube)
            push(cube)
        else:
            push(cube)
            push(cube)
    else:
        print(str(aux) + " face is already on UP")
                    
    aux = reach.faces['F'][4]
    if (cube.faces['F'][4] != aux):
        print("Setting " + str(aux) + " face on FRONT")
        if (cube.faces['R'][4] == aux):
            rotate(cube)
        elif (cube.faces['L'][4] == aux):
            rotate_(cube)
        else:
            rotate(cube)
            rotate(cube)
    else:
        print(str(aux) + " face is already on FRONT")
                    
    #En este punto tenemos todos los centros iguales al cubo objetivo
    
    #Ahora haremos la cruz en la fila de abajo
    aux1 = reach.faces['F'][7]
    aux2 = reach.faces['D'][1]
    
    if (cube.faces['D'][1] != aux2 or cube.faces['F'][7] != aux1):
        if(cube.faces['D'][1] == aux1 and cube.faces['F'][7] == aux2):
            F(cube)
            L_(cube)
            U_(cube)
            F(cube)
            F(cube)
        elif(cube.faces['R'][7] == aux1 and cube.faces['D'][5] == aux2):
            D_(cube)
        elif(cube.faces['R'][7] == aux2 and cube.faces['D'][5] == aux1):
            R(cube)
            F(cube)
        elif(cube.faces['L'][7] == aux1 and cube.faces['D'][3] == aux2):
            D(cube)
        elif(cube.faces['L'][7] == aux2 and cube.faces['D'][3] == aux1):
            L_(cube)
            F_(cube)
        elif(cube.faces['B'][1] == aux1 and cube.faces['D'][7] == aux2):
            D(cube)
            D(cube)
        elif(cube.faces['B'][1] == aux2 and cube.faces['D'][7] == aux1):
            B(cube)
            B(cube)
            U(cube)
            R_(cube)
            F(cube)
        elif(cube.faces['F'][5] == aux1 and cube.faces['R'][3] == aux2):
            F(cube)
        elif(cube.faces['F'][5] == aux2 and cube.faces['R'][3] == aux1):
            R(cube)
            U(cube)
            F(cube)
            F(cube)
        elif(cube.faces['F'][3] == aux1 and cube.faces['L'][5] == aux2):
            F_(cube)
        elif(cube.faces['F'][3] == aux2 and cube.faces['L'][5] == aux1):
            L(cube)
            D(cube)
        elif(cube.faces['R'][5] == aux1 and cube.faces['B'][5] == aux2):
            B(cube)
            U(cube)
            R_(cube)
            F(cube)
        elif(cube.faces['R'][5] == aux2 and cube.faces['B'][5] == aux1):
            B_(cube)
            D(cube)
            D(cube)
        elif(cube.faces['L'][3] == aux1 and cube.faces['B'][3] == aux2):
            L_(cube)
            D(cube)
        elif(cube.faces['L'][3] == aux2 and cube.faces['B'][3] == aux1):
            B_(cube)
            U(cube)
            U(cube)
            F(cube)
            F(cube)
        elif(cube.faces['F'][1] == aux1 and cube.faces['U'][7] == aux2):
            F(cube)
            F(cube)
        elif(cube.faces['F'][1] == aux2 and cube.faces['U'][7] == aux1):
            U_(cube)
            R_(cube)
            F(cube)
        elif(cube.faces['R'][1] == aux1 and cube.faces['U'][5] == aux2):
            U(cube)
            F(cube)
            F(cube)
        elif(cube.faces['R'][1] == aux2 and cube.faces['U'][5] == aux1):
            R_(cube)
            F(cube)
        elif(cube.faces['L'][1] == aux1 and cube.faces['U'][3] == aux2):
            U_(cube)
            F(cube)
            F(cube)
        elif(cube.faces['L'][1] == aux2 and cube.faces['U'][3] == aux1):
            L(cube)
            F_(cube)
        elif(cube.faces['B'][7] == aux1 and cube.faces['U'][1] == aux2):
            U(cube)
            U(cube)
            F(cube)
            F(cube)
        elif(cube.faces['B'][7] == aux2 and cube.faces['U'][1] == aux1):
            U(cube)
            R_(cube)
            F(cube)
    
    aux1 = reach.faces['R'][7]
    aux2 = reach.faces['D'][5]
    
    if (cube.faces['R'][7] != aux1 or cube.faces['D'][5] != aux2):
        if(cube.faces['R'][7] == aux2 and cube.faces['D'][5] == aux1):
            R_(cube)
            B(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['L'][7] == aux1 and cube.faces['D'][3] == aux2):
            F(cube)
            D(cube)
            D(cube)
            F_(cube)
        elif(cube.faces['L'][7] == aux2 and cube.faces['D'][3] == aux1):
            L(cube)
            B_(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['B'][1] == aux1 and cube.faces['D'][7] == aux2):
            F(cube)
            D_(cube)
            F_(cube)
        elif(cube.faces['B'][1] == aux2 and cube.faces['D'][7] == aux1):
            B(cube)
            R(cube)
        elif(cube.faces['F'][5] == aux1 and cube.faces['R'][3] == aux2):
            R(cube)
            U_(cube)
            B_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux2 and cube.faces['R'][3] == aux1):
            R_(cube)
        elif(cube.faces['F'][3] == aux1 and cube.faces['L'][5] == aux2):
            F(cube)
            U_(cube)
            F_(cube)
            R(cube)
            R(cube)
        elif(cube.faces['F'][3] == aux2 and cube.faces['L'][5] == aux1):
            L_(cube)
            U(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['L'][3] == aux1 and cube.faces['B'][3] == aux2):
            L(cube)
            U(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['L'][3] == aux2 and cube.faces['B'][3] == aux1):
            B_(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['R'][5] == aux1 and cube.faces['B'][5] == aux2):
            R(cube)
        elif(cube.faces['R'][5] == aux2 and cube.faces['B'][5] == aux1):
            B(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['U'][7] == aux2 and cube.faces['F'][1] == aux1):
            U_(cube)
            R(cube)
            R(cube)
        elif(cube.faces['U'][5] == aux2 and cube.faces['R'][1] == aux1):
            R(cube)
            R(cube)
        elif(cube.faces['U'][3] == aux2 and cube.faces['L'][1] == aux1):
            U(cube)
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['U'][1] == aux2 and cube.faces['B'][7] == aux1):
            U(cube)
            R(cube)
            R(cube)
        elif(cube.faces['U'][7] == aux1 and cube.faces['F'][1] == aux2):
            F(cube)
            R_(cube)
            F_(cube)
        elif(cube.faces['U'][3] == aux1 and cube.faces['L'][1] == aux2):
            U_(cube)
            F(cube)
            R_(cube)
            F_(cube)
        elif(cube.faces['U'][5] == aux1 and cube.faces['R'][1] == aux2):
            U(cube)
            F(cube)
            R_(cube)
            F_(cube)
        elif(cube.faces['U'][1] == aux1 and cube.faces['B'][7] == aux2):
            U(cube)
            U(cube)
            F(cube)
            R_(cube)
            F_(cube)
    
    aux1 = reach.faces['L'][7]
    aux2 = reach.faces['D'][3]
    
    if(cube.faces['L'][7] != aux1 or cube.faces['D'][3] != aux2):
        if(cube.faces['L'][7] == aux2 and cube.faces['D'][3] == aux1):
            L_(cube)
            F(cube)
            U(cube)
            F_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['B'][1] == aux1 and cube.faces['D'][7]):
            B_(cube)
            B_(cube)
            U_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['B'][1] == aux2 and cube.faces['D'][7] == aux1):
            B_(cube)
            L_(cube)
        elif(cube.faces['F'][3] == aux1 and cube.faces['L'][5] == aux2):
            F(cube)
            U(cube)
            F_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['F'][3] == aux2 and cube.faces['L'][5] == aux1):
            L(cube)
        elif(cube.faces['F'][5] == aux1 and cube.faces['R'][3] == aux2):
            F_(cube)
            U(cube)
            F(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['F'][5] == aux2 and cube.faces['R'][3] == aux1):
            R(cube)
            U_(cube)
            U_(cube)
            R_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['L'][3] == aux1 and cube.faces['B'][3] == aux2):
            L_(cube)
        elif(cube.faces['L'][3] == aux2 and cube.faces['B'][3] == aux1):
            B_(cube)
            U_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['R'][5] == aux1 and cube.faces['B'][5] == aux2):
            B_(cube)
            B_(cube)
            L_(cube)
        elif(cube.faces['R'][5] == aux2 and cube.faces['B'][5] == aux1):
            R_(cube)
            U_(cube)
            R(cube)
            U_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['U'][1] == aux2 and cube.faces['B'][7] == aux1):
            U_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['U'][3] == aux2 and cube.faces['L'][1] == aux1):
            L_(cube)
            L_(cube)
        elif(cube.faces['U'][7] == aux2 and cube.faces['F'][1] == aux1):
            U_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['U'][5] == aux2 and cube.faces['R'][1] == aux1):
            U_(cube)
            U_(cube)
            L_(cube)
            L_(cube)
        elif(cube.faces['U'][1] == aux1 and cube.faces['B'][7] == aux2):
            B(cube)
            L_(cube)
        elif(cube.faces['U'][3] == aux1 and cube.faces['L'][1] == aux2):
            U(cube)
            B(cube)
            L_(cube)
        elif(cube.faces['U'][7] == aux1 and cube.faces['F'][1] == aux2):
            U_(cube)
            U_(cube)
            B(cube)
            L_(cube)
        elif(cube.faces['U'][5] == aux1 and cube.faces['R'][1] == aux2):
            U_(cube)
            B(cube)
            L_(cube)
    
    aux1 = reach.faces['B'][1]
    aux2 = reach.faces['D'][7]
    
    
    
    if(cube.faces['B'][1] != aux1 or cube.faces['D'][7] != aux2):
        if(cube.faces['B'][1] == aux2 and cube.faces['D'][7] == aux1):
            B_(cube)
            R_(cube)
            U_(cube)
            B(cube)
            B(cube)
            R(cube)
        elif(cube.faces['F'][3] == aux1 and cube.faces['L'][5] == aux2):
            L_(cube)
            U(cube)
            L(cube)
            U_(cube)
            L_(cube)
            B(cube)
            L(cube)
        elif(cube.faces['F'][3] == aux2 and cube.faces['L'][5] == aux1):
            L_(cube)
            U(cube)
            L(cube)
            B(cube)
            B(cube)
        elif(cube.faces['F'][5] == aux1 and cube.faces['R'][3] == aux2):
            R(cube)
            U(cube)
            R_(cube)
            U_(cube)
            R(cube)
            B_(cube)
            R_(cube)
        elif(cube.faces['F'][5] == aux2 and cube.faces['R'][3] == aux1):
            R(cube)
            U_(cube)
            R_(cube)
            B(cube)
            B(cube)
        elif(cube.faces['L'][3] == aux1 and cube.faces['B'][3] == aux2):
            L(cube)
            U(cube)
            L_(cube)
            B(cube)
            B(cube)
        elif(cube.faces['L'][3] == aux2 and cube.faces['B'][3] == aux1):
            B(cube)
        elif(cube.faces['R'][5] == aux1 and cube.faces['B'][5] == aux2):
            B(cube)
            U(cube)
            R(cube)
            B_(cube)
            R_(cube)
        elif(cube.faces['R'][5] == aux2 and cube.faces['B'][5] == aux1):
            B_(cube)
        elif(cube.faces['U'][7] == aux2 and cube.faces['F'][1] == aux1):
            U(cube)
            U(cube)
            B(cube)
            B(cube)
        elif(cube.faces['U'][5] == aux2 and cube.faces['R'][1] == aux1):
            U_(cube)
            B(cube)
            B(cube)
        elif(cube.faces['U'][3] == aux2 and cube.faces['L'][1] == aux1):
            U(cube)
            B(cube)
            B(cube)
        elif(cube.faces['U'][1] == aux2 and cube.faces['B'][7] == aux1):
            B(cube)
            B(cube)
        elif(cube.faces['U'][7] == aux2 and cube.faces['F'][1] == aux1):
            U(cube)
            L_(cube)
            B(cube)
            L(cube)
        elif(cube.faces['U'][5] == aux2 and cube.faces['R'][1] == aux1):
            R(cube)
            B_(cube)
            R_(cube)
        elif(cube.faces['U'][3] == aux2 and cube.faces['L'][1] == aux1):
            L_(cube)
            B(cube)
            L(cube)
        elif(cube.faces['U'][1] == aux2 and cube.faces['B'][7] == aux1):
            U_(cube)
            L_(cube)
            B(cube)
            L(cube)
            
    #Ahora haremos el F2L (First two layers)
    #Tendremos en cuenta siempre que el cubo quiere colocar la esquina inferior izquierda y la arista derecha, haciendo un rotate 4 veces

    
    for i in range(0,4):
        aux1 = reach.faces['F'][8]
        aux2 = reach.faces['R'][6]
        
        aux3 = reach.faces['F'][5] 
        aux4 = reach.faces['R'][3]
        
        aux5 = reach.faces['D'][2]
        
        F2L(cube, aux1, aux2, aux3, aux4, aux5)

        rotate(cube)
        
        aux1 = reach.faces['R'][8]
        aux2 = reach.faces['B'][2]
        
        aux3 = reach.faces['R'][5]
        aux4 = reach.faces['B'][5]
        
        aux5 = reach.faces['D'][8]
        
        F2L(cube, aux1, aux2, aux3, aux4, aux5)
        
        rotate(cube)
        
        aux1 = reach.faces['B'][0]
        aux2 = reach.faces['L'][6]
        
        aux3 = reach.faces['B'][3]
        aux4 = reach.faces['L'][3]
        
        aux5 = reach.faces['D'][6]
        
        F2L(cube, aux1, aux2, aux3, aux4, aux5)
        
        rotate(cube)
        
        aux1 = reach.faces['L'][8]
        aux2 = reach.faces['F'][6]
        
        aux3 = reach.faces['L'][5]
        aux4 = reach.faces['F'][3]
        
        aux5 = reach.faces['D'][0]
        
        F2L(cube, aux1, aux2, aux3, aux4, aux5)
        
        rotate(cube)
        

    #En este punto tenemos hecho el F2L completo
    
    aux1 = reach.faces['U'][1]
    aux2 = reach.faces['B'][7]
    
    aux3 = reach.faces['U'][3]
    aux4 = reach.faces['L'][1]
    
    aux5 = reach.faces['U'][5]
    aux6 = reach.faces['R'][1]
    
    aux7 = reach.faces['U'][7]
    aux8 = reach.faces['F'][1]
    
    aristas = [0, 0, 0, 0]
    
    if((cube.faces['U'][1] == aux1 and cube.faces['B'][7] == aux2) or (cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4) or (cube.faces['U'][1] == aux5 and cube.faces['B'][7] == aux6) or (cube.faces['U'][1] == aux7 and cube.faces['B'][7] == aux8)):
        aristas[0] = 1
    rotate_(cube)
    if((cube.faces['U'][1] == aux1 and cube.faces['B'][7] == aux2) or (cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4) or (cube.faces['U'][1] == aux5 and cube.faces['B'][7] == aux6) or (cube.faces['U'][1] == aux7 and cube.faces['B'][7] == aux8)):
        aristas[1] = 1
    rotate_(cube)
    if((cube.faces['U'][1] == aux1 and cube.faces['B'][7] == aux2) or (cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4) or (cube.faces['U'][1] == aux5 and cube.faces['B'][7] == aux6) or (cube.faces['U'][1] == aux7 and cube.faces['B'][7] == aux8)):
        aristas[2] = 1
    rotate_(cube)
    if((cube.faces['U'][1] == aux1 and cube.faces['B'][7] == aux2) or (cube.faces['U'][1] == aux3 and cube.faces['B'][7] == aux4) or (cube.faces['U'][1] == aux5 and cube.faces['B'][7] == aux6) or (cube.faces['U'][1] == aux7 and cube.faces['B'][7] == aux8)):
        aristas[3] = 1
    rotate_(cube)
    
    if(aristas[0] == 1):
        if(aristas[1] == 1 and aristas[2] == 0):
            rotate_(cube)
            orientar(cube)
            orientar(cube)
            rotate(cube)
        elif(aristas[1] == 0 and aristas[2] == 1):
            rotate(cube)
            rotate(cube)
            orientar(cube)
            orientar(cube)
            rotate(cube)
            rotate(cube)
        else:
            rotate(cube)
            orientar(cube)
            rotate_(cube)
    elif(aristas[1] == 1):
        if(aristas[2] == 1):
            orientar(cube)
        else:
            orientar(cube)
            orientar(cube)
    elif(aristas[2] == 1):
        rotate(cube)
    else:
        orientar(cube)
        rotate_(cube)
        rotate_(cube)
        orientar(cube)
        orientar(cube)
        rotate(cube)
        rotate(cube)

    #Ahora tenemos la cruz de arriba, pero no sabemos si está bien orientada.
    
    done = False
    
    while(not done):
        if(cube.faces['F'][1] == aux8):
            if(cube.faces['R'][1] == aux6):
                permutar(cube)
                done = True
            elif(cube.faces['L'][1] == aux4):
                rotate_(cube)
                permutar(cube)
                rotate(cube)
                done = True
            elif(cube.faces['B'][7] == aux2):
                rotate(cube)
                permutar(cube)
                U_(cube)
                rotate_(cube)
                permutar(cube)
                done = True
        elif(cube.faces['R'][1] == aux6):
            if(cube.faces['L'][1] == aux4):
                permutar(cube)
                rotate_(cube)
                U_(cube)
                permutar(cube)
                rotate(cube)
                done = True
            elif(cube.faces['B'][7] == aux2):
                rotate(cube)
                permutar(cube)
                rotate_(cube)
                done = True
        else:
            U(cube)
    
    #Ya tenemos la cruz bien orientada. Ahora falta colocar las esquinas
    
    aux1 = reach.faces['U'][8]
    aux2 = reach.faces['F'][2]
    aux3 = reach.faces['R'][0]
    
    if(cube.faces['F'][0] == aux1 or cube.faces['U'][6] == aux1 or cube.faces['L'][2] == aux1):
        if(cube.faces['F'][0] == aux2 or cube.faces['U'][6] == aux2 or cube.faces['L'][2] == aux2):
            if(cube.faces['F'][0] == aux3 or cube.faces['U'][6] == aux3 or cube.faces['L'][2] == aux3):
                rotate_(cube)
                permutarEsquinas(cube)
                rotate(cube)
    
    done = False
    
    while(not done):
        if(cube.faces['F'][2] == aux1 or cube.faces['U'][8] == aux1 or cube.faces['R'][0] == aux1):
            if(cube.faces['F'][2] == aux2 or cube.faces['U'][8] == aux2 or cube.faces['R'][0] == aux2):
                if(cube.faces['F'][2] == aux3 or cube.faces['U'][8] == aux3 or cube.faces['R'][0] == aux3):
                    done = True
                else:
                    permutarEsquinas(cube)
            else:
                permutarEsquinas(cube)
        else:
            permutarEsquinas(cube)
                
    rotate(cube)
    
    done = False
    
    while(not done):
        if(cube.faces['F'][2] == aux1 or cube.faces['U'][8] == aux1 or cube.faces['R'][0] == aux1):
            if(cube.faces['F'][2] == aux2 or cube.faces['U'][8] == aux2 or cube.faces['R'][0] == aux2):
                if(cube.faces['F'][2] == aux3 or cube.faces['U'][8] == aux3 or cube.faces['R'][0] == aux3):
                    done = True
                else:
                    permutarEsquinas(cube)
            else:
                permutarEsquinas(cube)
        else:
            permutarEsquinas(cube)
    
    rotate_(cube)
    
    aux1 = reach.faces['U'][0]
    aux2 = reach.faces['U'][2]
    aux3 = reach.faces['U'][6]
    aux4 = reach.faces['U'][8]
    
    done = False
    
    while(not done):
        if(cube.faces['U'][8] == aux1):
            U(cube)
            done = True
        else:
            sexyMove(cube)
        done = False
    
    while(not done):
        if(cube.faces['U'][8] == aux1):
            U(cube)
            done = True
        else:
            sexyMove(cube)
            
        done = False
    
    while(not done):
        if(cube.faces['U'][8] == aux1):
            U(cube)
            done = True
        else:
            sexyMove(cube)
            
        done = False
    
    while(not done):
        if(cube.faces['U'][8] == aux1):
            U(cube)
            done = True
        else:
            sexyMove(cube)       
    
    
    #Cubo terminado!

###############################################################################################
#Esta serie de test se harán para comprobar que todos los movimientos funcionan correctamente.#
###############################################################################################

#print("Estado normal del cubo: ")
#printCube(testCube)
#print("***")
#
#print("Push:")
#push(testCube)
#printCube(testCube)
#print("***")
#
#print("Estado normal del cubo: ")
#push(testCube)
#push(testCube)
#push(testCube)
#printCube(testCube)
#print("***")
#
#print("Rotate: ")
#rotate(testCube)
#printCube(testCube)
#print("***")
#
#print("Rotate_: ")
#rotate_(testCube)
#printCube(testCube)
#print("***")
#
#print("Move: ")
#move(testCube)
#printCube(testCube)
#print("***")
#
#print("Move_")
#move_(testCube)
#printCube(testCube)
#print("***")
#
#print("Movimiento U")
#U(testCube)
#printCube(testCube)
#
#print("Movimiento U_")
#U_(testCube)
#printCube(testCube)
#
#print("Movimiento F")
#F(testCube)
#printCube(testCube)
#
#print("Movimiento F_")
#F_(testCube)
#printCube(testCube)
#
#print("Movimiento D")
#D(testCube)
#printCube(testCube)
#
#print("Movimiento D_")
#D_(testCube)
#printCube(testCube)
#
#print("Movimiento B")
#B(testCube)
#printCube(testCube)
#
#print("Movimiento B_")
#B_(testCube)
#printCube(testCube)
#
#print("Movimiento R")
#R(testCube)
#printCube(testCube)
#
#print("Movimiento R_")
#R_(testCube)
#printCube(testCube)
#
#print("Movimiento L")
#L(testCube)
#printCube(testCube)
#
#print("Movimiento L_")
#L_(testCube)
#printCube(testCube)

#TODOS LOS TESTS PASAN CORRECTAMENTE

                
#cube = Cube()
#setColorsCamera(cube)--> Camera
#setColors(cube)x
#setColorsManual(cube)--> Manual

#cube = copy.deepcopy(solved)
#cube.faces['U'][4] = 'G'
#cube.faces['F'][4] = 'O'
#cube.faces['D'][4] = 'B'
#cube.faces['B'][4] = 'R'
#cube.faces['R'][4] = 'Y'
#cube.faces['L'][4] = 'W'

#print("Starting state:")
#printCube(cube)
#print("**")
#printCube(solved)
#print("**************************************")

#Para el escaneo, el cubo hará -> SCAN, PUSH, SCAN, PUSH, SCAN, PUSH, SCAN, PUSH, ROTATE, PUSH, SCAN, PUSH, PUSH, ROTATE_, ROTATE_, SCAN, PUSH, PUSH, PUSH, ROTATE
