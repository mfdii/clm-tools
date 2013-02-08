# clm-tools

CLI tools for interacting with BMC Cloud Lifecycle Management similar to AWS EC2 Tools.

## Getting Started

Requires Python and httplib2.

### Edit the config:

    [Basic]
    ENDPOINT="http://bmcpm:8080" <- IP/Hostname of the Platform Manager and port (typically 8080)
    USERNAME="" <- admin level credentials
    PASSWORD="" <- admin password 
    INSTALL_DIR="/Users/michael/dev/bmc-tools" <- some location you installed the files

### Run the commands

**clm-describe-availability-zones**

Returns the GUID and name of any PODs in CLM

**clm-describe-images**

Returns the GUID and name of any Service Offerings in CLM

**clm-describe-instances**

Returns the raw json of any Serivce Offering Instances (services you have provisioned)

**clm-describe-regions**

Returns the GUID and name of any Locations in CLM

**clm-describe-vpcs**

Returns the GUID and name of any Network Containers

