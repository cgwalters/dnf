# repo.py
# DNF Repository objects.
#
# Copyright (C) 2013  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

import dnf.yum.config

class Repo(dnf.yum.config.RepoConf):
    def __init__(self, id_):
        super(Repo, self).__init__()
        self.id = id_
        self.basecachedir = None
        self.fallback_basecachedir = None
        self.base_persistdir = ""
        self.yumvar = {} # empty dict of yumvariables for $string replacement

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def set_failure_callback(self, cb):
        pass

    def set_interrupt_callback(self, cb):
        pass

    def set_progress_bar(self, cb):
        pass