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

class BlacklistedOnItem ():
    """

    """

    def __init__ ( self, raw_dict: dict ) -> None:
        """

        :param raw_dict:
        """
        self.realtime_black_list: str = raw_dict [ 'RBL' ];
        self.delist_url = raw_dict.get ( 'Delist' )

    def __str__ ( self) -> str:
        """

        :return:
        """
        string: str = "";
        for var_key in sorted ( vars ( self ) ):
            string = string + f"\t{var_key} = {getattr ( self, var_key )}\n";
        return f"{string}"


class BlacklistMonitor ():
    """

    """

    def __init__ ( self, raw_json: dict ) -> None:
        """

        :param raw_json:
        """
        """"""
        self.id: str = raw_json [ "ID" ];
        """"""
        self.type: str = raw_json [ "Type" ];
        """"""
        self.target: str = raw_json [ "Target" ];
        """"""
        self.add_date: int = raw_json [ "Add_Date" ];
        """"""
        self.last_check: int = raw_json [ "Last_Check" ];
        """"""
        self.status: str = raw_json [ "Status" ];
        """"""
        self.label: str = raw_json [ "Label" ];
        """"""
        self.contact_list_id: str = raw_json [ "Contact_List_ID" ];
        """"""
        self.blacklisted_count: int = raw_json [ "Blacklisted_Count" ];
        """List of BlacklistedOnItem object"""
        self.list_blacklisted_on: list = self.__parse_list_blacklisted_on ( raw_json [ "Blacklisted_On" ] )
        """"""
        self.report_link: str = raw_json [ "Links" ] [ "Report_Link" ];

    def __str__ ( self ) -> str:
        """

        :return:
        """
        string: str = ""
        for var_key in sorted ( vars ( self ) ):
            current_var = getattr ( self, var_key );
            ## Check if variable is a list
            if ( isinstance(current_var, list) and len ( current_var ) > 0 ):
                string = string + f"{var_key} =\n";
                ## Loop over list
                for item in current_var:
                    string = string + f"\t[\n{item.__str__()}\t]\n";
            else:
                string = string + f"{var_key} = {current_var}\n";
        return f"\n{string}\n"

    #TODO static yes/no, alternative ?
    def __parse_list_blacklisted_on ( self, raw_json: dict ) -> list:
        """

        :param raw_json:
        :return:
        """
        list_blacklisted_on: list = [ ];
        if raw_json is not None:
            for blacklisted_on_raw_item in raw_json:
                list_blacklisted_on.append ( BlacklistedOnItem ( blacklisted_on_raw_item ) );
        return list_blacklisted_on;
