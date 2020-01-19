#
# Copyright (C) 2010 Red Hat, Inc.
# Authors:
# Thomas Woerner <twoerner@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os, sys

def firewalld_active():
    chkconfig_status = os.system("/sbin/chkconfig firewalld >&/dev/null")
    service_status = os.system("/sbin/service firewalld status >&/dev/null")

    if chkconfig_status + service_status == 0:
        return True

    if not os.path.exists("/var/run/firewalld.pid"):
        return False

    try:
        fd = open("/var/run/firewalld.pid", "r")
        pid = fd.readline()
        fd.close()
    except:
        return False

    if not os.path.exists("/proc/%s" % pid):
        return False

    try:
        fd = open("/proc/%s/cmdline" % pid, "r")
        cmdline = fd.readline()
        fd.close()
    except:
        return False

    if "firewalld" in cmdline:
        return True

    return False

def firewalld_check():
    if firewalld_active():
        print _("ERROR: FirewallD is active, please use firewall-cmd.")
        sys.exit(1)
