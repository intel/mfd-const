# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
"""Tests for `mfd_const` package."""


class TestMfdConst:
    def test_pass(self):
        assert True

    def test_designed_number_vfs_by_speed(self):
        from mfd_const.network import DESIGNED_NUMBER_VFS_BY_SPEED

        _ = DESIGNED_NUMBER_VFS_BY_SPEED.items()

    def test_e835_device_ids_in_cnv_family(self):
        """Test that E835 device IDs are included in Family.CNV."""
        from mfd_const.network import DEVICE_IDS, Family

        e835_device_ids = [
            "0x1248",  # E835-CC for backplane
            "0x1261",  # E835-C for backplane
            "0x1265",  # E835-L for backplane
            "0x1249",  # E835-CC for QSFP
            "0x1262",  # E835-C for QSFP
            "0x1266",  # E835-L for QSFP
            "0x124A",  # E835-CC for SFP
            "0x1263",  # E835-C for SFP
            "0x1267",  # E835-L for SFP
        ]

        cnv_devices = DEVICE_IDS[Family.CNV.name]
        for device_id in e835_device_ids:
            assert device_id in cnv_devices, f"Device ID {device_id} not found in Family.CNV"

    def test_e835_device_ids_in_100g_nicinstaller(self):
        """Test that E835 device IDs are included in DEVID_CLASS_MAP_NICINSTALLER['100G']."""
        from mfd_typing import DeviceID

        from mfd_const.network import DEVID_CLASS_MAP_NICINSTALLER

        e835_device_ids = [
            DeviceID(0x1248),  # E835-CC for backplane
            DeviceID(0x1261),  # E835-C for backplane
            DeviceID(0x1265),  # E835-L for backplane
            DeviceID(0x1249),  # E835-CC for QSFP
            DeviceID(0x1262),  # E835-C for QSFP
            DeviceID(0x1266),  # E835-L for QSFP
            DeviceID(0x124A),  # E835-CC for SFP
            DeviceID(0x1263),  # E835-C for SFP
            DeviceID(0x1267),  # E835-L for SFP
        ]

        nicinstaller_100g = DEVID_CLASS_MAP_NICINSTALLER["100G"]
        for device_id in e835_device_ids:
            assert device_id in nicinstaller_100g, f"Device ID {device_id} not found in 100G class"

    def test_e835_device_ids_in_ice_driver(self):
        """Test that E835 device IDs are included in DRIVER_DEVICE_ID_MAP['ice']."""
        from mfd_typing import DeviceID

        from mfd_const.network import DRIVER_DEVICE_ID_MAP

        e835_device_ids = [
            DeviceID(0x1248),  # E835-CC for backplane
            DeviceID(0x1261),  # E835-C for backplane
            DeviceID(0x1265),  # E835-L for backplane
            DeviceID(0x1249),  # E835-CC for QSFP
            DeviceID(0x1262),  # E835-C for QSFP
            DeviceID(0x1266),  # E835-L for QSFP
            DeviceID(0x124A),  # E835-CC for SFP
            DeviceID(0x1263),  # E835-C for SFP
            DeviceID(0x1267),  # E835-L for SFP
        ]

        ice_devices = DRIVER_DEVICE_ID_MAP["ice"]
        for device_id in e835_device_ids:
            assert device_id in ice_devices, f"Device ID {device_id} not found in ice driver map"
