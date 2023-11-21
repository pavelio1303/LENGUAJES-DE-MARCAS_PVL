from lxml import etree

tree = etree.parse("movies.xml")
root = tree.getroot()

# Crea un script que solicite por pantalla un rating de edad y muestre todas las peliculas de ese rating
"""
solicitaRating = input("Rating edad película: ")

print(root.xpath(f"Movie[@rating = '{solicitaRating}']/Title/text()"))
"""
#Crea un script de python que solicite por pantalla:
# - Un rating de edad
# - Un género 
# - Una duración mínima
# Muestra las películas que complan esos requisitos.
"""
solicitaRating = input("Rating edad película: ")
solicitaGenero = input("Género película: ")
solicitaDuracionMinima = input("Duración mínima de la película: ")

print(root.xpath(f"Movie[@rating = '{solicitaRating}'][Genre = '{solicitaGenero}']/Title[@runtime >= {solicitaDuracionMinima}]/text()"))
"""

# Crea un script de python que muestre por pantalla:
#    1. La película más larga.
#    2. La película más corta.
#    3. La duración media de las películas.
#    4. Ten en cuenta que no todas las películas disponen del dato de duración.

# Además, el script debe solicitar por pantalla el nombre de una película y mostrar por pantalla si
#   está por encima o por debajo de la media.

# Si la película solicitada no tiene duracion, debe solicitar una película nueva hasta que sea válida.


# Ejer. 1 y 2:
listaTiempoPelisStr = root.xpath(f"Movie/Title/@runtime")

listaTiempoPelisInt = []

for tiempoStr in listaTiempoPelisStr:       # Bucle en el que convertimos Str a Int
    tiempoStr = int(tiempoStr)
    listaTiempoPelisInt.append(tiempoStr)
print(listaTiempoPelisInt)

tiempoPeliculaMasLarga = max(listaTiempoPelisInt)
tiempoPeliculaMasCorta = min(listaTiempoPelisInt)

nombrePeliculaLarga = root.xpath(f"Movie/Title[@runtime={tiempoPeliculaMasLarga}]/text()")[0]
nombrePeliculaCorta = root.xpath(f"Movie/Title[@runtime={tiempoPeliculaMasCorta}]/text()")[0]

print(f"La película con mayor tiempo dura es {nombrePeliculaLarga} ({tiempoPeliculaMasLarga})")
print(f"La película con menor tiempo dura es {nombrePeliculaCorta} ({tiempoPeliculaMasCorta})")

# Ejer. 3:
tiempoTotal= 0
for tiempoPelicula in listaTiempoPelisInt:
    tiempoTotal += tiempoPelicula
    mediaTiempo = tiempoTotal//len(listaTiempoPelisInt)

print(f"La duración total de todas las películas es de {tiempoTotal} minutos")
print(f"La media de todas las películas es de {mediaTiempo} minutos aproximádamente")

# Ejer. 4:

tiempoPeliculaSolicitada = []

while len(tiempoPeliculaSolicitada) == 0:
    nombrePeliSolicitado = input("Dame el nombre de una película:\n")
    tiempoPeliculaSolicitada = root.xpath(f"Movie/Title = '{nombrePeliSolicitado}'/Title/@runtime") 

tiempoPeliculaSolicitada = int(tiempoPeliculaSolicitada[0])








