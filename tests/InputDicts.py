"""!
@file
Template dictionaries for testing TiEMPO2 functionalities.
"""

import numpy as np

SZsource = {
        "type"          : "SZ",
        "Az"            : np.array([-1, 1]),
        "El"            : np.array([-1, 1]),
        "nAz"           : 10,
        "nEl"           : 10,
        "Te"            : 15, 
        "ne0"           : 1e-2,
        "beta"          : 0.6,
        "v_pec"         : 100,
        "rc"            : 116,
        "Da"            : 1500,
        "freqs"         : np.linspace(220, 440, 100)
        }

loadSZsource = {
        "type"          : "load",
        "filename"      : "test",
        "path"          : "."
        }

telescope = {
        "Dtel"          : 10,
        "Ttel"          : 300,
        "Tgnd"          : 280,
        "eta_ap"        : 0.7,
        "eta_mir"       : 0.99,
        "eta_fwd"       : 0.85,
        "f_chop"        : 30,
        "dAz_chop"      : 234
        }

instrument = {
        "freqs"         : np.linspace(220, 440, 10),
        "R"             : 300,
        "eta_inst"      : 0.4,
        "f_sample"      : 160
        }

atmosphere = {
        "Tatm"          : 293,
        "filename"      : "test",
        "path"          : "resources",
        "dx"            : 0.2,
        "dy"            : 0.2,
        "h_column"      : 1000,
        "v_wind"        : 4,
        "PWV0"          : 1
        }

observation = {
        "name_sim"      : "test_sim",
        "t_obs"         : 360,
        "nThreads"      : 1,
        "outDir"        : "."
        }
