# Zabbix_api scripts
The repo contains different scripts that can be used for managing Zabbix monitoring configurations
Programming Language used: Python 3.6.8

1. To fetch host Ids of hosts added in Zabbbix from a list of servers

- get_hostid.py

This script can be used to fetch out the Zabbix host ID number for the hosts added in Zabbix 

This host id is useful when doing different operations on the hosts ( modifications, adding trigger items..etc..)

Prerequisites:

    * Modify the script to use the actual Zabbix Server URL
    
    * Create a file server_list.txt and add the hostnames in it



2. To delete a lists of hosts from Zabbix Monitoring

- delete_host.py


This script can be used to deletet the hosts that are already added to Zabbix


Prerequisites:

    * Modify the script to use the actual Zabbix Server URL

    * Create a file server_list.txt and add the hostnames of the servers, that needed to delete in it

