# Crear un programa que permita ingresar una lista de numeros al usuario
# y muestre por pantalla el maximo entre ambos numeros.

# Nota : Hacerlo con la función max(a,b) y luego con una comparación

# INICIO
list_of_numbers = []
flag = False
acc = 0

print("Enter one number at a time or type 'exit' to finish:")

while flag == False:
    numbers = input("> ")
    list_of_numbers.append(int(numbers))
    acc += 1
    if numbers == "exit" or acc == 2:
        flag = True

print("The maximum number entered in the list is:", max(list_of_numbers))

max_number = list_of_numbers[0]

for number in list_of_numbers:
    if number > max_number:
        max_number = number

print("The maximum number by comparison is:", max_number)
# FIN
