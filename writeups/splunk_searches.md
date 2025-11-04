# Example Splunk Searches & Notes

1) Failed login brute force detection (Windows RDP)
index=wineventlog EventCode=4625 | stats count by src_ip, Account_Name | where count > 10

2) New service creation (suspicious persistence)
index=wineventlog EventCode=4697 | table _time, EventCode, Service_Name, Account_Name, host
