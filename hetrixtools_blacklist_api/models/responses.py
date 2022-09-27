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

"""This module contains models returned by this project"""

from typing import List;


class ResponseRBLEntry ():
    """Response class returned by this project when treating with RBL entry

    Attributes:
        rbl_source: on which RBL entry it's registered
        delist_url: url for delisting this entry in the corresponding RBL
    """

    def __init__ ( self, raw_json: dict ):
        """Default constructor

        Args:
            raw_json: object returned by HetrixTools API
        """
        self.rbl_source: str = raw_json [ 'RBL' ];
        self.delist_url: str = raw_json.get ( 'Delist' );

    def __str__ ( self ) -> str:
        """Create a string representation of this instance

        Returns:
            str: string representation of this instance
        """
        string: str = "";
        for var_key in sorted ( vars ( self ) ):
            string = string + f"\t{var_key} = {getattr ( self, var_key )}\n";
        return f"{string}";

    def __eq__ ( self, other ) -> bool:
        """Check equality between this object and another ResponseRBLEntry object

        Note:
            This method exists mainly for testing purpose

        Args:
            other: ResponseRBLEntry object to test for equality

        Returns:
            bool: True if both objects are equals
        """
        try:
            return self.rbl_source == other.rbl_source \
                   and self.delist_url == other.delist_url;
        except AttributeError:
            return False;


class ResponseBlacklistMonitor ():
    """Response class returned by this project when treating with Blacklist monitor

    Attributes:
        id: unique ID
        type: one of the following types 'IPv4'|'IPv6'|'Domain'
        target: IP or Domain address monitored (depending of the type) 
        add_date: date at which this blacklist monitor was created
        last_check: last date at which this target was checked for RBL
        status: one of the following status 'Active'|'In Queue'|'Processing'
        label: label associated to the blacklist monitor
        contact_list_id: which contact list to used (for alerting purpose)
        blacklisted_count: number of RBL entry for this target
        list_rbl_entry: list of RBL entry for this target
        report_link: url to HetrixTools website report for this target
    """

    def __init__ ( self, raw_json: dict ):
        """Default constructor

        Args:
            raw_json: object returned by HetrixTools API
        """
        self.id: str = raw_json [ "ID" ];
        self.type: str = raw_json [ "Type" ];
        self.target: str = raw_json [ "Target" ];
        self.add_date: int = raw_json [ "Add_Date" ];
        self.last_check: int = raw_json [ "Last_Check" ];
        self.status: str = raw_json [ "Status" ];
        self.label: str = raw_json [ "Label" ];
        self.contact_list_id: str = raw_json [ "Contact_List_ID" ];
        self.blacklisted_count: int = int ( raw_json [ "Blacklisted_Count" ] );
        self.list_rbl_entry: List [ ResponseRBLEntry ] = self.__parse_list_rbl_entry ( raw_json [ "Blacklisted_On" ] );
        self.report_link: str = raw_json [ "Links" ] [ "Report_Link" ];

    def __str__ ( self ) -> str:
        """Create a string representation of this instance

        Returns:
            str: string representation of this instance
        """
        string: str = "";
        for var_key in sorted ( vars ( self ) ):
            current_var = getattr ( self, var_key );
            ## Check if variable is a list
            if ( isinstance ( current_var, list ) and len ( current_var ) > 0 ):
                string = string + f"{var_key} =\n";
                ## Loop over list
                for item in current_var:
                    string = string + f"\t[\n{item.__str__()}\t]\n";
            else:
                string = string + f"{var_key} = {current_var}\n";
        return f"\n{string}\n";

    def __parse_list_rbl_entry ( self, raw_json: dict ) -> List [ ResponseRBLEntry ]:
        """Parse object returned by HetrixTools API to convert it into a List [ ResponseRBLEntry ]

        Args:
            raw_json: object returned by HetrixTools API

        Returns:
            List [ ResponseRBLEntry ]: returned list
        """
        list_blacklisted_on: List [ ResponseRBLEntry ] = [ ];
        if raw_json is not None:
            for blacklisted_on_raw_item in raw_json:
                list_blacklisted_on.append ( ResponseRBLEntry ( blacklisted_on_raw_item ) );
        return list_blacklisted_on;

    def __eq__ ( self, other ) -> bool:
        """Check equality between this object and another ResponseBlacklistMonitor object

        Note:
            This method exists mainly for testing purpose

        Args:
            other: ResponseBlacklistMonitor object to test for equality

        Returns:
            bool: True if both objects are equals
        """
        try:
            if ( len ( self.list_rbl_entry ) != len ( other.list_rbl_entry ) ):
                return False;
            for index, item in enumerate ( self.list_rbl_entry ):
                if ( item != other.list_rbl_entry [ index ] ):
                    return False;
            return self.id == other.id \
                   and self.label == other.label \
                   and self.target == other.target \
                   and self.type == other.type \
                   and self.status == other.status \
                   and self.last_check == self.last_check \
                   and self.blacklisted_count == self.blacklisted_count;
        except AttributeError:
            return False;