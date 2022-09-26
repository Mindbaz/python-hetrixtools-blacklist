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

"""This module contains some utils functions"""

import requests;


def read_file ( file_path: str, open_mode: str = "r", encoding: str = "utf-8", verbose: bool = False ) -> str:
    """Read a file and returns its content

    Args:
        file_path: Path to the file to read
        open_mode: String representing the open mode to use ("r" by default)
        encoding: String representing the encoding to use ("utf-8" by default)
        verbose: Verbose mode (False by default)

    Returns:
        str: file content as string
    """
    try:
        with open ( file = file_path, mode = open_mode, encoding = encoding ) as file:
            return file.read ();
    except ( LookupError, ValueError, FileNotFoundError, PermissionError ) as e:
        print ( f"Exception catched while reading file {file_path}: {e}" );
        return "";

def is_success_hetrixtools_API_call_response ( response: requests.Response ) -> bool:
    """Check the given response object and returns

    Args:
        response: the response object to check

    Returns:
        bool: True when the API returned a success (in terms of HetrixTools API) response
    """
    if not response.ok:
        return False;
    json_content = response.json ();
    ## For some response, the json returned on success is a list
    ## TODO real check (but it depends of each route response)
    if isinstance ( json_content, list ):
        pass
    elif isinstance ( json_content, dict ):
        if "status" not in json_content.keys ():
            return False;
        elif json_content.get ( "status" ) != "SUCCESS":
            return False;
    return True;
