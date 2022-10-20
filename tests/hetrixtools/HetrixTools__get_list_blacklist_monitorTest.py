#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import patch, Mock, call;

import requests

from hetrixtools_blacklist_api import utils
from hetrixtools_blacklist_api.hetrixtools import HetrixTools;
from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor, ResponseRBLEntry;
from hetrixtools_blacklist_api.models.hetrixtools_api_responses import APIResponseBlacklistMonitor;


class HetrixTools__get_list_blacklist_monitorTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Mock api returned object
        """Create Mock object"""
        self.expected_object_simple = requests.Response ();
        self.expected_object_simple._content = \
            b"""
        [
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
                    "Blacklisted_On": [],
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
                    "Blacklisted_On": [],
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
        ]
        """;
        self.expected_object_simple.status_code = 200;

        self.expected_object_not_success = requests.Response ();
        self.expected_object_not_success.status_code = 500;

        self.expected_object_success_malformed = requests.Response ();
        self.expected_object_success_malformed.status_code = 200;
        self.expected_object_success_malformed._content = \
            b"""
        [
            [],
            []
        ]
        """;

        self.expected_object_success_with_next_page = requests.Response ();
        self.expected_object_success_with_next_page.status_code = 200;
        self.expected_object_success_with_next_page._content = \
            b"""
        [
            [
                {
                    "ID": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "Type": "IPv4",
                    "Target": "1.2.3.4",
                    "Add_Date": 1633529168,
                    "Last_Check": 1663885008,
                    "Status": "Active",
                    "Label": "",
                    "Contact_List_ID": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "Blacklisted_Count": "0",
                    "Blacklisted_On": [],
                    "Links": {
                        "Report_Link": "https://hetrixtools.com/report/blacklist/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/",
                        "Whitelabel_Report_Link": ""
                    }
                }
            ],
            {
                "Meta": {
                    "Total_Records": "1"
                },
                "Links": {
                    "Pages": {
                        "Next": "dummy_page_next"
                    }
                }
            }
        ]
        """;

        self.expected_object_success_without_next_page = requests.Response ();
        self.expected_object_success_without_next_page.status_code = 200;
        self.expected_object_success_without_next_page._content = \
            b"""
        [
            [
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
                    "Blacklisted_On": [],
                    "Links": {
                        "Report_Link": "https://hetrixtools.com/report/blacklist/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab/",
                        "Whitelabel_Report_Link": ""
                    }
                }
            ],
            {
                "Meta": {
                    "Total_Records": "1"
                },
                "Links": {
                    "Pages": {
                    }
                }
            }
        ]
        """;

    def test_get_list_blacklist_monitor_default_params ( self ) -> None:
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get_list_blacklist_monitor", return_value = self.expected_object_simple ) as api_wrapper_get_list_blacklist_monitor:
            with patch ( "hetrixtools_blacklist_api.hetrixtools.is_success_hetrixtools_API_call_response", side_effect = utils.is_success_hetrixtools_API_call_response ) as is_success_hetrixtools_API_call_response:
                ## Create results object wanted
                list_object_expected = [ ];
                tmp_api_reponse = APIResponseBlacklistMonitor ( self.expected_object_simple.status_code, self.expected_object_simple.json () );
                list_object_expected.extend ( tmp_api_reponse.list_blacklist_monitor );

                ## Call the function to test
                list_blacklist_monitor = instance.get_list_blacklist_monitor ();

                api_wrapper_get_list_blacklist_monitor.assert_called_once_with (
                    page_number = 0,
                    result_per_page = 1024
                );
                is_success_hetrixtools_API_call_response.assert_called_once_with (
                    response = self.expected_object_simple
                )
                ## Assert equal function
                self.assertListEqual ( list_blacklist_monitor, list_object_expected );

    def test_not_success_API_call_response ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        list_object_expected = [];
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get_list_blacklist_monitor",
                     return_value = self.expected_object_not_success ) as api_wrapper_get_list_blacklist_monitor:
            with patch ( "hetrixtools_blacklist_api.hetrixtools.is_success_hetrixtools_API_call_response",
                         side_effect = utils.is_success_hetrixtools_API_call_response ) as is_success_hetrixtools_API_call_response:
                ## Call the function to test
                list_blacklist_monitor = instance.get_list_blacklist_monitor ();

                api_wrapper_get_list_blacklist_monitor.assert_called_once_with (
                    page_number = 0,
                    result_per_page = 1024
                );
                is_success_hetrixtools_API_call_response.assert_called_once_with (
                    response = self.expected_object_not_success
                )
                ## Assert equal function
                self.assertListEqual ( list_blacklist_monitor, list_object_expected );

    def test_not_success_API_call_malformed_response ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        list_object_expected = [];
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get_list_blacklist_monitor",
                     return_value = self.expected_object_success_malformed ) as api_wrapper_get_list_blacklist_monitor:
            with patch ( "hetrixtools_blacklist_api.hetrixtools.is_success_hetrixtools_API_call_response", side_effect = utils.is_success_hetrixtools_API_call_response ) as is_success_hetrixtools_API_call_response:
                ## Call the function to test
                list_blacklist_monitor = instance.get_list_blacklist_monitor ();

                api_wrapper_get_list_blacklist_monitor.assert_called_once_with (
                    page_number = 0,
                    result_per_page = 1024
                );
                is_success_hetrixtools_API_call_response.assert_called_once_with (
                    response = self.expected_object_success_malformed
                )
                ## Assert equal function
                self.assertListEqual ( list_blacklist_monitor, list_object_expected );

    def test_success_API_call_with_next_page ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        list_object_expected = [
            ResponseBlacklistMonitor ( self.expected_object_success_with_next_page.json () [ 0 ] [ 0 ] ),
            ResponseBlacklistMonitor ( self.expected_object_success_without_next_page.json () [ 0 ] [ 0 ] ),
        ];
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get",
                     side_effect = [ self.expected_object_success_with_next_page,
                                     self.expected_object_success_without_next_page ]) as api_wrapper_get:
            with patch ( "hetrixtools_blacklist_api.hetrixtools.is_success_hetrixtools_API_call_response",
                         side_effect = utils.is_success_hetrixtools_API_call_response ) as is_success_hetrixtools_API_call_response:
                ## Call the function to test
                list_blacklist_monitor = instance.get_list_blacklist_monitor ();

                api_wrapper_get.assert_has_calls ( [
                    call ( url = "https://api.hetrixtools.com/v2//blacklist/monitors/0/1024/" ),
                    call ( url = "dummy_page_next" )
                ] )
                is_success_hetrixtools_API_call_response.assert_has_calls (
                    [
                        call ( response = self.expected_object_success_with_next_page ),
                        call ( response = self.expected_object_success_without_next_page )
                    ]
                )
                ## Assert equal function
                self.assertListEqual ( list_blacklist_monitor, list_object_expected );

    def test_success_API_call_with_next_page_malformed ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        list_object_expected = [
            ResponseBlacklistMonitor ( self.expected_object_success_with_next_page.json () [ 0 ] [ 0 ] )
        ];
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get",
                     side_effect = [ self.expected_object_success_with_next_page,
                                     self.expected_object_success_malformed ] ) as api_wrapper_get:
            with patch ( "hetrixtools_blacklist_api.hetrixtools.is_success_hetrixtools_API_call_response",
                         side_effect = utils.is_success_hetrixtools_API_call_response ) as is_success_hetrixtools_API_call_response:
                ## Call the function to test
                list_blacklist_monitor = instance.get_list_blacklist_monitor ();

                api_wrapper_get.assert_has_calls ( [
                    call ( url = "https://api.hetrixtools.com/v2//blacklist/monitors/0/1024/"),
                    call ( url = "dummy_page_next" ) ] )

                is_success_hetrixtools_API_call_response.assert_has_calls (
                    [
                        call ( response = self.expected_object_success_with_next_page ),
                        call ( response = self.expected_object_success_malformed )
                    ]
                )
                ## Assert equal function
                self.assertListEqual ( list_blacklist_monitor, list_object_expected );

    def test_success_API_call_with_next_page_error ( self ):
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        list_object_expected = [
            ResponseBlacklistMonitor ( self.expected_object_success_with_next_page.json () [ 0 ] [ 0 ] )
        ];
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get",
                     side_effect = [ self.expected_object_success_with_next_page,
                                     self.expected_object_not_success ] ) as api_wrapper_get:
            with patch ( "hetrixtools_blacklist_api.hetrixtools.is_success_hetrixtools_API_call_response",
                         side_effect = utils.is_success_hetrixtools_API_call_response ) as is_success_hetrixtools_API_call_response:
                ## Call the function to test
                list_blacklist_monitor = instance.get_list_blacklist_monitor ();

                api_wrapper_get.assert_has_calls ( [
                    call ( url = "https://api.hetrixtools.com/v2//blacklist/monitors/0/1024/"),
                    call ( url = "dummy_page_next" ) ] )

                is_success_hetrixtools_API_call_response.assert_has_calls (
                    [
                        call ( response = self.expected_object_success_with_next_page ),
                        call ( response = self.expected_object_not_success )
                    ]
                )
                ## Assert equal function
                self.assertListEqual ( list_blacklist_monitor, list_object_expected );


if __name__ == "__main__":
    unittest.main ()
