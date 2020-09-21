import os
import sys
import tables as tb
import pandas as pd

import invisible_cities.core.system_of_units  as units
from invisible_cities.io.mcinfo_io import load_mchits_df
from invisible_cities.io.mcinfo_io import load_mcparticles_df


def load_mc_hits(iFileName: str) -> pd.DataFrame :
    return load_mchits_df(iFileName)


def load_mc_particles(iFileName: str) -> pd.DataFrame :
    return load_mcparticles_df(iFileName)


def get_num_mc_particles(iFileName: str, evt_number: int) -> int :
    with tb.open_file(iFileName) as mcfile:
        evt_cond = 'event_id == ' + str(evt_number)
        return len(mcfile.root.MC.particles.get_where_list(evt_cond))


def get_primary_particles(iFileName: str) -> pd.DataFrame :
    
    parts = load_mc_particles(iFileName)

    return parts[parts.primary]



