from pyscript import document,display
# DICTIONARY CONTAINING PLANET INFORMATION

planets= {"H" : ("Hydrogen", 1, 1.0078, ), "He" :
          #            0.     1  2       
           ("Helium", 2, 4.0026), "C" : ("Carbon", 6, 12.011), "N" : ("Nitrogen", 7, 14.007), "O" : ("Oxygen", 8, 15.999), "F" :("Fluorine", 9, 18.998), "Ne" : ("Neon", 10, 20.180), "P"  :("Phosphorus", 15, 30.974), "S" : ("Sulfar", 16, 32.065), "Cl" : ("Chlorine", 17, 35.453), "Ar" : ("Argon", 18, 39.948), "Se" : ("Selenium", 34, 78.960), "Br" : ("Bromine", 35, 79.904), "Kr" : ("Krypton", 36, 83.798), "I" : ("Iodine", 53, 126.90), "Xe" : ("Xenon", 54, 131.29), "Rn" : ("Radon", 86, 222)}

# KEY : VALUE
    # ELEMENT: ELEMENT NAME, ATOMIC #, ELEMENT MASS

def search_element(e):
    # Get the input FROM HTML
    Element1 = document.getElementById("element1").value
    # Retrieve information from dictionary
    result = planets.get(Element1, ("Element not found", "-", "-") )
    # Element symbol, Name, Number, Mass
    document.getElementById("code").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]