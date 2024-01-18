import requests

# recupero credenciales

def leer_credenciales_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            # Leer las líneas del archivo
            lineas = file.readlines()

            # Crear un diccionario para almacenar las credenciales
            credenciales = {}
            
            # Iterar sobre las líneas y agregar al diccionario
            for linea in lineas:
                # Dividir la línea en la forma "clave = valor"
                clave, valor = linea.strip().split(' = ')
                
                # Almacenar en el diccionario
                credenciales[clave] = valor

        return credenciales.get('User'), credenciales.get('Password')
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no se encuentra.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Uso de la función
archivo_credenciales = "C:\\Users\\lcano\\Desktop\\proyectos\\geo\\config.txt"
User, Password = leer_credenciales_desde_archivo(archivo_credenciales)

print(f"User: {User}")
print(f"Password: {Password}")

# Ingresa tus credenciales aquí


url_login = "https://customerapi.geovictoria.com/api/v1/Login"

# Parámetros que se enviarán en la solicitud POST
parametros = {
    "user": User,
    "password": Password
}
print(parametros)
# Realizar la solicitud POST con los parámetros
response = requests.post(url_login, json=parametros)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    resultado = response.json()
    token = resultado.get('token')
    print(token)


else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")


# Parte dos envio de marca


url = "https://customerapi.geovictoria.com/api/v1/punch/AddArtificial"


datos_solicitud = {
    "Date" : "20240117172900" ,
    "UserIdentifier" : "38319251",
    "Type" : "Salida"

}

headers = {
        "Authorization": f"{token}"
    }

response = requests.post(url, json=datos_solicitud, headers=headers)

# Verificar si la solicitud fue exitosa (código 2xx)
if response.ok:
    resultado = response.json()
    print(resultado)
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
    try:
        # Imprimir el contenido de la respuesta en caso de error
        error_response = response.json()
        print("Detalles del error:", error_response)
    except Exception as e:
        # En caso de que la respuesta no sea JSON, imprimir el contenido como texto
        print("Contenido del error:", response.text)




















