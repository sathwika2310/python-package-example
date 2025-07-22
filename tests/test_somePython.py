# tests/test_somePython.py

from myPackage import somePython

def test_freezing_point():
    assert somePython.fahr_to_kelvin(32) == 273.15

def test_boiling_point():
    assert round(somePython.fahr_to_kelvin(212), 2) == 373.15

def test_negative_temp():
    assert round(somePython.fahr_to_kelvin(-40), 2) == 233.15

