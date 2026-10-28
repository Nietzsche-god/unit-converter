TEMPERATURE_UNITS = {"C", "F", "K"}

VOLUME_TO_LITRE = {
    "l": 1.0,
    "ml": 0.001,
    "gallon": 3.785411784,  # US gallon
    "cup": 0.2365882365,    # US cup
}

ABSOLUTE_ZERO_C = -273.15


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between Celsius (C), Fahrenheit (F) and Kelvin (K)."""
    if from_unit not in TEMPERATURE_UNITS or to_unit not in TEMPERATURE_UNITS:
        raise ValueError(f"Unsupported temperature unit: {from_unit!r} -> {to_unit!r}")

    # Convert to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < ABSOLUTE_ZERO_C - 1e-9:
        raise ValueError("Temperature cannot be below absolute zero")

    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


def convert_volume(value, from_unit, to_unit):
    """Convert a volume between supported units."""
    if from_unit not in VOLUME_TO_LITRE or to_unit not in VOLUME_TO_LITRE:
        raise ValueError(f"Unsupported volume unit: {from_unit!r} -> {to_unit!r}")
    if value < 0:
        raise ValueError("Volume cannot be negative")
    return value * VOLUME_TO_LITRE[from_unit] / VOLUME_TO_LITRE[to_unit]
