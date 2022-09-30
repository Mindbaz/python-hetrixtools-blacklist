#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import patch

from hetrixtools_blacklist_api.hetrixtools import HetrixTools


class APIMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'APIMock : __init__' );
        pass;


class HetrixTools__constructorTest ( unittest.TestCase ):
    def test_constructor_default ( self ):
        with patch ( 'hetrixtools_blacklist_api.hetrixtools.APIWrapper', side_effect = APIMock ) as api_wrapper:
            token_file_path = "dummy_file_path";
            instance = HetrixTools ( token_file_path = token_file_path );
            api_wrapper.assert_called_once_with (
                token_file_path = token_file_path,
                use_relay_endpoint = False,
                verbose = False
            )
            self.assertTrue ( isinstance ( instance._HetrixTools__api, APIMock ) );

    def test_constructor_not_default ( self ):
        expected_verbose = True;
        expected_use_relay_endpoint = True;
        with patch ( 'hetrixtools_blacklist_api.hetrixtools.APIWrapper', side_effect = APIMock ) as api_wrapper:
            token_file_path = "dummy_file_path";
            instance = HetrixTools ( token_file_path = token_file_path, verbose = expected_verbose, use_relay_endpoint = expected_use_relay_endpoint );
            api_wrapper.assert_called_once_with (
                token_file_path = token_file_path,
                use_relay_endpoint = expected_use_relay_endpoint,
                verbose = expected_verbose
            )
            self.assertTrue ( isinstance ( instance._HetrixTools__api, APIMock ) );

    def test_api_property ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        self.assertEqual ( instance.api, instance._HetrixTools__api );


if __name__ == "__main__":
    unittest.main ();
