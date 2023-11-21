from lxml import etree

#cargar el archivo XML
tree = etree.parse("biblioteca.xml")
root = tree.getroot()

# 1. Selección de elementos en XPath
print("1. Selección de elementos en XPath")
print()

# Selección de todos los elementos 'libro'
libros = root.xpath('//libro')

# Selección de la lista de autores | text() nos muestra el contenido de los elementos
print(root.xpath("libro/autor/text()"))

# Selección del titulo del primer libro

print(root.xpath("libro[1]/titulo/text()"))  # En XPATH la lista de nodos comienza por 1

# Selección del título del último libro

print(root.xpath("libro[last()]/titulo/text()")) # Con last() seleccionamos el último elemento

# Selección del penúltimo elemento

print(root.xpath("libro[last()-1]/titulo/text()"))

# Selección de los 3 primeros

print(root.xpath("libro[position()<=3]/titulo/text()"))

# Selección de la lista de títulos de un mismo autor

print(root.xpath("libro[autor = 'George Orwell']/titulo/text()"))

# Selección de títulos del género 'Novela distópica'

print(root.xpath("libro[genero = 'Novela distópica']/titulo/text()"))

# Selección de títulos del género 'Novela distópica' anteriores al 2000

print(root.xpath("libro[genero = 'Novela distópica' and año < 2000]/titulo/text()"))

print("Ejercicios de ejemplo a continuación:")

# 1. Qué autores han escrito libros del género 'Novela'?

print(root.xpath("libro[genero = 'Novela']/autor/text()"))

# 2. Qué autores han escrito libros del género 'Novela'? Muestra los 5 primeros

print(root.xpath("libro[genero = 'Novela'][position() <= 5]/autor/text()"))

# 3. Cuantos libros de género 'Novela' posteriores al año 2000 hay?

print(len(root.xpath("libro[genero = 'Novela' and año > 2000]/titulo/text()")))

# 4. Muestra todos los libros del autor del primer libro de la lista de 'Novela'

autor1 = root.xpath("libro[genero = 'Novela']/autor/text()")[0]

print(root.xpath(f"libro[autor = '{autor1}']/titulo/text()"))

# 5. Muestra todos los libros escritos entre 1950 y 1980

print(root.xpath("libro[año >= 1950 and año <= 1980]/titulo/text()"))



