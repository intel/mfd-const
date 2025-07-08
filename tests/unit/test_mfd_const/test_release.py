# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT

from mfd_const.release import Milestone


def test_milestone_values():
    assert Milestone.ALPHA.value == "Alpha"
    assert Milestone.BETA.value == "Beta"
    assert Milestone.PC.value == "PC"
    assert Milestone.PV.value == "PV"


def test_milestone_names():
    assert Milestone.ALPHA.name == "ALPHA"
    assert Milestone.BETA.name == "BETA"
    assert Milestone.PC.name == "PC"
    assert Milestone.PV.name == "PV"
