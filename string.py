string1 = "Cisco Router"

#se puede acceder a los indices de un string, cada caracter representa un indice
#el ultimo caracter de puede acceder con -1
#para leer un string del reves se comineza con -1 y va decrenciendo en negativo
string1[1]
string1[-1]

#para saber el lenght de un caracter usar la funcion len
len(string1)

####### METODOS #######

a = "Cisco Switch"
#Arroja el indice del caracter que se le pasa en el parentesis
a.index("i")
#1

#Arroja el numero de veces que encuentra la letra i en el string
a.count("i")
#2

#Arroja el primer indice del macth que hace con los caracteres que se le pasa en el parentesis
a.find("sco")
#2

#Si no encuentra ningun match arroja -1
a.find("xyz")
#-1

#Metodo para pasar todo a minuscula un string
a.lower()
#'cisco switch'

#Metodo para pasar a mayuscula un string, no interfiere con el string original, o sea mantiene su valor a pesar del metodo

#Metodo para verificar con letra comienza un string, retorna true o false y es casesensitive
a.startswith("c")
False
a.startswith("C")
True

#Metodo para verificar con letra termina un string
a.endswith("h")
True

#Metodo para eliminar lo que esta al inicio y al fin de un string, si no se pasa nada en el parentisis elimina los espacios
b = "  Cisco Switch  "
b.strip()
'Cisco Switch'
c = "$$$Cisco Switch$$$"
c.strip("$")
'Cisco Switch'
c = "$$$Cisco $$$Switch$$$"
c.strip("$")
'Cisco $$$Switch'

#Metodo para reemplazar un caracter por otro, se pasa primero el caracter que va a ser reemplazado, luego el nuevo valor
b
'  Cisco Switch  '
b.replace(" ", "")
'CiscoSwitch'

#Crea una lista segun el parametro de split definido
d = "Cisco,Juniper,HP,Avaya,Nortel"
d.split(",")
['Cisco', 'Juniper', 'HP', 'Avaya', 'Nortel']

#Metodo para insertar algo en un string, en este caso inserta entre cada letra un _
a
'Cisco Switch'
"_".join(a)
'C_i_s_c_o_ _S_w_i_t_c_h'
