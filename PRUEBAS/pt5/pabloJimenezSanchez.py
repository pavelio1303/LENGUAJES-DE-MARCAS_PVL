from lxml import etree

circuito = etree.parse("circuits.xml")
rootCir = circuito.getroot()

drivers = etree.parse("drivers.xml")
rootDriv = drivers.getroot()
 
# 1 -------------------------------
solicitaPaisCircuitos = input("¿De que pais deseas conocer los circuitos?\n")
solicitaPaisDrivers = input("¿De que nacionalidad deseas conocer los pilotos?\n")

print("") # Salto estético

respuestaCircuitosPais = rootCir.xpath(f"circuit[country = '{solicitaPaisCircuitos}']/name/text()")

respuestaDriversPais = rootDriv.xpath(f"driver[nationality = '{solicitaPaisDrivers}']/driverRef/text()")

print(f"Los circuitos de {solicitaPaisCircuitos}, son {respuestaCircuitosPais}\n")

print(f"Los pilotos con nacionalidad {solicitaPaisDrivers}, son {respuestaDriversPais}\n")

# 2 -------------------------------

listaAltitudCircuitosStr = rootCir.xpath(f"circuit/alt/text()")
# print(listaAltitudCircuitosStr)----Comprobación

listaAltitudCircuitosInt = []

for altitudStr in listaAltitudCircuitosStr:       # Bucle en el que convertimos Str a Int
    altitudStr = int(altitudStr)
    listaAltitudCircuitosInt.append(altitudStr)

maxAltitudCircuito = max(listaAltitudCircuitosInt)

respuestaCircuitoAltitud = rootCir.xpath(f"circuit[alt = '{maxAltitudCircuito}']/name/text()")
respuestaCircuitoAltitudPais = rootCir.xpath(f"circuit[alt = '{maxAltitudCircuito}']/country/text()")

print(f"El circuito con más altitud es {respuestaCircuitoAltitud} en {respuestaCircuitoAltitudPais} con una altitud de {maxAltitudCircuito}")

# 3 -------------------------------

pideAltitud = int(input("Dame una altitud:\n"))

circuitosMasAltitud = rootCir.xpath(f"circuit[alt >= {pideAltitud}]/name/text()")
circuitosMenosAltitud = rootCir.xpath(f"circuit[alt <= {pideAltitud}]/name/text()")

print(f"hay {len(circuitosMasAltitud)} con más altitud")
print(f"hay {len(circuitosMenosAltitud)} con menos altitud")

# 4 -------------------------------

pidePais = input("Dame un pais:\n")

circuitosPaisAltura = rootCir.xpath(f"circuit[country = '{pidePais}' and alt > {pideAltitud}]/name/text()")

print(circuitosPaisAltura)