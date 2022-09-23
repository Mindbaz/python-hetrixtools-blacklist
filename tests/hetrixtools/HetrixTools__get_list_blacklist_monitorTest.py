#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest;
from unittest.mock import patch, Mock;

from hetrixtools_blacklist_api.hetrixtools import HetrixTools;
from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor, ResponseRBLEntry;
from hetrixtools_blacklist_api.models.hetrixtools_api_responses import APIResponseBlacklistMonitor;


class HetrixTools__get_list_blacklist_monitorTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Mock api returned object
        """Create Mock object"""
        self.expected_object_simple = Mock ();
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
        self.expected_object_simple.status_code = 200;

    def test_get_list_blacklist_monitor_default_params ( self ) -> None:
        instance = HetrixTools ( token_file_path = "dummy_file_path" );
        with patch ( 'hetrixtools_blacklist_api.api_wrapper.APIWrapper.get_list_blacklist_monitor' ) as api_wrapper_get_list_blacklist_monitor:
            ## Assign method return value to Mock object
            api_wrapper_get_list_blacklist_monitor.return_value = self.expected_object_simple;

            ## Create results object wanted
            list_object_expected = [ ];
            tmp_api_reponse = APIResponseBlacklistMonitor ( self.expected_object_simple.status_code, self.expected_object_simple.json () );
            list_object_expected.extend ( tmp_api_reponse.list_blacklist_monitor );

            ## Call the function to test
            list_blacklist_monitor = instance.get_list_blacklist_monitor ();

            ## Assert equal function
            self.assertListEqual ( list_blacklist_monitor, list_object_expected );


if __name__ == '__main__':
    unittest.main ()
