"""Sarla Aviation OEW method -- ADDITIVE shim, installed by sarla.weights.rcaide_adapter.install_into_rcaide().

This directory is NOT part of upstream RCAIDE. It exists so the method is reachable by RCAIDE's
importlib dispatch (and therefore from the GUI, which imports RCAIDE and cannot see `sarla`).
The physics lives in `sarla/weights/`; this is a re-export and nothing else.
"""
from .compute_operating_empty_weight import compute_operating_empty_weight
