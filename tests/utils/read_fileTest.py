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
from unittest.mock import patch, mock_open;

from hetrixtools_blacklist_api.utils import read_file;


class read_fileTest ( unittest.TestCase ):
    def test_file_not_exists ( self ):
        file_content = read_file ( file_path = "filename_that_do_not_exists" );
        self.assertEqual ( file_content, "" );

    def test_param_empty_file_path ( self ):
        file_content = read_file ( file_path = "", );
        self.assertEqual ( file_content, "" );

    def test_empty_open_mode ( self ):
        file_content = read_file ( file_path = "filename_that_do_not_exists", open_mode = "" );
        self.assertEqual ( file_content, "" );

    def test_empty_encoding ( self ):
        file_content = read_file ( file_path = "filename_that_do_not_exists", encoding = "" );
        self.assertEqual ( file_content, "" );

    def test_empty_verbose ( self ):
        str_expected = "dummy test\ndummy 2\r\n\tdummy 3";
        with patch ( "builtins.open", mock_open ( read_data = str_expected ) ):
            file_content = read_file ( file_path = "filename_that_do_not_exists", verbose = "" );
        self.assertEqual ( file_content, str_expected );

    def test_correct_file ( self ):
        str_expected = "dummy test\ndummy 2\r\n\tdummy 3";
        with patch ( "builtins.open", mock_open ( read_data = str_expected ) ) as mock_file:
            file_content = read_file ( file_path = "filename_that_do_not_exists" );
        self.assertEqual ( file_content, str_expected );


if __name__ == '__main__':
    unittest.main ();
