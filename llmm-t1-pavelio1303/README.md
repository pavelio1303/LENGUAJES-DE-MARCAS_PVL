[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/57KK_QOL)

# DOCUMENTACIÓN PROYECTO LENGUAJES DE MARCAS

### DOCUMENTACIÓN DTD

A la hora de realizar un DTD sobre un XML primero procedo a identificar los elementos principales, empezando por la raíz, en este caso 'aemet'. A continuación visualizo las tabulaciones para comprobar que elementos son los siguientes, leyendo todo el documento XML para ver cuales se repiten, si lo hacen siempre en la misma cantidad o no, o incluso si pueden no estar.
Además hay que prestar especial atención a los atributos, más en este proyecto en el cual hay gran cantidad de ellos, para ir nombrándolos trás el elemento al que pertenecen correctamente.
Trás un vistazo general me percaté de que había unos valores estáticos que delimitaban cosas como información de la página (como web o idioma), los cuales iban a aparecer siempre de forma fija, además de la región a la que pertenece dicha previsión.
A continuación, encontramos el grueso con la previsión por días. Cada día contiene distintos valores metereológicos divididos en tramos horarios, teniendo más precisión cuanta más cercana sea la fecha a la actualidad (cosa a tener en cuenta más adelante).

### DOCUMENTACIÓN XSD

La complejidad a la hora de elaborar el XSD es algo mayor a la de un DTD puesto que especificamos con más precisión valores como el número exacto de apariciones (o su rango) de un elemento, además de la indicación de los formatos (si es un string, un decimal, integer, fecha, etc... ).
El proceso de elaboración, en cuanto a lectura del documento XML se refiere, es similar a la del DTD aunque distinto en su ejecución. Además de lo ya indicado de tener especial precisión en las características de cada elemento, también hay que tener ojo con las tabulaciones y cierres ya que un error en estos pueden variar toda la lógica estructural del XSD.



