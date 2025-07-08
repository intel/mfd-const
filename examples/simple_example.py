# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT

# Put here only the dependencies required to run the module.
# Development and test requirements should go to the corresponding files.
"""Simple example of usage."""

import logging

from mfd_const import SPEED_IDS, Milestone
from mfd_const import FREEBSD_ADVERTISE_SPEED

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Device ids for 1G == {SPEED_IDS['@1G']}")
logger.info(
    f"Value for 1G advertise speed on ix driver is: {FREEBSD_ADVERTISE_SPEED['1G']['ix']}"
)
logger.info(f"Milestone: {Milestone.ALPHA}")