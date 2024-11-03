"""
Turns input target space into feature maps
"""

# Create density estimation for each timestep (PRIMARY SPATIAL FUNCTION FOR RL)

# NOT FOR THIS PROJECT UNLESS IT SPEEDS THINGS UP:
# Create fuzzy satellite octree (optional)
# Create particle flow model (optional)

# Create pre-computed spatial value or cost function of:
# - zero-mean corrected and zscaled density values in time (moving average?)
# - target covariance (avg, mean, max, sum)
# - target to sensor projected velocities
# - observation quality
# - orbital value potential (long/lat, gsd potential, overhead intel capacity,...)
# - satellite activity / differential filter (care about things that move a bunch or make frequent corrections/orbital plane updates)
# - [HARD FILTERS] access opps (simple range, simple lighting, simple KOZ (not including heavy stuff like spacecraft orientation based KOZ for gimbals))

# Note, runtime value and cost functions will be built in another module which will be dependent on action sequence taken