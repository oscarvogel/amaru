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


from collections import OrderedDict

""" Actions """

MENU = OrderedDict()

# Menu File
MENU['file'] = {
    "text": "&File",
    "items": [{
            "text": "New",
            "shortcut": "Ctrl+N",
            "triggered": "main_container:new_file"
        }, {
            "text": "Open...",
            "shortcut": "Ctrl+O",
            "triggered": "main_container:open_file"
        }, {
            "text": "Open folder...",
            "shortcut": "",
            "triggered": "main_container:open_folder"
        }, "-", {
            "text": "Save",
            "shortcut": "Ctrl+S",
            "triggered": "main_container:save_file"
        }, {
            "text": "Save As",
            #"shortcut": "save-as",
            "triggered": "main_container:save_file_as"
        }, {
            "text": "Save All",
            "triggered": "main_container:save_all"
        }, "-", {
            "text": "Close",
            "shortcut": "Ctrl+W",
            "triggered": "main_container:close_file"
        }, {
            "text": "Close Others",
            #"shortcut": "close-current",
            "triggered": "main_container:close_others"
        }, {
            "text": "Close All",
            #"shortcut": "close-all",
            "triggered": "main_container:close_all_files"
        }, "-", {
            "text": "Quit",
            "shortcut": "Ctrl+Q",
            "triggered": "close"}]}

# Menu Edit
MENU['edit'] = {
    "text": "&Edit",
    "items": [{
            "text": "Undo",
            "shortcut": "Ctrl+Z",
            "triggered": ""
        }, {
            "text": "Redo",
            "shortcut": "Ctrl+Y",
            "triggered": ""
        }, "-", {
            "text": "Cut",
            "shortcut": "Ctrl+X",
            "triggered": ""
        }, {
            "text": "Copy",
            "shortcut": "Ctrl+C",
            "triggered": ""
        }, {
            "text": "Paste",
            "shortcut": "Ctrl+V",
            "triggered": ""
        }, "-", ]}

# Menu View
MENU['view'] = {
    "text": "&View",
    "items": [{
            "text": "Full Screen Mode",
            "shortcut": "Ctrl+F11",
            "triggered": "show_full_screen_mode"
        }, "-", {
            "text": "Show Lateral",
            "shortcut": "F2",
            "triggered": "show_hide_lateral"
        }, {
            "text": "Show Tabs",
            "shortcut": "",
            "triggered": "main_container:visibility_tab_bar"
        }, {
            "text": "Show Status Bar",
            "shortcut": "",
            "triggered": "visibility_status_bar"
        }, "-", {
            "text": "Show Spaces",
            "triggered": "main_container:show_whitespaces"
        }, {
            "text": "Show Indentation Guides",
            "triggered": "main_container:show_indentation_guides"
        }, "-", {
            "text": "Split Tabs Horizontally",
            "shortcut": "F10",
            "triggered": "main_container:split_horizontally"
        }, {
            "text": "Split Tabs Vertically",
            "shortcut": "F9",
            "triggered": "main_container:split_vertically"}]}

# Menu Find
MENU['find'] = {
    "text": "F&ind",
    "items": [{
            "text": "Find...",
            "shortcut": "Ctrl+F",
            "triggered": "main_container:find"
        }, {
            "text": "Find Next",
            "triggered": "main_container:find_next"
        }, {
            "text": "Find Previous",
            "triggered": "main_container:find_previous"
        }, "-", {
            "text": "Replace...",
            "shortcut": "Ctrl+H",
            "triggered": "main_container:replace"}]}

# Menu Goto
MENU['goto'] = {
    "text": "&Goto",
    "items": []}

# Menu Help
MENU['help'] = {
    "text": "&Help",
    "items": [{
            "text": "About Qt",
            "triggered": "show_about_qt_dialog"}]}