# TODO

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
