from everyday_helloworld.main import hello


def test_hello():
    #assert hello() == "Hello, World!"
    assert hello("World") == "Hello, CI!"
    assert hello("Python") == "Hello, Python!"
