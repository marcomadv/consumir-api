from appcoints.config import APIKEY
from appcoints.models import *
from appcoints.views import *

class AppCoinsController:

    def executeProgram(self):  
        allcoin = AllCoinApiIo()
        viewTools = Views()
        #consulta de todas las monedas
        allcoin.getAllCoins(APIKEY)

        viewTools.viewListCoins(allcoin)
        #########################################################################
        moneda_cripto = viewTools.insertCoin()

        while moneda_cripto != "" and moneda_cripto.isalpha() == True:
            if moneda_cripto in allcoin.lista_criptos:
                exchange = Exchange(moneda_cripto)
                try:
                    exchange.updateExchange(APIKEY)
                    viewTools.viewRateExchange(exchange)
                except ModelError as error:
                    viewTools.viewError(error)
            
            moneda_cripto = viewTools.insertCoin()