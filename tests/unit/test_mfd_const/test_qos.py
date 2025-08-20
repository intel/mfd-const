# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
import mfd_const.qos as qos


def test_local_ets_constant():
    assert qos.LOCAL_ETS == "ETS"


def test_local_pfc_constant():
    assert qos.LOCAL_PFC == "PFC"


def test_local_app_constant():
    assert qos.LOCAL_APP == "APP"


def test_remote_ets_constant():
    assert qos.REMOTE_ETS == "Remote_ETS"


def test_dcb_tool_path_lnx():
    assert qos.DCB_TOOL_PATH_LNX == r"/tmp/tools/dcb"


def test_nic_registry_base_path_dcb():
    assert r"{4d36e972-e325-11ce-bfc1-08002be10318}" in qos.NIC_REGISTRY_BASE_PATH_DCB


def test_local_default_map_structure():
    assert qos.LOCAL_ETS in qos.LOCAL_DEFAULT_MAP
    assert qos.LOCAL_PFC in qos.LOCAL_DEFAULT_MAP
    assert isinstance(qos.LOCAL_DEFAULT_MAP[qos.LOCAL_ETS], dict)
    assert isinstance(qos.LOCAL_DEFAULT_MAP[qos.LOCAL_PFC], list)
    assert len(qos.LOCAL_DEFAULT_MAP[qos.LOCAL_PFC]) == 8


def test_local_iscsi_map_bandwidths():
    ets = qos.LOCAL_ISCSI_MAP[qos.LOCAL_ETS]
    assert ets["0"]["Bandwidth"] == 20
    assert ets["1"]["Bandwidth"] == 20
    assert ets["2"]["Bandwidth"] == 60


def test_san_dcb_map_priorities():
    pfc = qos.SAN_DCB_MAP[qos.LOCAL_PFC]
    assert pfc[3] is True
    assert pfc[4] is True
    assert all(isinstance(val, bool) for val in pfc)


def test_alt_san_dcb_app():
    app = qos.ALT_SAN_DCB[qos.LOCAL_APP]
    assert "3260" in app
    assert app["3260"]["Priority"] == 4
    assert app["3260"]["Protocol"] == "TCP"


def test_iscsi_policy():
    assert "UP4" in qos.ISCSI_POLICY
    up4 = qos.ISCSI_POLICY["UP4"]
    assert up4["Template"] == "iSCSI"
    assert up4["PriorityValue"] == "4"
