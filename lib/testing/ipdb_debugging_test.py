#!/usr/bin/env python3

import ipdb
from lib.ipdb_debugging import plus_two

def test_adds_two():
    '''adds_two() adds 2 to input arg and returns sum.'''
    ipdb.set_trace() 
    assert plus_two(3) == 5
