> [!IMPORTANT] 
> This project is under development. All source code and features on the main branch are for the purpose of testing or evaluation and not production ready.
# MFD Const

Module for keeping const values.

## Available data structures
* `DEVICE_IDS` - family: device_id mapping like "CPK": ["0xF0A5", "0xF0A5"]
* `DEVID_CLASS_MAP_NICINSTALLER` - speed: device_id mapping.
* `DRIVER_DIRECTORY_MAP` - driver: directory mapping like "ice": "PROCGB"
* `DRIVER_DEVICE_ID_MAP` - driver: device_id mapping like "ice": {DeviceID(0x124C), DeviceID(0x124D)}
* `SPEED_IDS`- speed: device_id mapping like "@1G": DEVICE_IDS["PVL"]
* `Family` - Enum class of available families like `Family.PVL`
* `family_to_full_name` - Dict with mapping Family to full name like `Family.CVL: "Columbiaville"`
* `Speed`- Enum class of available speeds like `Speed.G100`
* `FREEBSD_ADVERTISE_SPEED`- advertise_speed: speed mapping like "1G": {"ice": 0x4, "ixl": 0x2, "ix": 0x2}
* `MANAGEMENT_NETWORK` - list of networks used for management connection
* `LOCAL_DEFAULT_MAP` (`qos.py`) - QoS Default map for DCB local settings 
* `LOCAL_ISCSI_MAP` (`qos.py`) - ISCSI map for QoS
* `SAN_DCB_MAP` (`qos.py`) - SAN DCB map for QoS
* `ALT_SAN_DCB` (`qos.py`) - ALT SAN DCB map for QoS
* `ISCSI_POLICY` (`qos.py`) - ISCSI Policy
* `FreeBSDDriverNames` - Enum class of FreeBSD Driver Names
* `DESIGNED_NUMBER_VFS_BY_SPEED` - Designed number of VFs for every speed class, like for 100G NIC is designed 256 VFs
* `SUPPORTED_ADAPTER_RESET_TYPES` - Supporting reset types for NIC. 
* `Milestone` - Enum class of available milestones like `Milestone.PV`

## Usage

```python
from mfd_const import SPEED_IDS
logger.info(f"Device ids for 1G == {SPEED_IDS['@1G']}")

from mfd_const import FREEBSD_ADVERTISE_SPEED
logger.info(f"Value for 1G advertise speed on ix driver is: {FREEBSD_ADVERTISE_SPEED['1G']['ix']}")

from mfd_const import MANAGEMENT_NETWORK
from ipaddress import IPv4Interface
ip = IPv4Interface("10.10.10.10")
for mng_sub in MANAGEMENT_NETWORK:
    if ip in mng_sub:
    logger.info(f"{ip} is management IP.")

# To apply DCB settings related to QOS, please use the flags as below.
from mfd_const.qos import (LOCAL_PFC, LOCAL_DEFAULT_MAP)
res = dcb.verify_dcb(LOCAL_DEFAULT_MAP)
    if res:
        logger.info("DCB Configuration sustains the local settings")
```

## qos
Temporary path for copying tools from SUT/Controller to any host under test
`DCB_TOOL_PATH_LNX : Path for dcbnl.py - Netlink message generation/parsing script`

## Issue reporting

If you encounter any bugs or have suggestions for improvements, you're welcome to contribute directly or open an issue [here](https://github.com/intel/mfd-const/issues).
