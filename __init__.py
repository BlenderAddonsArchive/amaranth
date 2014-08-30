#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""
Amaranth

Using Blender every day, you get to change little things on it to speedup
your workflow. The problem is when you have to switch computers with
somebody else's Blender, it sucks.
That's the main reason behind Amaranth. I ported all sort of little changes
I find useful into this addon.

What is it about? Anything, whatever I think it can speedup workflow,
I'll try to add it. Enjoy <3
"""

import sys

from . import prefs
from .scene import refresh, save_reload, current_blend, stats
from .animation import timeline_extra_info, frame_current
from .node_editor import id_panel, display_image, templates, simplify_nodes, node_stats
from .render import border_camera, meshlights, passepartout, only_render, unsimplify
from .modeling import symmetry_tools
from .misc import dopesheet_grapheditor, color_management

bl_info = {
    "name": "Amaranth Toolset",
    "author": "Pablo Vazquez, Bassam Kurdali, Sergey Sharybin, Lukas Tönne, Cesar Saez",
    "version": (0, 9, 6),
    "blender": (2, 71),
    "location": "Everywhere!",
    "description": "A collection of tools and settings to improve productivity",
    "warning": "",
    "wiki_url": "http://pablovazquez.org/amaranth",
    "tracker_url": "",
    "category": "Scene",
}


def _call_globals(attr_name):
    for m in globals().values():
        if hasattr(m, attr_name):
            getattr(m, attr_name)()


def _flush_modules(pkg_name):
    for k in tuple(sys.modules.keys()):
        if pkg_name in k:
            del sys.modules[k]


def register():
    _call_globals("register")


def unregister():
    _call_globals("unregister")
    _flush_modules("amaranth")  # reload amaranth
