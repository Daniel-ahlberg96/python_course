# TODO
# Use debuging in test
# Run individual tests
# Add test for encrypt_multiple_passwords() and invalid_characters_in()
from basic_syntax import *
import pytest

class TestAll():

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_getting_started(self):
        user = "Daniel"
        version_nr = 1
        getting_started(user, version_nr)
        captured = self.capsys.readouterr()
        assert captured.out == f'Welcome user "{user}". You are using version {version_nr} of this program!\n'
    
    def test_upper_encryption_letter(self):
        password = "password"
        assert upper_encryption(password) == "passwordR"

    def test_upper_encryption_number(self):
        password = "1p"
        assert upper_encryption(password) == "1p1"

    def test_swap_encryption_even(self):
        password = "password"
        assert swap_encryption(password) == "wordpass"
    
    def test_swap_encryption_uneven(self):
        password = "pass_word"
        assert swap_encryption(password) == "_wordpass"

    def test_add_to_list_existing(self):
        password = "password"
        password_list = [[2, "wordRpass"], [2, "second_password"]]
        expected_password_list = [[3, "wordRpass"], [2, "second_password"]]
        add_to_list(password, password_list)
        for index in range(len(password_list)):
            assert password_list[index] == expected_password_list[index]
    
    def test_add_to_list_unique(self):
        password = "password"
        password_list = [[2, "password"], [2, "second_password"]]
        expected_password_list = [[2, "password"], [2, "second_password"], [1, "wordRpass"]]
        add_to_list(password, password_list)
        for index in range(len(password_list)):
            assert password_list[index] == expected_password_list[index]
        

