# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

import os
import sys


prefs = {}

def run(bk):
    global prefs

    supports_pyqt = (bk.launcher_version() >= 20170115)
    if supports_pyqt:
        from dialogs import launch_gui
    else:
        print('Plugin requires a newer version of Sigil.')
        return -1

    prefs = bk.getPrefs()

    # set default preference values
    if 'language_override' not in prefs:
        prefs['language_override'] = None
    if 'qt_geometry' not in prefs:
        prefs['qt_geometry'] = None
    if 'last_dir' not in prefs:
        prefs['lastDir'] = os.path.expanduser('~')

    # launch PyQt gui
    details = launch_gui(bk, prefs)
    print('Current time: {}'.format(details['time']))
    print('Button pushed: {}'.format(details['button_pushed']))

    return 0

def main():
    print('I reached main when I should not have\n')
    return -1


if __name__ == '__main__':
    sys.exit(main())
