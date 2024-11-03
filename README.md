# Kernel-Density-Based Deep Multi-Agent Reinforcement Learning for Space Telescope Tasking
*The name means 'eyes of the sky' in Latin... as far as I know.*

## Ryan Hartzell - Robotics MS Student @ Colorado School of Mines
## CSCI 598 - Advanced Data Science & CSCI 568 - Distributed Systems

### Overview
This will be my first attempt at a (at least sub-optimal) tasking framework for space-based SDA sensors. Specifically, I will be building utilities for computing various domain-relevant value (Q?) functions and cost (regret?) functions. The initial project will implement utilities for loading large amounts of TLE (orbital parameters) for all known space objects (RSOs), constructing density maps, arbitrary feature maps, and plotting/viz utilities. The initial algorithm is intended to be centralized as proof-of-concept, and an extension will be made to support decentralized tasking. This will include literature review and adaptation of the global optimization problem into a distributed (localized) optimization problem with periodic updates of the known "global" views of target space. Both the centralized case and decentralized case are intended to operate under the assumption of a dynamic, time-variant environment. In other words, the density of all spacecraft projected into the unit sphere about any given observer, as well as boolean access opportunity criteria, will change as time progresses.


Flow

- Load all objects (orbital, astroutines)
- Propagate across time window, WITH UNCERTAINTY (optional) (orbital, astroutines, GMAT?)
- Construct host frames (bildkedde and/or scipy)
- Construct basic projective sensor model (bildkedde)
- Project simply onto ra/dec or az/el unit sphere with respect to each observer frame (pick LHLV and compare to one fixed with respect to the Earth pole)
    * Bildkedde? Also potentially a new function in astroutines
- Either way, fit a BallTree (and RandomForest) to points (density)
- Generate density either as approximate (circle) or as direct (query circle superscribing FOV, then project corresponding sats to FPA and trim the edges)
    * Query tools in density
- Viz
    - Show change over time
    - Show change given different time-steps
    - Show different time windows and altitude cutoffs
    - Show with range constraint, brightness constraint, KOZ about earth, sun, moon
    - Compare all sensor density fields
- Do supppper basic A* or D* to pick the best targeting sequence per sensor under sets of constraints (no overlap, slew cost (weighted haversine/great circle distance), handle simultaneous obs, population observation statistics should be stable)
    * Try with various numbers of sensors in a constellation, all at same altitude or various altitudes.
    * Explore LEO only case... changes are RAPID so should be kinda cool...
- Construct additional features
    * Covariance (approx. we can just set it equal to sensor noise convolution with delta at actual location rather than the true observation update function with the Jacobian in ra/dec...)
    * Relative velocity in FOV/image space distribution!!! Why? Need to track on objects for good signal, and objects not tracked well in an FOV will smear
    
OPTIONAL!!! Starts to get into computational project
- Construct time-varying model of density spatially and see if we can predict it without trees at every time step...
    - Represent as a differential field, try to fit a global dynamics model to it
    - Graph based representation? W/ convolution for density weighting with arbitrary features of neighbor nodes at each query point
    - KDE plus Gaussian Process plus Markov Decision Process?
    - Fluid dynamics model of spacecraft motion???? This could be fun... same with other particle models
