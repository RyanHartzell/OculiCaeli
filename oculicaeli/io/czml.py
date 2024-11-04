"""
Based on the now archived :'( poliastro project's CZML reader/writer which leveraged CZML3
https://github.com/poliastro/poliastro/blob/main/src/poliastro/czml/extract_czml.py
"""

import czml3
from astropy import units as u
from astropy.time import Time, TimeDelta

# This should take in a CZML string which we can pack into a basic HTML string representation
def create_viewer(czml):
    pass

# This should take in a set of rvt ephemeris (raw numpy? astropy?) and a set of times
def ephem_to_czml(ephems, times):
    pass

# class ViewerInterface:
#     pass

class ViewerCZML:
    def __init__(self, rvt):
        pass
