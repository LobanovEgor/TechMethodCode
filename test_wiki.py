import pytest
import Wiki


def test_yes():
    yes = ['Да', 'ДА', 'да', 'Yes', 'YES', 'yes']
    assert Wiki.answer in yes