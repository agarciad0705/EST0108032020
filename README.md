# EST0108032020
Procedimiento:
1:Instalación ambiente 
Instalación pyton
	- https://www.python.org/

Intalación visual studio comunnity
	- https://code.visualstudio.com/?wt.mc_id=DX_841432
Instalación de cliente rest 
	- https://insomnia.rest/
Instalación de librerías desde consola:
	>>> pip install flask
	>>> pip install phonenumbers
2: Codificación:
Task 1
Importación de librerías:
 
Puesta en marcha del servicio en el puerto 4000:
 
Definición de método:
 
Definición del método en el cliente (carga del archivo numbers.csv):
 
Lectura del archivo en el servicio:
 
Procesamiento de información:
 
Basado en la documentación:
 Obtenemos el dato numérico basado en un texto, esto nos ayuda a quitar los paréntesis y formatear el número en un número valido para los procesos subsecuentes.
 
Ahora formateamos el número para poder ser procesado por el método siguiente que nos dice sí es un número valido.
 
También lo parseamos en formato valido para obtener la localización geográfica
 
Ahora solo formateamos los resultados e implementamos un método para evitar espacios en blanco:
 
Los añadimos a una lista 
 
Posteriormente la retornamos al cliente
 

Task 2 
En el siguiente código se genera el segundo número en base al ingresado, se toma la localidad y se genera dos grupos de aleatorios creando un número random correspondiente a algún número de la misma localidad.
 
Método de validación de números:
 
Llamado desde cliente:

 
 


