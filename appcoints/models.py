import requests

class ModelError(Exception):
    pass

class AllCoinApiIo:
    def __init__(self):
        self.lista_criptos=[]
        self.lista_no_criptos = []

    def getAllCoins(self, apikey):
        r = requests.get(f"https://rest.coinapi.io/v1/assets/?apikey={apikey}")

        if r.status_code != 200:
            raise Exception("Error en consulta codigo de error:{}".format(r.status_code))
        
        lista_general = r.json() #16379 registros
  

        for item in lista_general:
            if item["type_is_crypto"] == 1:
                self.lista_criptos.append(item["asset_id"])
            else:
                self.lista_no_criptos.append(item["asset_id"])

class Exchange:
    def __init__(self, cripto):
        self.moneda_cripto = cripto
        self.rate = None
        self.status_code = None

    def updateExchange(self,apikey):
        r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{self.moneda_cripto}/EUR?apikey={apikey}")

        respuesta = r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = respuesta['rate']
        else:
            raise ModelError(f"status: {r.status_code}, error: {respuesta['error']}") 