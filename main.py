import turtle

class Circuito():
    corredores = []
    __posStartY = (-30 , -10, 10, 30) # tupla para posicionar las tortugas en el punto de salida
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen() # Se pone en privado para que predefinamos la pantalla como queramos
        self.__screen.setup(width, height) # sin que nadie pueda modificarlo
        self.__screen.bgcolor('lightgray')
        self.__startLine = - width / 2 + 20
        self.__finishLine = width / 2 - 20
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() # para que no pinten al posicionarse en el punto de salida
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
        







if __name__ == '__main__': # de esta manera si importamos circuito a otro programa, esta parte no se ejecutaria
    circuito = Circuito(640, 480)