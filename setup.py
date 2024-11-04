from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
root = Path(__file__).parent
readme = (root / "README.md").read_text()
license = (root / "LICENSE").read_bytes().decode('utf-8')

setup(
    name='oculicaeli',
    version='0.1.0',
    description="This project implements 'Distributed Space-Based Telescope Tasking for Space Situational Awareness via the Apparent Spacecraft Density Heuristic', an approach developed for my Adv. Data Science course at Colorado School of Mines. Emphasis is placed on visualizing spacecraft densities from various observers in arbitrary orbits, and leverages both traditional ML, path planning (RRT*), and PPO Reinforcement Learning methods to develop telescope schedules.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Ryan Hartzell',
    author_email='rhartzell46@gmail.com',
    url='https://github.com/RyanHartzell/oculicaeli',
    license=license,
    packages=find_packages(include=['oculicaeli'])
)