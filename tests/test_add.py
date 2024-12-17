import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import add


def test_add():
    assert add(1, 2) == 3


def test_add_broken():
    assert add(1, 2) == 4
