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

"""This module contains the models returned by the HetrixTools API"""

from typing import List

from hetrixtools_blacklist_api.models.responses import ResponseBlacklistMonitor


class APIResponseBlacklistMonitor ():
    """Response class returned by the HetrixTools API when querying blacklist monitor object(s)

    Attributes:
        status_code: status code returned by the API call
        ok: True if status_code < 400
        list_blacklist_monitor: list of ResponseBlacklistMonitor object
        total_records: number of blacklist monitor records in total
        previous_page_call_url: url to the previous page
        next_page_call_url: url to the next page
    """

    def __init__ ( self, status_code: int, raw_json: dict ):
        """Default constructor

        Args:
            status_code: status code returned by the API call
            raw_json: object returned by the API
        """
        self.status_code: int = int ( status_code );
        self.ok: bool = True if self.status_code < 400 else False;
        self.list_blacklist_monitor: List [ ResponseBlacklistMonitor ] = self.__parse_list_blacklist_monitor ( raw_json [ 0 ] )
        self.total_records: int = raw_json [ 1 ] [ "Meta" ].get ( "Total_Records", 0 );
        self.previous_page_call_url: str = raw_json [ 1 ] [ "Links" ] [ "Pages" ].get ( "Prev", None );
        self.next_page_call_url: str = raw_json [ 1 ] [ "Links" ] [ "Pages" ].get ( "Next", None );

    def __parse_list_blacklist_monitor ( self, raw_json: dict ) -> List [ ResponseBlacklistMonitor ]:
        """Parse raw json returned by the API into a custom object

        Args:
            raw_json: json returned by the API

        Returns:
            List [ ResponseBlacklistMonitor ]:
        """
        list_blacklist_monitor = [ ]
        for black_list_monitor_item in raw_json:
            list_blacklist_monitor.append ( ResponseBlacklistMonitor ( black_list_monitor_item ) )
        return list_blacklist_monitor
