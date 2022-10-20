#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import Mock;

from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor, ResponseRBLEntry;


class ResponseBlacklistMonitor__constructorTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create parameters passed
        self.dummy_param_simple = {
            "ID": 0,
            "Type": "IPv4",
            "Target": "1.2.3.4",
            "Add_Date": 1633529168,
            "Last_Check": 1663885135,
            "Status": "Active",
            "Label": "Dummy label",
            "Contact_List_ID": "00000000000000000000000000000000",
            "Blacklisted_Count": "0",
            "Blacklisted_On": [ ],
            "Links": {
                "Report_Link": "https://hetrixtools.com/report/blacklist/00000000000000000000000000000000/",
                "Whitelabel_Report_Link": ""
            }
        };

        ## Create results object wanted
        self.expected_object_simple = Mock ();
        self.expected_object_simple.id = self.dummy_param_simple.get ( "ID" );
        self.expected_object_simple.type = self.dummy_param_simple.get ( "Type" );
        self.expected_object_simple.target = self.dummy_param_simple.get ( "Target" );
        self.expected_object_simple.add_date = self.dummy_param_simple.get ( "Add_Date" );
        self.expected_object_simple.last_check = self.dummy_param_simple.get ( "Last_Check" );
        self.expected_object_simple.status = self.dummy_param_simple.get ( "Status" );
        self.expected_object_simple.label = self.dummy_param_simple.get ( "Label" );
        self.expected_object_simple.contact_list_id = self.dummy_param_simple.get ( "Contact_List_ID" );
        self.expected_object_simple.blacklisted_count = self.dummy_param_simple.get ( "Blacklisted_Count" );
        self.expected_object_simple.list_rbl_entry = [];
        self.expected_object_simple.report_link = self.dummy_param_simple.get ( "Links" ).get ( "Report_Link" );

        ## Create parameters passed
        self.dummy_param_blacklisted_on = {
            "ID": 1,
            "Type": "IPv4",
            "Target": "1.2.3.4",
            "Add_Date": 1633529168,
            "Last_Check": 1663885135,
            "Status": "Active",
            "Label": "Dummy label",
            "Contact_List_ID": "00000000000000000000000000000000",
            "Blacklisted_Count": "1",
            "Blacklisted_On": [
                {
                    "RBL": "multi.surbl.org",
                    "Delist": "http://www.surbl.org/surbl-analysis"
                },
                {
                    "RBL": "black.mail.abusix.zone",
                    "Delist": "https://www.abusix.ai/search?q=84.247.62.11"
                }
            ],
            "Links": {
                "Report_Link": "https://hetrixtools.com/report/blacklist/00000000000000000000000000000001/",
                "Whitelabel_Report_Link": ""
            }
        };

        ## Create results object wanted
        self.expected_object_blacklisted_on = Mock ();
        self.expected_object_blacklisted_on.id = self.dummy_param_blacklisted_on.get ( "ID" );
        self.expected_object_blacklisted_on.type = self.dummy_param_blacklisted_on.get ( "Type" );
        self.expected_object_blacklisted_on.target = self.dummy_param_blacklisted_on.get ( "Target" );
        self.expected_object_blacklisted_on.add_date = self.dummy_param_blacklisted_on.get ( "Add_Date" );
        self.expected_object_blacklisted_on.last_check = self.dummy_param_blacklisted_on.get ( "Last_Check" );
        self.expected_object_blacklisted_on.status = self.dummy_param_blacklisted_on.get ( "Status" );
        self.expected_object_blacklisted_on.label = self.dummy_param_blacklisted_on.get ( "Label" );
        self.expected_object_blacklisted_on.contact_list_id = self.dummy_param_blacklisted_on.get ( "Contact_List_ID" );
        self.expected_object_blacklisted_on.blacklisted_count = self.dummy_param_blacklisted_on.get ( "Blacklisted_Count" );
        self.expected_object_blacklisted_on.list_rbl_entry = [
            ResponseRBLEntry ( self.dummy_param_blacklisted_on.get ( "Blacklisted_On" ) [ 0 ] ),
            ResponseRBLEntry ( self.dummy_param_blacklisted_on.get ( "Blacklisted_On" ) [ 1 ] ),
        ];
        self.expected_object_blacklisted_on.report_link = self.dummy_param_blacklisted_on.get ( "Links" ).get ( "Report_Link" );

    def test_constructor_success ( self ):
        response_rbl_entry = ResponseBlacklistMonitor ( self.dummy_param_simple );
        self.assertEqual ( self.expected_object_simple, response_rbl_entry );

    def test_constructor_blacklist_on ( self ):
        response_rbl_entry = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on );
        self.assertEqual ( self.expected_object_blacklisted_on, response_rbl_entry );

if __name__ == "__main__":
    unittest.main ();
