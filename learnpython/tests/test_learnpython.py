from learnpython import __version__
from learnpython import helloworld

def test_version():
    assert __version__ == '0.1.0'
    

def test_sayhello():
    assert helloworld.say_hello() == 'hello'