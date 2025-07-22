# tests/test_somePython.py

from mypackage import somePython

def test_freezing_point():
    assert somePython.fahrToKelv(32) == 273.15

def test_boiling_point():
    assert round(somePython.fahrToKelv(212), 2) == 373.15

def test_negative_temp():
    assert round(somePython.fahrToKelv(-40), 2) == 233.15

