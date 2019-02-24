from kostiP.kosti import *


def test_calculate_luck_level1():
    assert calculate_luck_level(20,4,6,8,2) == 0


def test_calculate_luck_level2():
    assert calculate_luck_level(24,6,4,7,3) == 4


def test_output_luck_level1():
    assert output_luck_level(0) == "Ты угадал! Круто!"


def test_output_level2():
    assert output_luck_level(3) == "Ты был близко"


def test_output_level3():
    assert output_luck_level(4) == "Не угадал :с"
