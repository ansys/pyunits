"""Pyunits is a pythonic interface for units, unit systems, and unit conversions."""
import os

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__.replace(".", "-"))


from ansys.units.dimensions import Dimensions, DimensionsError  # noqa: F401
from ansys.units.map import QuantityMap, QuantityMapError  # noqa: F401
from ansys.units.quantity import Quantity, QuantityError  # noqa: F401
from ansys.units.systems import UnitSystem, UnitSystemError  # noqa: F401
from ansys.units.tables import UnitsTable  # noqa: F401

_THIS_DIRNAME = os.path.dirname(__file__)
_README_FILE = os.path.normpath(os.path.join(_THIS_DIRNAME, "docs", "README.rst"))

if os.path.exists(_README_FILE):
    with open(_README_FILE, encoding="utf8") as f:
        __doc__ = f.read()
