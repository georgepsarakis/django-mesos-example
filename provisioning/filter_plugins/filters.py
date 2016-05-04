from __future__ import unicode_literals
import os
import re


def vagrant_status(text):
    regex = r'(?P<vm_name>.+)\s{6}' + \
        r'(?P<status>[a-z\s]+)\s+\((?P<provider>[a-z]+)\)'
    parsed = re.search(regex, text)
    if parsed is not None:
        return parsed.groupdict()


def os_path_abspath(path):
    return os.path.abspath(path)


def os_path_join(*paths):
    return os.path.join(*paths)


class FilterModule(object):
    def filters(self):
        return {
            'vagrant_status': vagrant_status,
            'os_path_abspath': os_path_abspath,
            'os_path_join': os_path_join
        }
