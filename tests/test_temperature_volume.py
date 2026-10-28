import pytest

from converter.temperature_volume import convert_temperature, convert_volume


def test_celsius_to_fahrenheit_normal():
    assert convert_temperature(100, "C", "F") == pytest.approx(212)


def test_fahrenheit_to_celsius_normal():
    assert convert_temperature(32, "F", "C") == pytest.approx(0)


def test_absolute_zero_boundary():
    assert convert_temperature(-273.15, "C", "K") == pytest.approx(0)


def test_below_absolute_zero_raises_error():
    with pytest.raises(ValueError):
        convert_temperature(-300, "C", "F")


def test_litre_to_ml_normal():
    assert convert_volume(1.5, "l", "ml") == pytest.approx(1500)


def test_zero_volume_edge_case():
    assert convert_volume(0, "gallon", "l") == 0


def test_invalid_volume_unit_raises_error():
    with pytest.raises(ValueError):
        convert_volume(1, "l", "bucket")


def test_kelvin_to_fahrenheit_normal():
    assert convert_temperature(273.15, "K", "F") == pytest.approx(32)
