import re # Para poder validar si tiene caracteres especiales

# Pedimos la contraseña y guardamos en variable password
password = input("Ingrese contraseña: ")

# Creamos la funcion para validar la contraseña
def validar_contrasena(password):
    # Variable que contendrá si la contraseña es válida o no
    global is_validate
    is_validate = False  # Inicializa la variable is_validate

    # Validamos la longitud
    if len(password) > 7:
        # Validamos si contiene mayúsculas
        has_mayus = any(i.isupper() for i in password)
        if has_mayus:
            # Validamos si contiene minúsculas 
            has_minus = any(i.islower() for i in password)
            if has_minus:
                # Validamos si contiene números
                has_num = any(i.isdigit() for i in password)
                if has_num:
                    # Validamos si tiene caracteres especiales
                    has_character = bool(re.search(r'[^a-zA-Z0-9\s]', password))
                    if has_character:
                        is_validate = True        
                    else:
                        print("Contraseña sin caracteres especiales")
                else:
                    print("Contraseña sin números")
            else:
                print("Contraseña sin minúsculas")
        else:
            print("Contraseña sin mayúsculas")
    else:
        print("Contraseña muy corta")

    if is_validate:
        print("Contraseña segura")
    else:
        print("Fail Pass")

validar_contrasena(password)