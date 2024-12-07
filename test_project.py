import pytest
from unittest.mock import patch
from project import choose_word, choose_city

# Test for choose_word function
def test_choose_word():
    # Mock the word list with specific content
    mock_word_list = [
        ("python", "A snake or a programming language"),
        ("java", "A coffee drink"),
        ("ruby", "A red gemstone")
    ]
    
    # Patch the load_word_list function to return the mock list
    with patch('project.load_word_list', return_value=mock_word_list):
        word, clue = choose_word()
        
        # Assert that the word chosen is from the mock list
        assert (word, clue) in mock_word_list

# Test for choose_city function
def test_choose_city():
    # Mock the city list with specific content
    mock_city_list = [
        ("paris", "Capital of France"),
        ("london", "Capital of England"),
        ("tokyo", "Capital of Japan")
    ]
    
    # Patch the load_city_list function to return the mock list
    with patch('project.load_city_list', return_value=mock_city_list):
        city, clue = choose_city()
        
        # Assert that the city chosen is from the mock list
        assert (city, clue) in mock_city_list

if __name__ == "__main__":
    pytest.main()
