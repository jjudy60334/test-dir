from src.app import print_hello


def test_print_hello():
    assert 'hello world' == print_hello()
