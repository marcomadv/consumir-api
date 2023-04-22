from appcoints.models import *
from appcoints.config import APIKEY
import pytest

def test_allcoin():
    todo = AllCoinApiIo()
    assert isinstance(todo, AllCoinApiIo)
    todo.getAllCoins(APIKEY)
    total = len(todo.lista_criptos) + len(todo.lista_no_criptos)
    assert total == 16379

def test_exchange_ok():
    cambio = Exchange("ETH")
    cambio.updateExchange(APIKEY)
    assert cambio.rate != None

def test_exchange_error():
    cambio2 = Exchange("ÑÑ")
    with pytest.raises(ModelError) as exceptionInfo:    
        cambio2.updateExchange(APIKEY)
    assert cambio2.status_code == 550