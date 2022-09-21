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

        #TODO delete dummy test
        # target = "1.2.3.4"
        # label = "test"
        # contact = "40c093754bf26f461883f9bd918ff52b"
        # add_response = self.__api.add_blacklist_monitor ( target = target, label = label, contact = contact );
        # if add_response.ok:
        #     print ( add_response.json () )
        #
        # edit_response = self.__api.edit_blacklist_monitor( target = target, label = "test-edited", contact = contact )
        # if edit_response.ok:
        #     print (edit_response.json())
        #
        # remove_response = self.__api.delete_blacklist_monitor( target = target )
        # if remove_response.ok:
        #     print (remove_response.json())

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
        if request_response.ok:
            ## Build object from raw dict response
            response_object = APIResponseBlacklistMonitor ( request_response.status_code, request_response.json () )
            ## Add object to total list
            total_list_blacklist_monitor.extend ( response_object.list_blacklist_monitor );
            ## loop until there is another page to query
            while response_object.next_page_call_url is not None and response_object.ok:
                request_response = self.__api.get ( response_object.next_page_call_url );
                response_object = APIResponseBlacklistMonitor ( request_response.status_code, request_response.json () )
                total_list_blacklist_monitor.extend ( response_object.list_blacklist_monitor );
        return total_list_blacklist_monitor