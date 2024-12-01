import pytest
from project import guess_the_word, guess_the_number, guess_the_map


def test_guess_the_word():
    assert guess_the_word("python", "It's a Snake.") == True
    assert guess_the_word("java", "It's a Coffee.") == True
    assert guess_the_word("ruby", "It's a Red Diamond.") == True

def test_guess_the_number():
    assert guess_the_number(10) == True
    assert guess_the_number(5) == True

def test_guess_the_map():
    assert guess_the_map("paris", "The city of love, known for the Eiffel Tower.") == True
    assert guess_the_map("london", "Capital city of the UK, famous for the Big Ben.") == True

if __name__ == "__main__":
    pytest.main()