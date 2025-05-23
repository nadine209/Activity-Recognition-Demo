# test_temporal.py
import pytest
from temporal_rules_advanced import AllenTemporalLogic

def test_before():
    event_A = (100, 120)
    event_B = (121, 150)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.before() is True

def test_meets():
    event_A = (100, 120)
    event_B = (120, 150)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.meets() is True

def test_overlaps():
    event_A = (100, 130)
    event_B = (120, 150)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.overlaps() is True

def test_starts():
    event_A = (100, 120)
    event_B = (100, 150)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.starts() is True

def test_during():
    event_A = (110, 120)
    event_B = (100, 150)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.during() is True

def test_finishes():
    event_A = (100, 120)  # event_A commence à 100 et finit à 120
    event_B = (120, 130)  # event_B commence exactement à la fin de event_A
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.finishes() is True  # Maintenant, A finit exactement au début de B


def test_equals():
    event_A = (100, 120)
    event_B = (100, 120)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.equals() is True

if __name__ == "__main__":
    pytest.main()

# pytest test_temporal.py

