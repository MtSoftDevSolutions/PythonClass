#This is an exercise to explore parent and child classes and how they relate to each other
class Airplane:
    wings = input("How many wings does this plane have?")
    color = input("What is the color of the plane?")
    company = input("Which company does this plane belong to?")

class PropPlane(Airplane):
    movementmech = propeller
    history = original

class JetPlane(Airplane):
    movementmech = Jets
    history = newer
    
