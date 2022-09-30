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

"""Retrieves the blacklist_monitor for a given account (token needed) and display the results in a 'visual way'"""

import os
import argparse

from hetrixtools_blacklist_api.hetrixtools import HetrixTools;
from hetrixtools_blacklist_api import __version__;


def parse_arguments () -> argparse.Namespace:
    parser = argparse.ArgumentParser ( prog = "hetrix_tools_get_list_blacklist_monitor" );

    ## All arguments
    parser.add_argument ( "--token_file", type = str, help = "HetrixTools API token file" );
    parser.add_argument ( "--use_relay_endpoint", action = "store_true", help = "Verbose mode" );
    parser.add_argument ( "--verbose", action = "store_true", help = "Verbose mode" );
    parser.add_argument ( "--version", action = "store_true", help = "Display version" );
    args = parser.parse_args ();
    return args;


def print_version () -> None:
    """Print the current project version
    """
    print ( __version__ );
    exit ( 0 );


def print_verbose ( args: argparse.Namespace ) -> None:
    """Print additional information when verbose enabled

    Args:
        args: argparse namespace
    """
    print ( "v v v v v v v v v v v v v v v v v v v v v" );
    print ( "Arguments list : " );
    for arg in sorted ( vars ( args ) ):
        print ( "{} : {}".format ( arg.rjust ( 30 ), getattr ( args, arg ) ) );
    print ( "^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^" );


def validate_arguments ( args: argparse.Namespace ) -> None:
    """Validate some arguments and exit in case of bad/missing parameters

    Args:
        args: argparse namespace
    """
    ## --token arg check
    if ( not args.token_file ):
        print ( "Missing --token file. -h to show help" );
        exit ( 2 );
    if ( not os.path.isfile ( args.token_file ) ):
        print ( "Argument '--token' do not corresponds to an existing file. -h to show help" );
        exit ( 2 );


def run () -> None:
    """Main function called
    """
    ## Parse arguments from script user input
    args = parse_arguments ();

    ## Display version
    if ( args.version == True ):
        print_version ();

    ## Valid required argument
    validate_arguments ( args )

    ## Print args to console
    if ( args.verbose ):
        print_verbose ( args );

    ## Begin
    hetrix_tools_blacklist_client = HetrixTools ( token_file_path = args.token_file, use_relay_endpoint = args.use_relay_endpoint, verbose = args.verbose );

    ## Display result list of blacklist monitor
    all_blacklist_monitor_list = hetrix_tools_blacklist_client.get_list_blacklist_monitor ();
    for blacklist_monitor in all_blacklist_monitor_list:
        print ( blacklist_monitor );


if __name__ == "__main__":
    run ();
