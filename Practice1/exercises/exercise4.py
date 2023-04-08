"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
a = int(numero_01)
b = int(numero_02)
c = int(numero_03)
d = int(numero_04)
suma_de_numeros = a + b + c + d
# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
aa = str(numero_01)
bb = str(numero_02)
cc = str(numero_03)
suma_de_numeros_string = aa + bb + cc
# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
aaa = int(numero_binario,2)
bbb = int(numero_octal,8)
ccc = int(numero_hexadecimal,16)

multiplicacion_de_numeros = aaa * bbb * ccc
# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todos los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
aaaa = int(numero_01)
bbbb = int(numero_02,16)
cccc = int(numero_03,8)
dddd = numero_04
resultado_resta = aaaa - bbbb - cccc - dddd


# COMPLETAR - FIN

assert resultado_resta == -456350
