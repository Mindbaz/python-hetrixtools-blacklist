#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

        self.expected_object_error = Mock ();
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

    def test_get_blacklist_monitor_success_default_param ( self ):
        expected_page_number = 0;
        expected_per_page = 1024;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get", return_value = self.expected_object_simple ) as patch_request_get:
            returned_object = api_wrapper.get_list_blacklist_monitor ();
            patch_request_get.assert_called_once_with (
                url = "https://api.hetrixtools.com/v2//blacklist/monitors/{}/{}/"
                .format ( expected_page_number, expected_per_page )
            );
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_get_blacklist_monitor_success_not_default_param ( self ):
        """API Instance"""
        expected_page_number = 1;
        expected_per_page = 666;
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get", return_value = self.expected_object_simple ) as get:
            returned_object = api_wrapper.get_list_blacklist_monitor (
                page_number = expected_page_number,
                result_per_page = expected_per_page
            );
            get.assert_called_once_with (
                url = "https://api.hetrixtools.com/v2//blacklist/monitors/{}/{}/"
                .format ( expected_page_number, expected_per_page )
            );
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_get_blacklist_monitor_error ( self ):
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get", return_value = self.expected_object_error ) as get:
            returned_object = api_wrapper.get_list_blacklist_monitor ();
            get.assert_called_once_with (
                url = "https://api.hetrixtools.com/v2//blacklist/monitors/0/1024/"
            );
        self.assertEqual ( self.expected_object_error, returned_object );


if __name__ == "__main__":
    unittest.main ();
