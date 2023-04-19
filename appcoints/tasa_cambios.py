import requests

apikey = "21731024-FD09-4C6F-B749-E8C12255AC64"

#3 creo un input para cargar la moneda digital;
moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:
    #invocar metodo get con url especifica

    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}")

    respuesta = r.json() #respuesta http en formato de diccionario
    #ejercicio1, como capturamos solo el rate y mostramos y #ejercicio 2, como capturo el error;

    if r.status_code == 200:
        print("{:.2f}€".format(respuesta["rate"])) #1903.90€
        break
    else:
        print(respuesta["error"])

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()







'''
print("codigo http de respuesta", r.status_code)

print("cabecera", r.headers['content-type'])

print("encoding:", r.encoding)

print("respuesta en string:",r.text)
print(type(r.text))
print("respuesta en json",r.json())

print(type(r.json()))
'''