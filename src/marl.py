"""
This module should contain all pytorch RL code

Must be able to ingest heuristic values over environment
Must be able to initialize agents (N=5 telescopes, variety of orbits, identical capabilities (homogeneous))
    - Centralized RL strategy
    - All agents have knowledge of global map
    - This is ground-system software

Given assumptions/constraints on:
    - Collection type (only ideal tracking aka commanded target rate track)
    - slew rate (fixed)
    - slew upper bound (worst case pi radians to reverse pointing)
    - access to targets
        * KOZ for Earth, Moon, Sun
        * Range (Neighborhood)
        * Target brightness (target brightness (vMag) > SNR_Thresh_Hyperparameter * minimum detectable irrad (vMag))
    - Optional: target tracking limit (relative velocity on focal plane cannot be higher than coarse/fine slew rate)
    - Time window (build target schedule over next hour)
    - Integration time
        * constant?
        * scale inversely with vMag of target?

Heuristic (might include in reward?)
    - Spatial Density of Accessible Targets
    - Optional: Fake target value/importance?

Reward (incentive sets of actions which...)
    - Number of simultaneous observations (bonus targets sensed in a given field of view)
    - maximize overall target revisit frequency
    - maximize overall information gain (covariance minimization)
    - (imaging duration * #actions) / schedule duration  (given maximum number of possible actions)
    - targeting diversity (value getting observations from different sensors)

Penalty (penalize actions which...)
    - * Optional: Imaging operation quality (prefer tracking objects that are at a low relative velocity?)
    - Total slew (haversine) over trajectory
    - Percentage of accessible objects in catalog not seen at all (normalized by access % of schedule duration)

Run on 5 hour chunks of information on all satellites in catalog, precompute access opportunities, over a week or so of TLEs
Validate learnt policies on unseen time window of about 8 hours
Plot trajectories (schedules) over movie of environment from each telescope's perspective
Show all integrated metrics and quality measures for each plan (sensor centric, target centric)

"""