# -*- coding: utf-8 -*-
#
# Copyright 2015 - Zector Labs
#
# This file is part of Amaru.
#
# Amaru is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Amaru is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Amaru; If not, see <http://www.gnu.org/licenses/>.

""" ¡Rock and Roll! """

import sys
import os
from PyQt5.QtWidgets import QApplication
from amaru.ui.main import Amaru
from amaru.core import logger
# Logger
log = logger.get_logger(__name__)

amaru_dir = os.path.dirname(__file__)
style = os.path.join(amaru_dir, "resources", "themes", "amaru_dark.qss")


def rock_and_roll():
    qapp = QApplication(sys.argv)

    # Show GUI
    log.debug("Showing GUI...")
    gui = Amaru()
    gui.setMinimumSize(700, 500)
    gui.show()

    # StyleSheet
    log.debug("Aply style sheet...")
    with open(style, mode='r') as f:
        qapp.setStyleSheet(f.read())

    sys.exit(qapp.exec_())