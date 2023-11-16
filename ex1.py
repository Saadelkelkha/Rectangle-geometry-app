class Rectangle():
    def __init__(self, longueur, largeur):
        # Initialize the Rectangle object with given length and width
        self.longueur = longueur
        self.largeur = largeur

    def Perimetre(self):
        # Calculate and return the perimeter of the rectangle
        P = (self.largeur + self.longueur) * 2
        return P
    
    def Aire(self):
        # Calculate and return the area of the rectangle
        A = self.largeur * self.longueur
        return A
    
    def IsCarre(self):
        # Check if the rectangle is a square and return True or False
        if self.largeur == self.longueur:
            return True
        else:
            return False

    def AfficheRectangle(self):
        # Display information about the rectangle, including its length, width, perimeter, area, and whether it's a square or not
        print("longueur :", self.longueur)
        print("largeur :", self.largeur)
        print("Perimetre :", Rectangle.Perimetre(self))
        print("Aire :", Rectangle.Aire(self))
        if Rectangle.IsCarre(self) == True:
            print("Il s'agit d'un carre")
        else:
            print("Il ne s'agit pas d'un carre")


