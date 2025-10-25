#!/usr/bin/env python3
"""
Setup script for MazeSolver package
"""

from setuptools import setup, find_packages
import os


# Read the contents of README file
def read_file(filename):
    """Read file contents"""
    here = os.path.abspath(os.path.dirname(__file__))
    try:
        with open(os.path.join(here, filename), encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


# Package metadata
NAME = "maze-solver"
VERSION = "1.0.0"
DESCRIPTION = (
    "A comprehensive maze solving package with BFS algorithm and path visualization"
)
AUTHOR = "MazeSolver Developer"
AUTHOR_EMAIL = "developer@example.com"
URL = "https://github.com/yourusername/maze-solver"
LICENSE = "MIT"

# Long description from README
LONG_DESCRIPTION = read_file("README.md")
if not LONG_DESCRIPTION:
    LONG_DESCRIPTION = DESCRIPTION

# Required packages
REQUIRED = [
    # No external dependencies required
]

# Development dependencies
EXTRAS_REQUIRE = {
    "dev": [
        "pytest>=6.0",
        "pytest-cov>=2.0",
        "black>=21.0",
        "flake8>=3.8",
        "mypy>=0.800",
    ],
    "test": [
        "pytest>=6.0",
        "pytest-cov>=2.0",
    ],
}

# Classifiers
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Games/Entertainment :: Puzzle Games",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Operating System :: OS Independent",
]

# Keywords
KEYWORDS = [
    "maze",
    "solver",
    "bfs",
    "pathfinding",
    "algorithm",
    "visualization",
    "puzzle",
    "game",
    "graph",
    "search",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    # Package information
    packages=find_packages(),
    package_data={
        "maze_solver": ["*.py"],
    },
    include_package_data=True,
    # Dependencies
    install_requires=REQUIRED,
    extras_require=EXTRAS_REQUIRE,
    # Python version requirement
    python_requires=">=3.7",
    # Entry points for command line interface
    entry_points={
        "console_scripts": [
            "maze-solver-demo=maze_solver:demo",
        ],
    },
    # Metadata
    classifiers=CLASSIFIERS,
    keywords=" ".join(KEYWORDS),
    # Additional metadata
    project_urls={
        "Bug Reports": f"{URL}/issues",
        "Source": URL,
        "Documentation": f"{URL}#readme",
    },
    # Test configuration
    test_suite="tests",
    # Zip safe
    zip_safe=False,
)
