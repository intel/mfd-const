# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
"""Tests for `mfd_const` package."""


class TestMfdConst:
    def test_pass(self):
        assert True

    def test_designed_number_vfs_by_speed(self):
        from mfd_const.network import DESIGNED_NUMBER_VFS_BY_SPEED

        _ = DESIGNED_NUMBER_VFS_BY_SPEED.items()
