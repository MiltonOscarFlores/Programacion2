# Crear un programa que permita al usuario ingresar una lista de numeros.
# De esa lista de numeros almacenar en otra lista los numeros impares.

# El programa debe de mostrar por pantalla la lista de numeros originales
# y la lista de numeros impares.

# INICIO
list_of_numbers = []
list_of_odd_numbers = []
flag = False
print("Enter one number at a time or type 'exit' to finish:")

while not flag:
    numbers = input("> ")
    if numbers == "exit":
        flag = True
    else:
        list_of_numbers.append(int(numbers))

for number in list_of_numbers:
    if number % 2 != 0:
        list_of_odd_numbers.append(number)


print(f"The list of numbers is: {list_of_numbers}")
print(f"The odd numbers are:{list_of_odd_numbers}")
# FIN
