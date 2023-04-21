from appcoints.models import AllCoinApiIo
from appcoints.config import APIKEY

def test_allcoin():
    todo = AllCoinApiIo()
    assert isinstance(todo, AllCoinApiIo)
    todo.getAllCoins(APIKEY)
    total = len(todo.lista_criptos) + len(todo.lista_no_criptos)
    assert total == 16379
