instrument = {
        "freqs"         : "Range of frequencies of filterbank in Hertz.",
        "R"             : "Resolving power f / df.",
        "eta_inst"      : "Efficiency of entire chip.",
        "f_sample"      : "Readout frequency in Hertz.",
        }

telescope = {
        "Dtel"          : "Diameter of telescope in meters.",
        "Ttel"          : "Temperature of telescope in Kelvin.",
        "Tgnd"          : "Temperature of ground around telescope in Kelvin.",
        "eta_ap"        : "Aperture efficiency of telescope, as function of instrument frequencies. If a single number is given, assume same aperture efficiency across entire frequency range.",
        "eta_mir"       : "Mirror efficiency.",
        "eta_fwd"       : "Front-to-back efficiency.",
        "chop_mode"     : "Whether to chop (True) or not (False).",
        "f_chop"        : "Chopping frequency in Hertz (ignored if chop_mode = False).",
        "dAz_chop"      : "Angular separation between chopping paths (ignored if chop_mode = False).",
        }

atmosphere = {
        "Tatm"          : "Temperature of atmosphere in Kelvin.",
        "filename"      : "Name of file containing ARIS screen.",
        "path"          : "Path to ARIS file",
        "dx"            : "Gridsize of ARIS screen along x-axis in meter.",
        "dy"            : "Gridsize of ARIS screen along y-axis in meter.",
        "h_column"      : "Reference height of atmospheric column.",
        "v_wind"        : "Windspeed in meters per second.",
        "PWV0"          : "Mean PWV value in millimeters.",
        }

source = {
        "backend"       : "Choose astronomical source: MockSZ for tSZ and kSZ simulations, GalSpec for sub-mm galaxies (not yet implemented).",
        "Az"            : "Azimuthal extent of source map in degrees.",
        "El"            : "Elevation extent of source map in degrees.",
        # MockSZ specific
        "Te"            : "Electron temperature of cluster gas in Kelvin.",
        "ne0"           : "Central electron density in # per square centimeter.",
        "beta"          : "Isothermal-beta structure coefficient.",
        "v_pec"         : "Peculiar cluster velocity, relative to CMB, in kilometers per second.",
        "rc"            : "Cluster core radius in kiloparsec.",
        "Da"            : "Angular diameter distance in megaparsec.",
        }

simparams = {
        "name_sim"      : "Name of simulation.",
        "t_obs"         : "Total observation time in seconds.",
        "nThreads"      : "Number of CPU threads to use.",
        "outDir"        : "Output directory of simulation. Automatically uses name_sim as name of file.",
        }
