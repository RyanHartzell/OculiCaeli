"""
Contains all imaging science routines.

Should implement my PerspectiveCamera model here, or import Bildkedde as a dependency... :)
"""

APPARENT_VISUAL_MAGNITUDE_SUN = -24.73 # Double check....

# Assume ECI
# Use bildkedde as model
class PerspectiveCamera:
    def __init__(self, transform) -> None:
        self.world2cam = transform # Homogeneous transform which converts from world to camera origin and orientation

    def __matmul__(self, other):
        self.world2cam = self.world2cam @ other

    def transform(self, H):
        # H must be a homogeneous transformation matrix aka numpy array (4,4)
        pass

    def look_at(self, pos, mode='world'):
        # If pos is a 3 vector, it is Cartesian position in world frame
        # Basically just do the Rodiriguez and get the rotation matrix using the cross of old and new boresight vector [+Z]
        pass

    def observe(targets):
        # This project all target positions to the boresight frame (bx, by)
        # but only returns those which actually fall within the circular or rectangular FOV
        pass

    def _project_to_boresight(self, pos):
        # Target states should be pos (N,3) and this function returns (bx,by) coordinates in
        pass

class Constraints:
    pass

class Observer:
    def __init__(self, sensor, ephemeris, constraints) -> None:
        self.sensor = sensor # This is a perspective camera
        self.ephemeris = ephemeris # This is the set of state vectors in time which this Observer follows through the world frame [ECI]
        self.constraints = constraints # Dictionary of all known constraints. This will become a standard object with json schema for ease of use

def solar_phase_angle():
    # Use skyfield for this
    pass

def calculate_apparent_aperture_referred_in_band_irradiance():
    # Lumos isn't stable apparently, so just homebrew instead
    pass

def calculate_apparent_visual_magnitude(irrad, ref=APPARENT_VISUAL_MAGNITUDE_SUN):
    pass