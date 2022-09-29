#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import Mock;

from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor, ResponseRBLEntry;


class ResponseBlacklistMonitor__str__Test ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create parameters passed
        self.dummy_param_simple = {
            'ID': 0,
            'Type': "IPv4",
            'Target': "1.2.3.4",
            'Add_Date': 1633529168,
            'Last_Check': 1663885135,
            'Status': "Active",
            'Label': "Dummy label",
            'Contact_List_ID': "00000000000000000000000000000000",
            'Blacklisted_Count': "0",
            'Blacklisted_On': [ ],
            'Links': {
                "Report_Link": "https://hetrixtools.com/report/blacklist/00000000000000000000000000000000/",
                "Whitelabel_Report_Link": ""
            }
        };

        ## Create results object wanted
        self.expected_object_simple = Mock ();
        self.expected_object_simple.id = self.dummy_param_simple.get ( 'ID' );
        self.expected_object_simple.type = self.dummy_param_simple.get ( 'Type' );
        self.expected_object_simple.target = self.dummy_param_simple.get ( 'Target' );
        self.expected_object_simple.add_date = self.dummy_param_simple.get ( 'Add_Date' );
        self.expected_object_simple.last_check = self.dummy_param_simple.get ( 'Last_Check' );
        self.expected_object_simple.status = self.dummy_param_simple.get ( 'Status' );
        self.expected_object_simple.label = self.dummy_param_simple.get ( 'Label' );
        self.expected_object_simple.contact_list_id = self.dummy_param_simple.get ( 'Contact_List_ID' );
        self.expected_object_simple.blacklisted_count = self.dummy_param_simple.get ( 'Blacklisted_Count' );
        self.expected_object_simple.list_rbl_entry = [];
        self.expected_object_simple.report_link = self.dummy_param_simple.get ( 'Links' ).get ( 'Report_Link' );

        self.expected_object_simple_str = f"\nadd_date = {self.expected_object_simple.add_date}\n" \
                                      + f"blacklisted_count = {self.expected_object_simple.blacklisted_count}\n" \
                                      + f"contact_list_id = {self.expected_object_simple.contact_list_id}\n" \
                                      + f"id = {self.expected_object_simple.id}\n" \
                                      + f"label = {self.expected_object_simple.label}\n" \
                                      + f"last_check = {self.expected_object_simple.last_check}\n" \
                                      + f"list_rbl_entry = []\n" \
                                      + f"report_link = {self.expected_object_simple.report_link}\n" \
                                      + f"status = {self.expected_object_simple.status}\n" \
                                      + f"target = {self.expected_object_simple.target}\n" \
                                      + f"type = {self.expected_object_simple.type}\n\n";

        ## Create parameters passed
        self.dummy_param_blacklisted_on = {
            'ID': 1,
            'Type': "IPv4",
            'Target': "1.2.3.4",
            'Add_Date': 1633529168,
            'Last_Check': 1663885135,
            'Status': "Active",
            'Label': "Dummy label",
            'Contact_List_ID': "00000000000000000000000000000000",
            'Blacklisted_Count': "2",
            'Blacklisted_On': [
                {
                    "RBL": "multi.surbl.org",
                    "Delist": "http://www.surbl.org/surbl-analysis"
                },
                {
                    "RBL": "black.mail.abusix.zone",
                    "Delist": "https://www.abusix.ai/search?q=84.247.62.11"
                }
            ],
            'Links': {
                "Report_Link": "https://hetrixtools.com/report/blacklist/00000000000000000000000000000001/",
                "Whitelabel_Report_Link": ""
            }
        };

        ## Create results object wanted
        self.expected_object_blacklisted_on = Mock ();
        self.expected_object_blacklisted_on.id = self.dummy_param_blacklisted_on.get ( 'ID' );
        self.expected_object_blacklisted_on.type = self.dummy_param_blacklisted_on.get ( 'Type' );
        self.expected_object_blacklisted_on.target = self.dummy_param_blacklisted_on.get ( 'Target' );
        self.expected_object_blacklisted_on.add_date = self.dummy_param_blacklisted_on.get ( 'Add_Date' );
        self.expected_object_blacklisted_on.last_check = self.dummy_param_blacklisted_on.get ( 'Last_Check' );
        self.expected_object_blacklisted_on.status = self.dummy_param_blacklisted_on.get ( 'Status' );
        self.expected_object_blacklisted_on.label = self.dummy_param_blacklisted_on.get ( 'Label' );
        self.expected_object_blacklisted_on.contact_list_id = self.dummy_param_blacklisted_on.get ( 'Contact_List_ID' );
        self.expected_object_blacklisted_on.blacklisted_count = self.dummy_param_blacklisted_on.get ( 'Blacklisted_Count' );
        self.expected_object_blacklisted_on.list_rbl_entry = [
            ResponseRBLEntry ( self.dummy_param_blacklisted_on.get ( 'Blacklisted_On' ) [ 0 ] ),
            ResponseRBLEntry ( self.dummy_param_blacklisted_on.get ( 'Blacklisted_On' ) [ 1 ] ),
        ];
        self.expected_object_blacklisted_on.report_link = self.dummy_param_blacklisted_on.get ( 'Links' ).get ( 'Report_Link' );

        self.expected_object_blacklisted_on_str = f"\nadd_date = {self.expected_object_blacklisted_on.add_date}\n" \
                                      + f"blacklisted_count = {self.expected_object_blacklisted_on.blacklisted_count}\n" \
                                      + f"contact_list_id = {self.expected_object_blacklisted_on.contact_list_id}\n" \
                                      + f"id = {self.expected_object_blacklisted_on.id}\n" \
                                      + f"label = {self.expected_object_blacklisted_on.label}\n" \
                                      + f"last_check = {self.expected_object_blacklisted_on.last_check}\n" \
                                      + f"list_rbl_entry =\n" \
                                      + f"\t[\n" \
                                      + f"\tdelist_url = {self.expected_object_blacklisted_on.list_rbl_entry [ 0 ].delist_url}\n" \
                                      + f"\trbl_source = {self.expected_object_blacklisted_on.list_rbl_entry [ 0 ].rbl_source}\n" \
                                      + f"\t]\n" \
                                      + f"\t[\n" \
                                      + f"\tdelist_url = {self.expected_object_blacklisted_on.list_rbl_entry [ 1 ].delist_url}\n" \
                                      + f"\trbl_source = {self.expected_object_blacklisted_on.list_rbl_entry [ 1 ].rbl_source}\n" \
                                      + f"\t]\n" \
                                      + f"report_link = {self.expected_object_blacklisted_on.report_link}\n" \
                                      + f"status = {self.expected_object_blacklisted_on.status}\n" \
                                      + f"target = {self.expected_object_blacklisted_on.target}\n" \
                                      + f"type = {self.expected_object_blacklisted_on.type}\n\n";

    def test_str ( self ):
        response_rbl_entry = ResponseBlacklistMonitor ( self.dummy_param_simple );
        self.assertEqual ( self.expected_object_simple_str, str ( response_rbl_entry ) );

    def test_str_with_rbl_entries ( self ):
        response_rbl_entry = ResponseBlacklistMonitor ( self.dummy_param_blacklisted_on );
        self.assertEqual ( self.expected_object_blacklisted_on_str, str ( response_rbl_entry ) );

if __name__ == '__main__':
    unittest.main ();
