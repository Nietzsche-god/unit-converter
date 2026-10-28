"""Feature A: length and weight conversion."""

# Factors to a base unit (metre for length, kilogram for weight)
LENGTH_TO_METRE = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mile": 1609.344,
    "foot": 0.3048,
    "inch": 0.0254,
}

WEIGHT_TO_KG = {
    "kg": 1.0,
    "g": 0.001,
    "lb": 0.45359237,
    "oz": 0.028349523125,
}


def _convert(value, from_unit, to_unit, table, kind):
    if from_unit not in table or to_unit not in table:
        raise ValueError(f"Unsupported {kind} unit: {from_unit!r} -> {to_unit!r}")
    if value < 0:
        raise ValueError(f"{kind.capitalize()} cannot be negative")
    return value * table[from_unit] / table[to_unit]


def convert_length(value, from_unit, to_unit):
    """Convert a length between supported units."""
    return _convert(value, from_unit, to_unit, LENGTH_TO_METRE, "length")


def convert_weight(value, from_unit, to_unit):
    """Convert a weight between supported units."""
    return _convert(value, from_unit, to_unit, WEIGHT_TO_KG, "weight")
