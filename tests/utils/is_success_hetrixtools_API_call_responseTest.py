#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Mindbaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""""""

import unittest;
from unittest.mock import patch, mock_open, Mock;

import requests

from hetrixtools_blacklist_api.utils import is_success_hetrixtools_API_call_response;


class is_success_hetrixtools_API_call_responseTest ( unittest.TestCase ):
    def test_not_ok ( self ):
        response = requests.Response ();
        response.status_code = 500;
        self.assertFalse ( is_success_hetrixtools_API_call_response ( response = response ) );

    def test_json_as_empty_array ( self ):
        response = requests.Response ();
        response.status_code = 200;
        response._content = \
            b"""
            []
        """;
        self.assertTrue ( is_success_hetrixtools_API_call_response ( response = response ) );

    def test_json_as_correct_array ( self ):
        response = requests.Response ();
        response.status_code = 200;
        response._content = \
            b"""[
            [],
            {
                \"Meta\": {
                    \"Total_Records\": \"0\"
                },
                \"Links\": {
                    \"Pages\": { }
                }
            }
        ]""";
        self.assertTrue ( is_success_hetrixtools_API_call_response ( response = response ) );

    def test_json_as_empty_dict ( self ):
        response = requests.Response ();
        response.status_code = 200;
        response._content = \
            b"""{
            }""";
        self.assertFalse ( is_success_hetrixtools_API_call_response ( response = response ) );

    def test_json_as_malformed_dict ( self ):
        response = requests.Response ();
        response.status_code = 200;
        response._content = \
            b"""{
                "dummy_key": "dummy_value"
            }""";
        self.assertFalse ( is_success_hetrixtools_API_call_response ( response = response ) );

    def test_json_status_success ( self ):
        response = requests.Response ();
        response.status_code = 200;
        response._content = \
            b"""{
                "status": "SUCCESS"
            }""";
        self.assertTrue ( is_success_hetrixtools_API_call_response ( response = response ) );

    def test_json_status_not_success ( self ):
        response = requests.Response ();
        response.status_code = 200;
        response._content = \
            b"""{
                "status": "ERROR"
            }""";
        self.assertFalse ( is_success_hetrixtools_API_call_response ( response = response ) );


if __name__ == '__main__':
    unittest.main ();
