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

import sys
from PyQt5.QtGui import QFont
#from PyQt5.QtCore import QSettings

platform = sys.platform

# Font
if platform.startswith('linux'):
    DEFAULT_FONT = QFont("Monospace", 12)
elif platform.startswith('win'):
    DEFAULT_FONT = QFont("Courier", 11)
else:
    DEFAULT_FONT = QFont("Monaco", 12)

# Indentation
INDENTATION_WIDTH = 4

TABS = False