#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest;
from unittest.mock import patch, Mock;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__delete_blacklist_monitorTest ( unittest.TestCase ):
    def setUp ( self ) -> None:
        ## Create results object wanted
        self.expected_object_simple = Mock ();
        self.expected_object_simple.status_code = 200;
        self.expected_object_simple.json = Mock ( return_value = {
            "status": "SUCCESS",
            "message": "monitor has been deleted"
        } );
        self.expected_object_simple.ok = True;

        ## Create parameters passed
        self.dummy_param_simple = {
            "target": "1.2.3.4"
        };

    def test_delete_blacklist_monitor_success ( self ):
        """API Instance"""
        with patch ( "hetrixtools_blacklist_api.api_wrapper.APIWrapper.post",
                     return_value = self.expected_object_simple ) as post:
            api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
            returned_object = api_wrapper.delete_blacklist_monitor (
                **self.dummy_param_simple
            );
            post.assert_called_once_with (
                url = "https://api.hetrixtools.com/v2//blacklist/delete/",
                data = self.dummy_param_simple
            )
        self.assertEqual ( self.expected_object_simple, returned_object );


if __name__ == "__main__":
    unittest.main ();
