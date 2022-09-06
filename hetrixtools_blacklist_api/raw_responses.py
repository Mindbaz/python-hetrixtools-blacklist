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

from hetrixtools_blacklist_api.blacklist_monitor import BlacklistMonitor


class BlacklistMonitorResponse ():
    """

    """

    def __init__ ( self, status_code: int, raw_json: dict ):
        """

        :param status_code:
        :param raw_json:
        """
        """"""
        self.status_code: int = int ( status_code );
        """"""
        self.ok: bool = True if self.status_code < 400 else False;
        """"""
        self.list_blacklist_monitor: list = self.__parse_list_blacklist_monitor ( raw_json [ 0 ] )
        """"""
        self.total_records: int = raw_json [ 1 ] [ 'Meta' ].get ( 'Total_Records', 0 );
        """"""
        self.previous_page_call_url: str = raw_json [ 1 ] [ 'Links' ] [ 'Pages' ].get ( 'Prev', None );
        """"""
        self.next_page_call_url: str = raw_json [ 1 ] [ 'Links' ] [ 'Pages' ].get ( 'Next', None );

    def __parse_list_blacklist_monitor ( self, raw_json: dict ) -> list:
        list_blacklist_monitor = [ ]
        for black_list_monitor_item in raw_json:
            list_blacklist_monitor.append ( BlacklistMonitor ( black_list_monitor_item ) )
        return list_blacklist_monitor
