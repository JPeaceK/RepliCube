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

def setColors(cube):
    for face in cube.faces:
        for i in range(9):
            color = input(f"Enter the color for position {i+1} of face {face}: ")
            cube.faces[face][i] = color
            
    print(cube.faces['U'])

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
    
    
    
    
cube = Cube()
setColors(cube)
print("Estado normal:")
printCube(cube)
print("**************************************")
print("push")
push(cube)
printCube(cube)
print("**************************************")
print("rotate")
rotate(cube)
printCube(cube)
print("**************************************")
print("rotate_")
rotate_(cube)
printCube(cube)
print("**************************************")
print("move")
move(cube)
printCube(cube)
print("**************************************")
print("move_")
move_(cube)
printCube(cube)
print("**************************************")



#Para el escaneo, el cubo hará -> SCAN, PUSH, SCAN, PUSH, SCAN, PUSH, SCAN, PUSH, ROTATE, PUSH, SCAN, PUSH, PUSH, ROTATE_, ROTATE_, SCAN, PUSH, PUSH, PUSH, ROTATE


