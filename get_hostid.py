#!/usr/bin/python3.6
import json
import sys
import getpass
username=input("Enter Zabbix Username : ")
password=getpass.getpass("Enter password : ")
from zabbix_api import ZabbixAPI
server = "https://ZABBIX_SERVER_URL.com/"
zapi = ZabbixAPI(server=server)
zapi.login(username, password)
#save the list of hostnames in a file in current directory with name server_list.txt
with open (r"server_list.txt") as f:
	for line in f:
		host_name = line.strip()
		hostid_json = zapi.host.get({"output": ["hostid"], "filter": {"host": host_name}})
		hostid = hostid_json[0].get("hostid")
		print(host_name, hostid)
