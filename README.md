# python-hetrixtools-blacklist

Unofficial tool to retrieve data from HetrixTools API about blacklist monitoring. The recovered data will
offer a simple schema in order to be able to easily save this data in a flat
file or in database.

## Models

### ResponseBlacklistMonitor

* id : `int`
* type : `str`
* target : `str`
* add_date : `int`
* last_check : `int`
* status : `str`
* label : `str|None`
* contact_list_id : `str`
* blacklisted_count : `int`
* list_rbl_entry: `List [ ResponseRBLEntry ]`
* report_link: `str`

### ResponseRBLEntry

* rbl_source : `str`
* delist_url : `str`

## How to use it

```sh
python entry_points_hetrixtools_blacklist_api/hetrixtools_get_list_blacklist_monitor.py -h
> usage: hetrixtools_get_list_blacklist_monitor [-h] [--token_file TOKEN_FILE] [--use_relay_endpoint] [--verbose] [--version]
```

# Support version

Python : `>=3.6`
