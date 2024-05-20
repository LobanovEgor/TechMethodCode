import pytest
from Code import Wiki


def test_yes():
    yes = ['Да', 'ДА', 'да', 'Yes', 'YES', 'yes']
    answer = 'yes'
    assert answer in yes