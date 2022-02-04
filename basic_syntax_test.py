# TODO
# Implement tests for upper_encryption and swap_encryption

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
    
    def test_upper_encryption():
        pass