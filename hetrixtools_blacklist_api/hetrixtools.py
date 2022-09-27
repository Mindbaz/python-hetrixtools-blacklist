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

"""This module act as an additionnal layer for the api_wrapper"""

from typing import List

from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor
from hetrixtools_blacklist_api.api_wrapper import APIWrapper
from hetrixtools_blacklist_api.models.hetrixtools_api_responses import APIResponseBlacklistMonitor
from hetrixtools_blacklist_api.utils import is_success_hetrixtools_API_call_response;


class HetrixTools ():
    """Additionnal class layer that manages the api_wrapper calls and provides better responses model

    Attributes:
        __api (APIWrapper): APIWrapper instance
    """

    def __init__ ( self, token_file_path: str, use_relay_endpoint: bool = False, verbose: bool = False ) -> None:
        """Default constructor

        Args:
            token_file_path:
            use_relay_endpoint:
            verbose:
        """
        """API instance"""
        self.__api = APIWrapper ( token_file_path = token_file_path, use_relay_endpoint = use_relay_endpoint, verbose = verbose );

    def get_list_blacklist_monitor ( self ) -> List [ ResponseBlacklistMonitor ]:
        """Get the whole list of blacklist monitor managed by HetrixTools

        Returns:
            List [ ResponseBlacklistMonitor ]: list of objects retrieved

        Note:
            Multiple API calls may be needed
        """
        total_list_blacklist_monitor = [ ];
        ## Get first page list of blacklist monitor
        request_response = self.__api.get_list_blacklist_monitor ( page_number = 0, result_per_page = 1024 );
        if is_success_hetrixtools_API_call_response ( request_response ):
            try:
                ## Build object from raw dict response
                response_object = APIResponseBlacklistMonitor ( request_response.status_code, request_response.json () )
            except (KeyError, TypeError) as e:
                print ( f"Unexpected response received, cannot parse it. Error: {e}" );
                return total_list_blacklist_monitor;
            ## Add object to total list
            total_list_blacklist_monitor.extend ( response_object.list_blacklist_monitor );
            ## loop until there is another page to query
            while response_object.next_page_call_url is not None:
                request_response = self.__api.get ( response_object.next_page_call_url );
                if is_success_hetrixtools_API_call_response ( request_response ):
                    try:
                        response_object = APIResponseBlacklistMonitor ( request_response.status_code, request_response.json () )
                    except (KeyError, TypeError) as e:
                        print ( f"Unexpected response received, cannot parse it. Error: {e}" );
                        return total_list_blacklist_monitor;
                    total_list_blacklist_monitor.extend ( response_object.list_blacklist_monitor );
                else:
                    print ( f"An error occurred while retrieving the whole blacklist_list." );
                    break;
        return total_list_blacklist_monitor
