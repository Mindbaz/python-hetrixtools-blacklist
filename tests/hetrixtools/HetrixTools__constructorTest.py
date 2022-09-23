#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest;

from hetrixtools_blacklist_api.hetrixtools import HetrixTools

class HetrixTools__constructorTest ( unittest.TestCase ):
    def test_good_constructor ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );

if __name__ == '__main__':
    unittest.main ();
