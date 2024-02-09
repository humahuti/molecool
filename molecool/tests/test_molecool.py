"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import sys
import numpy as np
import pytest

import molecool
from molecool.functions import calculate_distance



def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool" in sys.modules

def test_calculate_distance():
    """Makes sure to calc distance works"""
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    calculate_distance = molecool.calculate_distance(r1, r2)

    assert calculate_distance == 1

def  test_calc_right_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])
    
    # r_list = [(a,b) for a,b in [r1, r2, r3]]
    # a_list = []

    # for i,r in enumerate(r_list):
    #     a1 = calculate_distance(r_list[i])
    #     a_list.append(a1)

    expected_val = 90
    calc_val = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert expected_val == calc_val

# def test_molecular_mass():
#     symbols = ['C','H', 'H', 'H', 'H']
#     calc_mass = molecool
#     actual_mass = 16.04

#     assert pytest.approx(actual_mass, abs=1e-2) == molecool.calculate_molecular_mass(symbols)


@pytest.fixture
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])
    
    return symbols, coordinates

def test_build_bond_list(methane_molecule):
    # symbols, coordinates = methane_molecule

    coordinates = methane_molecule[-1]

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for atoms, bonds in bonds.items():
        assert bonds == 1.4

# def test_build_bond_list_failure(methane_molecule):
#     symbols, coordinates = methane_molecule
    
#     with pytest.raises(ValueError):
#         molecool.build_bond_list(coordinates, min_bond=-1)

def test_center_of_mass(methane_molecule):
    symbols, coordinates = methane_molecule

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])
    
    assert np.array_equal(center_of_mass, expected_center)