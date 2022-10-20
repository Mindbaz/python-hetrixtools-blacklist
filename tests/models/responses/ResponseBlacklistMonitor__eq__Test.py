#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import Mock;

from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor, ResponseRBLEntry;


class ResponseBlacklistMonitor__eq__Test ( unittest.TestCase ):
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
        self.dummy_param_simple_2 = {
            "ID": 1,
            "Type": "IPv6",
            "Target": "1.2.3.4.5.6",
            "Add_Date": 1633529168,
            "Last_Check": 1663885135,
            "Status": "Active",
            "Label": "Dummy label",
            "Contact_List_ID": "00000000000000000000000000000000",
            "Blacklisted_Count": "0",
            "Blacklisted_On": [ ],
            "Links": {
                "Report_Link": "https://hetrixtools.com/report/blacklist/00000000000000000000000000000001/",
                "Whitelabel_Report_Link": ""
            }
        };

        ## Create results object wanted
        self.expected_object_simple_2 = Mock ();
        self.expected_object_simple_2.id = self.expected_object_simple_2.get ( "ID" );
        self.expected_object_simple_2.type = self.expected_object_simple_2.get ( "Type" );
        self.expected_object_simple_2.target = self.expected_object_simple_2.get ( "Target" );
        self.expected_object_simple_2.add_date = self.expected_object_simple_2.get ( "Add_Date" );
        self.expected_object_simple_2.last_check = self.expected_object_simple_2.get ( "Last_Check" );
        self.expected_object_simple_2.status = self.expected_object_simple_2.get ( "Status" );
        self.expected_object_simple_2.label = self.expected_object_simple_2.get ( "Label" );
        self.expected_object_simple_2.contact_list_id = self.expected_object_simple_2.get ( "Contact_List_ID" );
        self.expected_object_simple_2.blacklisted_count = self.expected_object_simple_2.get ( "Blacklisted_Count" );
        self.expected_object_simple_2.list_rbl_entry = [];
        self.expected_object_simple_2.report_link = self.expected_object_simple_2.get ( "Links" ).get ( "Report_Link" );

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
        ];
        self.expected_object_blacklisted_on.report_link = self.dummy_param_blacklisted_on.get ( "Links" ).get ( "Report_Link" );

        ## Create parameters passed
        self.dummy_param_blacklisted_on_modified = {
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
        self.expected_object_blacklisted_on_modified = Mock ();
        self.expected_object_blacklisted_on_modified.id = self.dummy_param_blacklisted_on_modified.get ( "ID" );
        self.expected_object_blacklisted_on_modified.type = self.dummy_param_blacklisted_on_modified.get ( "Type" );
        self.expected_object_blacklisted_on_modified.target = self.dummy_param_blacklisted_on_modified.get ( "Target" );
        self.expected_object_blacklisted_on_modified.add_date = self.dummy_param_blacklisted_on_modified.get ( "Add_Date" );
        self.expected_object_blacklisted_on_modified.last_check = self.dummy_param_blacklisted_on_modified.get ( "Last_Check" );
        self.expected_object_blacklisted_on_modified.status = self.dummy_param_blacklisted_on_modified.get ( "Status" );
        self.expected_object_blacklisted_on_modified.label = self.dummy_param_blacklisted_on_modified.get ( "Label" );
        self.expected_object_blacklisted_on_modified.contact_list_id = self.dummy_param_blacklisted_on_modified.get ( "Contact_List_ID" );
        self.expected_object_blacklisted_on_modified.blacklisted_count = self.dummy_param_blacklisted_on_modified.get ( "Blacklisted_Count" );
        self.expected_object_blacklisted_on_modified.list_rbl_entry = [
            ResponseRBLEntry ( self.dummy_param_blacklisted_on_modified.get ( "Blacklisted_On" ) [ 0 ] ),
        ];
        self.expected_object_blacklisted_on_modified.report_link = self.dummy_param_blacklisted_on_modified.get ( "Links" ).get ( "Report_Link" );


    def test_eq_none ( self ):
        response_rbl_entry_simple = ResponseBlacklistMonitor ( self.dummy_param_simple );
        self.assertNotEqual ( None, response_rbl_entry_simple );

    def test_eq_not_equal ( self ):
        response_rbl_entry_simple = ResponseBlacklistMonitor ( self.dummy_param_simple );
        response_rbl_entry_simple_2 = ResponseBlacklistMonitor ( self.dummy_param_simple_2 );

        self.assertNotEqual ( response_rbl_entry_simple, response_rbl_entry_simple_2 );

    def test_eq_rbl_entry_different_len ( self ):
        response_rbl_entry_simple = ResponseBlacklistMonitor ( self.dummy_param_simple );
        response_rbl_entry_blacklisted_on = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on );

        self.assertNotEqual ( response_rbl_entry_simple, response_rbl_entry_blacklisted_on );

    def test_eq_rbl_entry_different_content ( self ):
        response_rbl_entry_blacklisted_on = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on );
        response_rbl_entry_blacklisted_on_modified = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on_modified );

        self.assertNotEqual ( response_rbl_entry_blacklisted_on, response_rbl_entry_blacklisted_on_modified );

    def test_eq_rbl_entry_same_blacklisted_on ( self ):
        response_rbl_entry_blacklisted_on = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on );
        response_rbl_entry_blacklisted_on_copy = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on );

        self.assertEqual ( response_rbl_entry_blacklisted_on, response_rbl_entry_blacklisted_on_copy );

if __name__ == "__main__":
    unittest.main ();
