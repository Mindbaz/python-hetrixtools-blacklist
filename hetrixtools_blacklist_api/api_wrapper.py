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

"""This module offer a wrapper for some HetrixTools API calls (blacklist monitoring part only)"""

import requests

from hetrixtools_blacklist_api.utils import read_file

class APIWrapper ( ):
    """Wrapper for HetrixTools API calls

    Attributes:
        use_relay_endpoint (bool): Use the classic API endpoint or the relay one (in case of blocking proxy)
        verbose (bool): Display additional logs.
        __token (str): Token string representation.
        __endpoint_url (str): Endpoint URL at which the wrapper will make its calls.
    """

    def __init__ ( self, token_file_path: str, use_relay_endpoint: bool = False, verbose: bool = False ) -> None:
        """Default constructor

        Args:
            token_file_path: Absolute file path to HetrixTools API token.
            use_relay_endpoint: Use the relay endpoint. Defaults to False.
            verbose: Display additional logs. Defaults to False.
        """
        """Use the classic API endpoint or the relay one (in case of CloudFlare blocking your IP address)"""
        self.use_relay_endpoint: bool = bool ( use_relay_endpoint );
        """API Token"""
        self.__token: str = read_file ( file_path = token_file_path, verbose = verbose ).strip ();
        """Endpoint URL to call"""
        if not self.use_relay_endpoint:
            self.__endpoint_url: str = "https://api.hetrixtools.com/";
        else:
            self.__endpoint_url: str = "https://relay.hetrixtools.com/api/";
        """Verbose mode"""
        self.verbose: bool = bool ( verbose );

    def get_list_blacklist_monitor ( self, page_number: int = 0, result_per_page: int = 1024 ) -> requests.Response:
        """Retrieve list of blacklist monitor from HetrixTools API

        Args:
            page_number: Page index to retrieved
            result_per_page: Number of results by page

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = f"v2/{self.__token}/blacklist/monitors/{int ( page_number )}/{int ( result_per_page )}/";
        response = self.get ( url = self.__endpoint_url + route );
        return response;

    def add_blacklist_monitor ( self, target: str, label: str, contact: str ) -> requests.Response:
        """Call HetrixTools API to add a new blacklist monitor

        Args:
            target: An IP/domain address
            label: Label associated to the blacklist monitor (for easier identification / query)
            contact: Contact ID used for the alerting

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        #TODO {'status': 'SUCCESS', 'message': 'monitor has been added', 'monitor_id': 'aaebae66de1c2921b21471d384eeba0e', 'report_id': '6805d5c042f36d81cf9a1f55df7c120e'}
        route = f"v2/{self.__token}/blacklist/add/"
        data_object = {
            "target": str ( target ),
            "label": str ( label ),
            "contact": str ( contact )
        };
        response = self.post ( url = self.__endpoint_url + route, data = data_object );
        return response;

    def edit_blacklist_monitor ( self, target: str, label: str, contact: str ) -> requests.Response:
        """Call HetrixTools API to edit an existing blacklist monitor

        Args:
            target: An IP/domain address
            label: Label associated to the blacklist monitor (for easier identification / query)
            contact: Contact ID used for the alerting

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        #TODO {'status': 'SUCCESS', 'message': 'monitor has been edited'}
        route = f"v2/{self.__token}/blacklist/edit/";
        data_object = {
            "target": target,
            "label": str ( label ),
            "contact": str ( contact )
        };
        return self.post ( url = self.__endpoint_url + route, data = data_object );

    def delete_blacklist_monitor ( self, target: str ) -> requests.Response:
        """Call HetrixTools API to delete an existing blacklist monitor

        Args:
            target: An IP/domain address

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        #TODO {'status': 'SUCCESS', 'message': 'monitor has been deleted'}
        route = f"v2/{self.__token}/blacklist/delete/";
        data_object = {
            "target": target
        };
        return self.post ( url = self.__endpoint_url + route, data = data_object );

    def api_status ( self ) -> requests.Response:
        """Call HetrixTools API to get account status about API remaining calls

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = f"v1/{self.__token}/status/";
        return self.get ( url = self.__endpoint_url + route );

    def list_contact_lists ( self ) -> requests.Response:
        """Call hetrixTools API to get list of contacts ID

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = f"v1/{self.__token}/contacts/";
        return self.get ( url = self.__endpoint_url + route );

    def get ( self, url: str, parameters: dict = None ) -> requests.Response:
        """Calls an API REST route: GET

        Args:
            url: url to call
            parameters: parameters for this call

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        response = requests.get ( url = url, params = parameters );
        return response;

    def post ( self, url: str, data: dict = None ) -> requests.Response:
        """Calls an API REST route: POST

        Args:
            url: url to call
            data: data for this call

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        response = requests.post ( url = url, data = data );
        return response;
