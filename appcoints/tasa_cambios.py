import requests


#invocar metodo get con url especifica

r = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey=21731024-FD09-4C6F-B749-E8C12255AC64")

print("codigo http de respuesta", r.status_code)

print("cabecera", r.headers['content-type'])

print("encoding:", r.encoding)

print("respuesta en string:",r.text)
print(type(r.text))
print("respuesta en json",r.json())
print(type(r.json()))