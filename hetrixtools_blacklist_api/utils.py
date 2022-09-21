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

import os


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
    if ( not os.path.isfile ( file_path ) ):
        if ( verbose ):
            print ( f"Trying to reads a non-existing file: {file_path}" )
        return ""
    with open ( file = file_path, mode = open_mode, encoding = encoding ) as file:
        return file.read ()
