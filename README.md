# CVE-2023-27055

## Aver Information Inc. PTZApp2 Directory Traversal to LFI Vulnerability

**Description**: PTZApp2 is a free application that is used to control AVER USB cameras. This software creates a web application on the localhost that users of the software can use to manage and control connected USB PTZ cameras. 

**Impact**: By sending a crafted GET request to the web based application it is possible to perform a directory traversal attack against the application and disclose sensitive files stored on the system. The PoC.py script discloses the HOSTS file of the system, but can be modified to access sensitive files stored on the system, including the public and private keys of the web application server created by the software. 

**Root Cause**: This vulnerability is caused by insufficient filtering and validation of browser supplied user input. 

**Affected Versions**: All versions of PTZApp2 prior to update 2.0.1051.53 are affected by this vulnerability. 
