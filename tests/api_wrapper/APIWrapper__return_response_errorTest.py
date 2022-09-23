#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest;
from unittest.mock import patch, Mock;

from hetrixtools_blacklist_api.api_wrapper import APIWrapper;


class APIWrapper__return_response_errorTest ( unittest.TestCase ):
    def test_msg_assigned ( self ):
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        """Msg expected"""
        msg_expected = "Dummy ERROR";
        """Status code expected"""
        status_code_expected = 503;
        response_error = api_wrapper._APIWrapper__return_response_error ( status_code = status_code_expected,
                                                                          msg = msg_expected );
        self.assertEqual ( response_error.reason, msg_expected );
        self.assertEqual ( response_error.status_code, status_code_expected );

    def test_msg_empty ( self ):
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        """Msg expected"""
        msg_expected = None;
        """Status code expected"""
        status_code_expected = 501;
        response_error = api_wrapper._APIWrapper__return_response_error ( status_code = status_code_expected );
        self.assertEqual ( response_error.reason, msg_expected );
        self.assertEqual ( response_error.status_code, status_code_expected );


if __name__ == '__main__':
    unittest.main ();
