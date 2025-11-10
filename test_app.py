# test_app.py

def soma(a, b):
    """Função simples que retorna a soma de dois números."""
    return a + b


def get_texto():
    """Função que retorna um texto para verificação."""
    return "UC10 - Teste Automatizado"


def test_soma_simples():
    """Testa se a soma de 2 + 3 resulta em 5."""
    assert soma(2, 3) == 5


def test_verifica_texto():
    """Testa se o texto retornado contém a palavra 'UC10'."""
    assert "UC10" in get_texto()
