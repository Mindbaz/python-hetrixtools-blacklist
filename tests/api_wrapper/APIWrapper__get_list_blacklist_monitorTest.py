#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest
from unittest.mock import Mock, patch;
import requests;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__get_blacklist_monitorTest( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create results object wanted
        self.expected_object_simple = Mock();
        self.expected_object_simple.status_code = 200;
        self.expected_object_simple.json = Mock ( return_value = [
            [
                {
                    "ID": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "Type": "IPv4",
                    "Target": "1.2.3.4",
                    "Add_Date": 1633529168,
                    "Last_Check": 1663885135,
                    "Status": "Active",
                    "Label": "",
                    "Contact_List_ID": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "Blacklisted_Count": "0",
                    "Blacklisted_On": None,
                    "Links": {
                        "Report_Link": "https://hetrixtools.com/report/blacklist/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/",
                        "Whitelabel_Report_Link": ""
                    }
                },
                {
                    "ID": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                    "Type": "IPv4",
                    "Target": "1.2.3.5",
                    "Add_Date": 1633529168,
                    "Last_Check": 1663885008,
                    "Status": "Active",
                    "Label": "",
                    "Contact_List_ID": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "Blacklisted_Count": "0",
                    "Blacklisted_On": None,
                    "Links": {
                        "Report_Link": "https://hetrixtools.com/report/blacklist/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab/",
                        "Whitelabel_Report_Link": ""
                    }
                }
            ],
            {
                "Meta": {
                    "Total_Records": "2"
                },
                "Links": {
                    "Pages": {
                    }
                }
            }
        ] );
        self.expected_object_simple.ok = True;

        self.expected_object_error = Mock();
        self.expected_object_error.status_code = 400;
        self.expected_object_error.json = Mock ( return_value = [
            [ ],
            {
                "Meta": {
                    "Total_Records": "0"
                },
                "Links": {
                    "Pages": {
                    }
                }
            }
        ] );
        self.expected_object_error.ok = False;

    def test_get_blacklist_monitor_success ( self ):
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( 'requests.get' ) as patch_request_get:
            patch_request_get.return_value = self.expected_object_simple;
            returned_object = api_wrapper.get_list_blacklist_monitor();
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_get_blacklist_monitor_connection_error ( self ):
        ## Simulate connection problem
        import socket
        def guard ( *args, **kwargs ):
            raise requests.ConnectionError ( "Temporary failure in name resolution" )

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.get_list_blacklist_monitor ();
        self.assertEqual ( returned_object.status_code, 503 );

    def test_get_blacklist_monitor_connect_timeout ( self ):
        ## Simulate connection problem
        import socket
        def guard ( *args, **kwargs ):
            raise requests.ConnectTimeout ( "Temporary failure in name resolution" )

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.get_list_blacklist_monitor ();
        self.assertEqual ( returned_object.status_code, 503 );

    def test_get_blacklist_monitor_error ( self ):
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( 'requests.get' ) as patch_request_get:
            patch_request_get.return_value = self.expected_object_error;
            returned_object = api_wrapper.get_list_blacklist_monitor ();
        self.assertEqual ( self.expected_object_error, returned_object );


if __name__ == '__main__':
    unittest.main ();
