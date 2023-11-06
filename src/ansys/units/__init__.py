"""Pyunits is a pythonic interface for units, unit systems, and unit conversions."""


import os

from ansys.units._constants import (  # noqa: F401
    _api_quantity_map,
    _base_units,
    _derived_units,
    _multipliers,
    _QuantityType,
    _unit_systems,
)
from ansys.units._version import __version__  # noqa: F401
from ansys.units.base_dimensions import BaseDimensions
from ansys.units.dimensions import Dimensions, DimensionsError  # noqa: F401
from ansys.units.map import QuantityMap, QuantityMapError  # noqa: F401
from ansys.units.quantity import Quantity, QuantityError  # noqa: F401
from ansys.units.systems import UnitSystem, UnitSystemError  # noqa: F401
from ansys.units.unit import Unit, UnitError  # noqa: F401
from ansys.units.unit_registry import UnitRegistry  # noqa: F401

_THIS_DIRNAME = os.path.dirname(__file__)
_README_FILE = os.path.normpath(os.path.join(_THIS_DIRNAME, "docs", "README.rst"))

if os.path.exists(_README_FILE):
    with open(_README_FILE, encoding="utf8") as f:
        __doc__ = f.read()
