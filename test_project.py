import pytest
from project import guess_the_word, guess_the_number, guess_the_map


def test_guess_the_word():
    assert guess_the_word("python", "It's a Snake.") == True
    assert guess_the_word("java", "It's a Coffee.") == True
    assert guess_the_word("ruby", "It's a Red Diamond.") == True
    assert guess_the_word("html", "Web Development") == True
    assert guess_the_word("machine", "1 or 0 coding.") == True
    assert guess_the_word("basket", "It's a container used for storing clean or dirty clothes.") == True

def test_guess_the_number():
    pass

def test_guess_the_map():
    assert guess_the_map("paris", "The city of love, known for the Eiffel Tower.") == True
    assert guess_the_map("london", "Capital city of the UK, famous for the Big Ben.") == True
    assert guess_the_map("tokyo", "Capital of Japan, known for its technology and cherry blossoms.") == True
    assert guess_the_map("newyork", "City that never sleeps, home of the Statue of Liberty.") == True
    assert guess_the_map("sydney", "Known for the Opera House and Harbour Bridge in Australia.") == True

if __name__ == "__main__":
    pytest.main()
