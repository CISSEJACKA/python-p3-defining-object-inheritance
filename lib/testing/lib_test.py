# lib/testing/lib_test.py
import pytest
from lib.vehicle import Vehicle
from lib.car import Car

def test_vehicle():
    v = Vehicle("medium", 4)
    assert v.wheel_size == "medium"
    assert v.wheel_number == 4
    assert v.go() == "vrrrrrrrooom!"
    assert v.fill_up_tank() == "filling up!"

def test_car():
    c = Car("medium", 4)
    assert c.wheel_size == "medium"
    assert c.wheel_number == 4
    assert c.go() == "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
