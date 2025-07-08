# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
"""Tests for _internal_data_structures."""

import pytest

from mfd_const._internal_data_structures import InternalDict


class TestInternalDataStructures:
    @pytest.fixture
    def internal_dict(self):
        yield InternalDict({"key": "value"})

    def test__getitem__(self, internal_dict):
        assert internal_dict.get("key") == "value"
        assert internal_dict["key"] == "value"

        with pytest.raises(KeyError, match=r".*Please extend dict.*"):
            internal_dict["non_existing_key"]
