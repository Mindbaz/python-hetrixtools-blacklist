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

from hetrixtools_blacklist_api.api_wrapper import APIWrapper
from hetrixtools_blacklist_api.raw_responses import BlacklistMonitorResponse


class HetrixTools ():
    """

    """

    def __init__ ( self, token_file_path: str, use_relay_endpoint: bool = False, verbose: bool = False ) -> None:
        """

        :param token_file_path:
        :param pool_size:
        :param use_relay_endpoint:
        :param verbose:
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

    def get_list_blacklist_monitor ( self ) -> list:
        """
        Get the whole list of blacklist monitor managed by HetrixTools
        :return: A list of hetrixtools_blacklist_api.raw_responses.BlacklistMonitorResponse object

        .. note:: (multiple API calls may be needed)
        """
        total_list_blacklist_monitor = [ ];
        request_response = self.__api.get_list_blacklist_monitor ( page_number = 0, result_per_page = 1024 );
        if request_response.ok:
            response_object = BlacklistMonitorResponse ( request_response.status_code, request_response.json () )
            total_list_blacklist_monitor.extend ( response_object.list_blacklist_monitor );
            while response_object.next_page_call_url is not None and response_object.ok:
                request_response = self.__api.get ( response_object.next_page_call_url );
                response_object = BlacklistMonitorResponse ( request_response.status_code, request_response.json () )
                total_list_blacklist_monitor.extend ( response_object.list_blacklist_monitor );
        return total_list_blacklist_monitor

    # TODO model ? laissez en raw ? Juste le get ?
    # def get_raw_api_status ( self ):
    #     """
    #
    #     :return:
    #     """
    #     request_response = self.__api.api_status ();
    #     print(request_response.content)
    #     return request_response;
    #
    # def get_raw_list_contacts_list ( self ):
    #     """
    #
    #     :return:
    #     """
    #     request_response = self.__api.list_contact_lists ();
    #     print(request_response.content)
    #     return request_response;
