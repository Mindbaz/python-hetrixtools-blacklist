#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get",
                     return_value = self.expected_object_simple ) as get:
            api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
            returned_object = api_wrapper.api_status ();
            get.assert_called_once_with (
                url = "https://api.hetrixtools.com/v1//status/"
            )
        self.assertEqual ( self.expected_object_simple, returned_object );


if __name__ == "__main__":
    unittest.main ();
