#Libraries
import os

def get_os():
    return "nt" if os.name == "nt" else "clear"

def clear_console():
    os.system("cls" if get_os() == "nt" else "clear")

def getNumberType(value):
    return "número par" if value % 2 == 0 else "número impar"

app_tittle = "NumberCheck"
app_description = f"""
    Hola Usuario! Para usar {app_tittle} debes ingresar el número y
    la aplicación te responderá con el resultado.

    Si deseas salir escibe "leave" o presiona "CTRL+C" y el programa se cerrará.
"""

clear_console()
print(f"""
    ---->   {app_tittle}    <----
    {app_description}"""
    )

while True:
    try:
        inputValue = input(">>> ")

        if any(word in inputValue for word in {"leave", "salir"}):
            clear_console()
            print(f"Cerrando {app_tittle}...")
            break

        if inputValue.isdigit():
            num = int(inputValue)
            print(f"Seleccionaste {num} y es {getNumberType(num)}.")

        else:
            clear_console()
            print("Debes ingresar un número válido.")
    except KeyboardInterrupt:
        print(f"Cerrando {app_tittle}...")
        break