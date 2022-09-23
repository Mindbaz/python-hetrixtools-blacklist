#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest;
from unittest.mock import patch, Mock;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__api_statusTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create results object wanted
        self.expected_object_simple = Mock ();
        self.expected_object_simple.status_code = 200;
        self.expected_object_simple.json = Mock ( return_value = {
            "Account_ID": "00000000000000000000000000000000",
            "API_Status": {
                "Max_API_Calls": 20000,
                "Remaining_API_Calls": 20000
            },
            "API_Blacklist_Check_Status": {
                "Monthly_API_Checks_From_Package": 5000,
                "Spent_API_Checks_This_Month": 0,
                "Extra_API_Checks_Available": 0,
                "Total_API_Checks_Left": 5000
            }
        } );
        self.expected_object_simple.ok = True;

    def test_api_status_success ( self ):
        """API Instance"""
        with patch ( 'requests.get' ) as patch_request_get:
            patch_request_get.return_value = self.expected_object_simple;
            api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
            returned_object = api_wrapper.api_status ();
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_api_status_connection_error ( self ):
        ## Simulate connection problem
        import socket, requests;
        def guard ( *args, **kwargs ):
            raise requests.ConnectionError ( "Temporary failure in name resolution" );

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.api_status ();
        self.assertEqual ( returned_object.status_code, 503 );

    def test_api_status_connect_timeout ( self ):
        ## Simulate connection problem
        import socket, requests;
        def guard ( *args, **kwargs ):
            raise requests.ConnectTimeout ( "Temporary failure in name resolution" );

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.api_status ();
        self.assertEqual ( returned_object.status_code, 503 );


if __name__ == '__main__':
    unittest.main ();
