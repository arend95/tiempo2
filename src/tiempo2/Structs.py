"""!
@file
Structs that are passed to the C++ backend.
""" 

import ctypes
import numpy as np

class Instrument(ctypes.Structure):
    """!
    Struct representing the simulated instrument.
    """

    _fields_ = [("freqs", ctypes.POINTER(ctypes.c_double)),
                ("nfreqs", ctypes.c_int),
                ("R", ctypes.c_int),
                ("eta_inst", ctypes.c_double),
                ("freq_sample", ctypes.c_double)]

class Telescope(ctypes.Structure):
    """!
    Struct representing the simulated telescope.
    """

    _fields_ = [("Ttel", ctypes.c_double),
                ("Tgnd", ctypes.c_double),
                ("Dtel", ctypes.c_double),
                ("dAz_chop", ctypes.c_double),
                ("freq_chop", ctypes.c_double),
                ("eta_ap", ctypes.POINTER(ctypes.c_double)),
                ("eta_mir", ctypes.c_double),
                ("eta_fwd", ctypes.c_double)]

class Atmosphere(ctypes.Structure):
    """!
    Struct representing the simulated atmosphere.
    """

    _fields_ = [("Tatm", ctypes.c_double),
                ("h_column", ctypes.c_double),
                ("vel_w", ctypes.c_double),
                ("x_atm", ctypes.POINTER(ctypes.c_double)),
                ("y_atm", ctypes.POINTER(ctypes.c_double)),
                ("nx", ctypes.c_int),
                ("ny", ctypes.c_int),
                ("PWV", ctypes.POINTER(ctypes.c_double)),
                ("freqs_atm", ctypes.POINTER(ctypes.c_double)),
                ("nfreqs_atm", ctypes.c_int),
                ("PWV_atm", ctypes.POINTER(ctypes.c_double)),
                ("eta_atm", ctypes.POINTER(ctypes.c_double))]

class Source(ctypes.Structure):
    """!
    Struct representing simulated astronomical source.
    """

    _fields_ = [("Az", ctypes.POINTER(ctypes.c_double)),
                ("nAz", ctypes.c_int),
                ("El", ctypes.POINTER(ctypes.c_int)),
                ("nEl", ctypes.c_int),
                ("I_nu", ctypes.POINTER(ctypes.c_double))]

class SimParams(ctypes.Structure):
    """!
    Struct representing simulation parameters.
    """

    _fields_ = [("t_obs", ctypes.c_double),
                ("nThreads", ctypes.c_int)]
