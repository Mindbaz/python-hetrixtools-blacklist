#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest;
from unittest.mock import Mock;

from hetrixtools_blacklist_api.models.responses import ResponseRBLEntry;


class ResponseRBLEntry__constructorTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create parameters passed
        self.dummy_param_simple = {
            'RBL': "dummy_rbl.com",
            'Delist': "dummy_rbl.com/delist"
        }
        self.dummy_param_simple_2 = {
            'RBL': "dummy_rbl_2.com",
            'Delist': "dummy_rbl_2.com/delist"
        }
        self.dummy_param_incomplete = {
            'Delist': "dummy_rbl_2.com/delist"
        }

        ## Create results object wanted
        self.expected_object_simple = Mock ();
        self.expected_object_simple.delist_url = self.dummy_param_simple.get ( 'Delist' );
        self.expected_object_simple.rbl_source = self.dummy_param_simple.get ( 'RBL' );
        self.expected_object_simple_str = f"\tdelist_url = {self.expected_object_simple.delist_url}\n" \
                                      + f"\trbl_source = {self.expected_object_simple.rbl_source}\n"

    def test_constructor_success ( self ):
        response_rbl_entry = ResponseRBLEntry ( self.dummy_param_simple );
        self.assertEqual ( self.expected_object_simple, response_rbl_entry );

    def test_str ( self ):
        response_rbl_entry = ResponseRBLEntry ( self.dummy_param_simple );
        self.assertEqual ( self.expected_object_simple_str, str ( response_rbl_entry ) );

    def test_eq_none ( self ):
        response_rbl_entry_simple = ResponseRBLEntry ( self.dummy_param_simple );
        self.assertNotEqual ( None, response_rbl_entry_simple );

    def test_eq_not_equal ( self ):
        response_rbl_entry_simple = ResponseRBLEntry ( self.dummy_param_simple );
        response_rbl_entry_simple_2 = ResponseRBLEntry ( self.dummy_param_simple_2 );

        self.assertNotEqual ( response_rbl_entry_simple, response_rbl_entry_simple_2 );


if __name__ == '__main__':
    unittest.main ();
