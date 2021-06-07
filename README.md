# Proyecto_Final_Entrega_1

Link en GitHub: [Proyecto_Final_Entrega_1](https://github.com/kamurillUC/Proyecto_Final_Entrega_1)

Solo ejecutar el main.py
Funciones en mis_funciones.py
Clases en mis_clases.py
 
# Requerimientos: 
1- Deberá crear una “Portada” que incluya el nombre “Tienda Simón” y sus datos personales  e imprimir estos datos en la terminal. 
2- Deberá preguntar al interesado por su nombre de usuario y contraseña. a. El sistema debe contar con dos roles, uno de administrador y otro de visitante. b. Se recomienda el uso de diccionarios.  
c. Cada usuario deberá contar con la siguiente información: 
i. username 
ii. password 
iii. full_name 
iv. role 
d. Los datos para los usuarios deben ser los siguientes: 
i. Usuario administrador: 
1. username: admin 
2. password: admin 
3. full_name: Alejandro Sanchez 
4. role: admin 
ii. Usuario invitado: 
1. username: guest 
2. password: guest 
3. full_name: {nombre_del_estudiante} 
4. role: invitado. 
3- Debe solicitar el nombre de usuario y contraseña.  
4- En caso de que estos coincidan con alguno de los dos usuarios existentes, el programa  debe continuar, de lo contrario debe finalizar. 
5- Debe imprimir en pantalla: “Bienvenido al sistema de inventarios de tienda Simón,  {full_name} es un placer atenderle” 
6- Seguidamente se requiere crear un menú con las siguientes opciones si el usuario  conectado es administrador:  
Desea ingresar al sistema de inventarios(si/no):



-Si la respuesta es negativa, termina el programa, de lo contrario se deberá mostrar el siguiente  menú: 
Seleccione un departamento: 
1- Damas 
2- Caballeros 
3- Niños



4- Salir



7- En caso de seleccionar 4, el programa finaliza. 
8- Debe almacenar en memoria cual fue el departamento seleccionado y mostrar el  siguiente menú: 
Menú de productos del departamento {nombre_departamento}: 
1-Consultar 
2-Ingresar 
3-Actualizar  
4-Eliminar  
5-Volver 
6-Salir



9- En caso de seleccionar la opción 1 se debe mostrar en la pantalla “Consulta de productos” 10- En caso de seleccionar la opción 2 se debe mostrar en la pantalla “Ingrese el producto” 11- En caso de seleccionar la opción 3 se debe mostrar en la pantalla “Actualice el producto” 12- En caso de seleccionar la opción 4 se debe mostrar en la pantalla “Elimine el producto” 13- En caso de seleccionar volver, se deberá mostrar nuevamente el menú de departamentos. 14- En caso de seleccionar la opción 5 se debe mostrar en la pantalla “Saliendo del sistema  de inventarios” y se debe salir del menú.  
15- En caso de que el usuario conectado tenga el rol de invitado se debe mostrar el siguiente  menú: 
Desea ingresar al sistema de inventarios(si/no): 
Seleccione un departamento: 
1- Damas 
2- Caballeros 
3- Niños 
Menú de productos del departamento {nombre_departamento}: 
1-Consultar 
2-Volver 
3-Salir



16- En caso de seleccionar la opción 1 se debe mostrar en la pantalla “Consulta de productos” 17- En caso de seleccionar la opción 2 se debe regresar al menú de departamentos. 
18- En caso de seleccionar la opción 3 se debe mostrar en la pantalla “Saliendo del sistema  de inventarios” y se debe salir del menú. 
Nota: Luego de completar cada acción se debe regresar al menú anterior. Por ejemplo, Luego de  mostrar todos los productos se debe mostrar nuevamente el menú para seleccionar otra opción. 
