#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import patch, Mock;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__list_contact_listsTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create results object wanted
        self.expected_object_simple = Mock ();
        self.expected_object_simple.status_code = 200;
        self.expected_object_simple.json = Mock ( return_value = [
            {
                "Name": "Dummy Contact 1",
                "ID": "00000000000000000000000000000000"
            },
            {
                "Name": "Dummy contact 2",
                "ID": "00000000000000000000000000000001"
            }
        ] );
        self.expected_object_simple.ok = True;

    def test_list_contact_lists_success ( self ):
        """API Instance"""
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.get",
                     return_value = self.expected_object_simple ) as get:
            api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
            returned_object = api_wrapper.list_contact_lists ();
            get.assert_called_once_with (
                url = "https://api.hetrixtools.com/v1//contacts/"
            )
        self.assertEqual ( self.expected_object_simple, returned_object );


if __name__ == "__main__":
    unittest.main ();
