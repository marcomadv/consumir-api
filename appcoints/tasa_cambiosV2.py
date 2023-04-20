import requests
from config import APIKEY

#consulta de todas las monedas
r = requests.get(f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}")

if r.status_code != 200:
    raise Exception("Error en consulta codigo de error:{}".format(r.status_code))

lista_general = r.json() #16379 registros
lista_criptos=[]
lista_no_criptos = []

for item in lista_general:
    if item["type_is_crypto"] == 1:
        lista_criptos.append(item["asset_id"])
    else:
        lista_no_criptos.append(item["asset_id"])

print("cantidad_criptos: ",len(lista_criptos))
print("cantidad_no_criptos: ",len(lista_no_criptos))

#############################################

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:
    if moneda_cripto in lista_criptos:
        #invocar metodo get con url especifica
        r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}")

        respuesta = r.json() #respuesta http en formato de diccionario
        #ejercicio1, como capturamos solo el rate y mostramos y #ejercicio 2, como capturo el error;

        if r.status_code == 200:
            print("{:.2f}€".format(respuesta["rate"])) #1903.90€
            break
        else:
            print(respuesta["error"])

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()
