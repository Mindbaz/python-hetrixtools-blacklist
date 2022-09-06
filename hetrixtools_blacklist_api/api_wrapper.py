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

import requests

from hetrixtools_blacklist_api.utils import read_file

class APIWrapper ( object ):
    """
    """

    def __init__ ( self, token_file_path: str, use_relay_endpoint: bool = False, verbose: bool = False ) -> None:
        """

        :param token_file_path: Absolute file path to HetrixTools API token
        :param use_relay_endpoint: Use the relay endpoint (False by default)
        :param verbose: Display additionnal logs. (False by default)
        """
        """Use the classic API endpoing or the relay one (in case of CloudFlare blocking your IP address)"""
        self.use_relay_endpoint: bool = bool ( use_relay_endpoint );
        """API Token"""
        self.__token = read_file ( file_path = token_file_path, verbose = verbose ).strip ();
        """Endpoint URL to call"""
        if not self.use_relay_endpoint:
            self.__endpoint_url: str = "https://api.hetrixtools.com/";
        else:
            self.__endpoint_url: str = "https://relay.hetrixtools.com/api/";
        """Verbose mode"""
        self.verbose: bool = bool ( verbose );

    def get_list_blacklist_monitor ( self, page_number: int = 0, result_per_page: int = 1024 ):
        route = f"v2/{self.__token}/blacklist/monitors/{int ( page_number )}/{int ( result_per_page )}/"
        response = self.get ( url = self.__endpoint_url + route );
        return response;

    def add_blacklist_monitor ( self, target: str, label: str, contact: str ):
        """

        :param target:
        :param label:
        :param contact:
        :return:


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

    def edit_blacklist_monitor ( self, target: str, label: str, contact: str ):
        #TODO {'status': 'SUCCESS', 'message': 'monitor has been edited'}
        route = f"v2/{self.__token}/blacklist/edit/";
        data_object = {
            "target": target,
            "label": str ( label ),
            "contact": str ( contact )
        };
        return self.post ( url = self.__endpoint_url + route, data = data_object );

    def delete_blacklist_monitor ( self, target: str ):
        #TODO {'status': 'SUCCESS', 'message': 'monitor has been deleted'}
        route = f"v2/{self.__token}/blacklist/delete/";
        data_object = {
            "target": target
        };
        return self.post ( url = self.__endpoint_url + route, data = data_object );

    def api_status ( self ):
        route = f"v1/{self.__token}/status/";
        return self.get ( url = self.__endpoint_url + route );

    def list_contact_lists ( self ):
        route = f"v1/{self.__token}/contacts/";
        return self.get ( url = self.__endpoint_url + route );

    def get ( self, url: str, parameters: dict = None ) -> requests.Response:
        response = requests.get ( url = url, params = parameters );
        return response;

    def post ( self, url: str, data: dict = None ) -> requests.Response:
        response = requests.post ( url = url, data = data );
        return response;
