#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

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
        with patch ( 'requests.get' ) as patch_request_get:
            patch_request_get.return_value = self.expected_object_simple;
            api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
            returned_object = api_wrapper.list_contact_lists ();
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_list_contact_lists_connection_error ( self ):
        ## Simulate connection problem
        import socket, requests;
        def guard ( *args, **kwargs ):
            raise requests.ConnectionError ( "Temporary failure in name resolution" );

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.list_contact_lists ();
        self.assertEqual ( returned_object.status_code, 503 );

    def test_list_contact_lists_connect_timeout ( self ):
        ## Simulate connection problem
        import socket, requests;
        def guard ( *args, **kwargs ):
            raise requests.ConnectTimeout ( "Temporary failure in name resolution" );

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.list_contact_lists ();
        self.assertEqual ( returned_object.status_code, 503 );


if __name__ == '__main__':
    unittest.main ();
