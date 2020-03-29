# nxos-telemetry-grpc-receiver
python --version
Python 3.7.5

Receiver of model-driven-telemetry from NX-OS in gRPC format.
Protobuffers used from https://github.com/CiscoDevNet/nx-telemetry-proto (source specified in Nexus programmability guide: https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x_chapter_0101001.html)

Receiver shows received gRPC messages contain  telemetry data. Data is parsed into JSON and printed out to cli.
JSON might be used for investigation of internal fields. 

In example yang model Cisco-NX-OS-device:System is used (xpath: Cisco-NX-OS-device:System/intf-items - only interfaces configuration and operational data). 

Server listens for TCP port 50001.
Telemetry configuration on NX-OS 9.3(3):

telemetry
  destination-group 1
    ip address <receiver_ip> port 50001 protocol gRPC encoding GPB 
  sensor-group 1
    data-source YANG
    path Cisco-NX-OS-device:System/intf-items
  subscription 1
    dst-grp 1
    !send data every 10 seconds
    snsr-grp 1 sample-interval 10000
    
Run 'python server.py' to receive data.
Main purpose is to understand received data in gRPC if yang-model itself is not enough. 
