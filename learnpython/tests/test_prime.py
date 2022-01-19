from learnpython import __version__
from learnpython import prime

def test_version():
    assert __version__ == '0.1.0'
    


def test_1_is_a_prime_number():
    list_of_prime_numbers = prime.add_to_list_if_number_is_prime(1)
    assert len(list_of_prime_numbers) == 1

def test_2_is_a_prime_number():
    list_of_prime_numbers = prime.add_to_list_if_number_is_prime(2)
    assert len(list_of_prime_numbers) == 2

def test_7_is_a_prime_number():
    list_of_prime_numbers = prime.add_to_list_if_number_is_prime(7)
    assert len(list_of_prime_numbers) == 5

def test_100_is_a_prime_number():
    list_of_prime_numbers = prime.add_to_list_if_number_is_prime(100)
    assert len(list_of_prime_numbers) == 26
    print('does this work')
