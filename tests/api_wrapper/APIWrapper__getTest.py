#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock, patch;
import requests;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__getTest( unittest.TestCase ):
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

    def test_get_success_without_param ( self ):
        expected_url = "https://api.hetrixtools.com/v1//contacts/";
        expected_params = None;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "requests.get", return_value = self.expected_object_simple ) as request_get:
            returned_object = api_wrapper.get ( url = expected_url );
            request_get.assert_called_once_with (
                url = expected_url,
                params = expected_params
            );
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_get_success_with_param ( self ):
        expected_url = "https://api.hetrixtools.com/v1//contacts/";
        expected_params = {
            "dummy_key": "dummy_value",
            "dummy_number": 666
        };
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "requests.get", return_value = self.expected_object_simple ) as request_get:
            returned_object = api_wrapper.get (
                url = expected_url,
                params = expected_params
            );
            request_get.assert_called_once_with (
                url = expected_url,
                params = expected_params
            );
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_get_blacklist_monitor_connection_error ( self ):
        expected_url = "https://api.hetrixtools.com/v1//contacts/";
        expected_params = None;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "requests.get", side_effect = requests.ConnectionError ( "Temporary failure in name resolution" ) ) as request_get:
            returned_object = api_wrapper.get ( url = expected_url );
            request_get.assert_called_once_with (
                url = expected_url,
                params = expected_params
            );
        self.assertEqual ( returned_object.status_code, 503 );

    def test_get_blacklist_monitor_connect_timeout ( self ):
        expected_url = "https://api.hetrixtools.com/v1//contacts/";
        expected_params = None;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "requests.get", side_effect = requests.ConnectTimeout ( "Temporary failure in name resolution" ) ) as request_get:
            returned_object = api_wrapper.get ( url = expected_url );
            request_get.assert_called_once_with (
                url = expected_url,
                params = expected_params
            );
        self.assertEqual ( returned_object.status_code, 503 );


if __name__ == "__main__":
    unittest.main ();
