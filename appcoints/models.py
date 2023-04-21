import requests

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

