"""
Contains all utilities for density estimation
"""

import numpy as np

if __name__=="__main__":
    from imsci import *
else:
    from .imsci import *

from sklearn.neighbors import BallTree

# Apparent Spacecraft Density from a particular observer at time $t_o$
# Extends BallTree for ease of use.
class HeuristicMapper(BallTree):
    def __init__(self, targets, observer, scale_factor=3, leaf_size=40, sample_weight=None, **kwargs):
        # get targets' az/el values via observer
        elaz = observer.observe(targets)
        self.targets = targets # store these so we can calculate arbitrary features which go with the az/el positions
        
        super().__init__(elaz, leaf_size, "haversine", sample_weight, **kwargs)

        self.observer = observer

        # This will give a grid of shape (scale x 360 rows, scale x 180 columns)
        _AZ, _EL = np.meshgrid(np.linspace(-np.pi, np.pi, scale_factor*360//1),np.linspace(-np.pi/2, np.pi/2, scale_factor*180//1))
        self.grid = np.asarray([_EL.flat,_AZ.flat]) # Note EL,AZ ordering -> Needed format for Ball Tree
        print(self.grid.shape)

    # Produce density map in AZEL from query points
    def compute(self):
        # Queries every point in EL, AZ and stores array of ids at within observer FOV at each point
        # If constrained==True, then use constraints specified on observer to filter returned objects (range, lighting, Earth/Sun/Moon KOZ)
        # Ids can then be used to generate arbitrary heuristics which have a spatial dependency

        self.lut = self.query_radius([self._EL.flat,self._AZ.flat], np.max(self.observer.sensor.afov)/2) # Use half the maximum value of the afov as a superscribing circle
        return self

    # Uses pre-computed query record to generate any number of heuristics associated with ids
    def map(self, heuristic="density"):
        # Support various features associated with spacecraft IDs
        # Basic support for count and density, but distributions like relative velocity or average/max covariance will ultimately be supported
        # Can also pass in a heuristic/metric calculator function (callable)
        return

    def kde(self):
        return

if __name__=="__main__":
    import matplotlib.pyplot as plt
    scale = 3
    _AZ, _EL = np.meshgrid(np.linspace(-np.pi, np.pi, scale*360//1),np.linspace(-np.pi/2, np.pi/2, scale*180//1))

    # Set up target points (uniformly distributed over a sphere)
    az = np.random.uniform(-np.pi, np.pi, 100) 

    el = np.random.normal(0, np.pi/6, 100)
    el[el>(np.pi/2)] = np.pi/2
    el[el<(-np.pi/2)] = -np.pi/2 

    # Build tree
    tree = BallTree(np.c_[el.flat, az.flat], metric="haversine")

    # Compute kernel density (might be quicker than exactly computing...)
    kde = tree.kernel_density(np.c_[_EL.flat, _AZ.flat], h=0.5, kernel="gaussian")
    kde = kde.reshape(_AZ.shape)
    
    plt.imshow(kde, cmap='inferno')
    plt.show()
    
    # Note difference due to h parameter (bandwidth of kernel)
    kde = tree.kernel_density(np.c_[_EL.flat, _AZ.flat], h=0.05, kernel="gaussian")
    kde = kde.reshape(_AZ.shape)
    plt.imshow(kde, cmap='inferno')
    plt.show()

    # Should be able to plot hemispheres using polar plots too here, ideally with reference "circles" drawn for KOZ!!!
    def plot_polar():
        pass