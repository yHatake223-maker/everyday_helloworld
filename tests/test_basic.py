from everyday_helloworld.main import hello

def test_hello():
    assert hello() == "Hello, World!"
    assert hello("Python") == "Hello, Python!"
