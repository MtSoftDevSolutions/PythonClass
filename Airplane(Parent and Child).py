#This is an exercise to explore parent and child classes and how they relate to each other
class Airplane: #Airplane is parent class
    wings = input("How many wings does this plane have?") #Typically there are 2 wings, but you can never rule out experimental planes
    color = input("What is the color of the plane?")
    company = input("Which company does this plane belong to?") #Could be used later to form relation between parent and child (i.e. older companies that no longer exist may have been using prop planes)

class PropPlane(Airplane): #the way the syntax works here shows that PropPlane is a child class of Airplane
    movementmech = "propeller" 
    history = "original" #The first airplanes started out as prop planes

class JetPlane(Airplane):
   company:"Delta"
   span: 20000
    
    
