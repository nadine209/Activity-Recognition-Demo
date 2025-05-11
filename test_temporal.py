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
    event_A = (100, 120)
    event_B = (90, 120)
    # Vérifie si la fin de A est égale à la fin de B et que le début de A est avant le début de B
    return self.event_A[1] == self.event_B[1] and self.event_A[0] < self.event_B[0]


def test_equals():
    event_A = (100, 120)
    event_B = (100, 120)
    allen = AllenTemporalLogic(event_A, event_B)
    assert allen.equals() is True

if __name__ == "__main__":
    pytest.main()

