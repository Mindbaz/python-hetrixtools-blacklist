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
        with patch ( "requests.post" ) as patch_request_post:
            patch_request_post.return_value = self.expected_object_simple;
            api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
            returned_object = api_wrapper.delete_blacklist_monitor (
                *self.dummy_param_simple
            );
        self.assertEqual ( self.expected_object_simple, returned_object );

    def test_delete_blacklist_monitor_connection_error ( self ):
        ## Simulate connection problem
        import socket, requests;
        def guard ( *args, **kwargs ):
            raise requests.ConnectionError ( "Temporary failure in name resolution" );

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.delete_blacklist_monitor (
            *self.dummy_param_simple
        );
        self.assertEqual ( returned_object.status_code, 503 );

    def test_delete_blacklist_monitor_connect_timeout ( self ):
        ## Simulate connection problem
        import socket, requests;
        def guard ( *args, **kwargs ):
            raise requests.ConnectTimeout ( "Temporary failure in name resolution" );

        socket.socket = guard;
        """API Instance"""
        api_wrapper = APIWrapper ( token_file_path = "dummy_file_path" );
        returned_object = api_wrapper.delete_blacklist_monitor (
            *self.dummy_param_simple
        );
        self.assertEqual ( returned_object.status_code, 503 );


if __name__ == "__main__":
    unittest.main ();
