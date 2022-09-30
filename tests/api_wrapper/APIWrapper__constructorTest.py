#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import patch, mock_open;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__constructorTest( unittest.TestCase ):
    def test_constructor ( self ):
        token_expected = "aaaaaaaaaaaaaabbaaaaaaaaaaaaaaaa";
        file_path = "dummy_file_path";
        with patch ( "hetrixtools_blacklist_api.utils.open", mock_open ( read_data = token_expected ), create = False ) as mock_file:
            api_wrapper = APIWrapper ( token_file_path = file_path );
        self.assertFalse ( api_wrapper.use_relay_endpoint );
        self.assertFalse ( api_wrapper.verbose );
        self.assertEqual ( api_wrapper.token, token_expected );
        self.assertEqual ( api_wrapper.endpoint_url, "https://api.hetrixtools.com/" );

    def test_file_not_exists ( self ):
        token_expected = "";
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        self.assertFalse ( api_wrapper.use_relay_endpoint );
        self.assertFalse ( api_wrapper.verbose );
        self.assertEqual ( api_wrapper.token, token_expected );
        self.assertEqual ( api_wrapper.endpoint_url, "https://api.hetrixtools.com/" );

    def test_use_relay_endpoint ( self ):
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path", use_relay_endpoint = True );
        self.assertTrue ( api_wrapper.use_relay_endpoint );
        self.assertEqual ( api_wrapper.endpoint_url, "https://relay.hetrixtools.com/api/" );

    def test_verbose_true ( self ):
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path", verbose = True );
        self.assertTrue ( api_wrapper.verbose );

    def test_token_property ( self ):
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        self.assertEqual ( api_wrapper.token, api_wrapper._APIWrapper__token );

    def test_endpoint_url_property ( self ):
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        self.assertEqual ( api_wrapper.endpoint_url, api_wrapper._APIWrapper__endpoint_url )

if __name__ == '__main__':
    unittest.main ();
