def setColorsManual(cube):
    for face in cube.faces:
        for i in range(9):
            color = input(f"Enter the color for position {i+1} of face {face}: ")
            cube.faces[face][i] = color
            
