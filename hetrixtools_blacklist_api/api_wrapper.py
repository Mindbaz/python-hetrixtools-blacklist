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

import requests;
from typing import Optional;

from hetrixtools_blacklist_api.utils import read_file;


class APIWrapper ():
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
        self.__token: str = read_file ( file_path = token_file_path ).strip ();
        """Endpoint URL to call"""
        if not self.use_relay_endpoint:
            self.__endpoint_url: str = "https://api.hetrixtools.com/";
        else:
            self.__endpoint_url: str = "https://relay.hetrixtools.com/api/";
        """Verbose mode"""
        self.verbose: bool = bool ( verbose );

    @property
    def token ( self ) -> str:
        """Token getter

        Returns:
            str: __token attribute
        """
        return self.__token;

    @property
    def endpoint_url ( self ) -> str:
        """Endpoint_url getter

        Returns:
            str: __endpoint_url attribute
        """
        return self.__endpoint_url;

    def get_list_blacklist_monitor ( self, page_number: int = 0, result_per_page: int = 1024 ) -> requests.Response:
        """Retrieve list of blacklist monitor from HetrixTools API

        Args:
            page_number: Page index to retrieved
            result_per_page: Number of results by page

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = "v2/{}/blacklist/monitors/{}/{}/"\
            .format ( self.token, int ( page_number ), int ( result_per_page ) );
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
        route = "v2/{}/blacklist/add/".format ( self.token );
        data_object = {
            "target": str ( target ),
            "label": str ( label ),
            "contact": str ( contact )
        };
        response = self.post ( url = self.endpoint_url + route, data = data_object );
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
        route = "v2/{}/blacklist/edit/".format ( self.token );
        data_object = {
            "target": str ( target ),
            "label": str ( label ),
            "contact": str ( contact )
        };
        return self.post ( url = self.endpoint_url + route, data = data_object );

    def delete_blacklist_monitor ( self, target: str ) -> requests.Response:
        """Call HetrixTools API to delete an existing blacklist monitor

        Args:
            target: An IP/domain address

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = "v2/{}/blacklist/delete/".format ( self.token );
        data_object = {
            "target": target
        };
        return self.post ( url = self.endpoint_url + route, data = data_object );

    def api_status ( self ) -> requests.Response:
        """Call HetrixTools API to get account status about API remaining calls

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = "v1/{}/status/".format ( self.token );
        return self.get ( url = self.endpoint_url + route );

    def list_contact_lists ( self ) -> requests.Response:
        """Call hetrixTools API to get list of contacts ID

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        route = "v1/{}/contacts/".format ( self.token );
        return self.get ( url = self.endpoint_url + route );

    def get ( self, url: str, params: dict = None ) -> requests.Response:
        """Calls an API REST route: GET

        Args:
            url: url to call
            params: params for this call

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        try:
            response = requests.get ( url = url, params = params );
            return response;
        except ( requests.ConnectTimeout, requests.ConnectionError ) as e:
            print ( "An error occured while calling get url {}, reason: {}".format ( url, e ) );
            return self.__build_response_object ( status_code = 503, msg = e );

    def post ( self, url: str, data: dict = None ) -> requests.Response:
        """Calls an API REST route: POST

        Args:
            url: url to call
            data: data for this call

        Returns:
            requests.Response: response returned by HetrixTools API
        """
        try:
            response = requests.post ( url = url, data = data );
            return response;
        except (requests.ConnectTimeout, requests.ConnectionError) as e:
            print ( "An error occured while calling get url {}, reason: {}".format ( url, e ) );
            return self.__build_response_object ( status_code = 503, msg = e );

    def __build_response_object ( self, status_code: int, msg: Optional [ str ] = None ) -> requests.Response:
        """Create a request.Response with the given status_code and msg
        
        Args:
            status_code: status_code associated to the Response
            msg: msg associated to the Response

        Returns:
            requests.Response: error response built with given status_code and msg
        """
        error_response = requests.Response ();
        error_response.status_code = int ( status_code );
        error_response.reason = msg;
        return error_response;
