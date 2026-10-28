import pytest

from converter.length_weight import convert_length, convert_weight


def test_km_to_m_normal():
    assert convert_length(2, "km", "m") == 2000


def test_mile_to_km_normal():
    assert convert_length(1, "mile", "km") == pytest.approx(1.609344)


def test_zero_length_edge_case():
    assert convert_length(0, "m", "foot") == 0


def test_kg_to_lb_normal():
    assert convert_weight(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-4)


def test_same_unit_returns_same_value_edge_case():
    assert convert_weight(5, "g", "g") == pytest.approx(5)


def test_unknown_unit_raises_error():
    with pytest.raises(ValueError):
        convert_length(1, "m", "parsec")


def test_negative_weight_raises_error():
    with pytest.raises(ValueError):
        convert_weight(-1, "kg", "g")
