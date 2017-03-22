# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

from __future__ import unicode_literals, division, absolute_import, print_function

import sys
import os
import binascii
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import pyqtSlot, QCoreApplication, QTranslator, Qt


_DETAILS = {
    'time'          : 'None',
    'button_pushed' : 'False',
    'file_selected' : 'None'
}


def launch_gui(bk, prefs):
    app = QApplication(sys.argv)
    widget = MyWidget(bk, prefs)
    widget.show()
    app.exec_()
    return _DETAILS


# Used to mark strings that should be tranlated if possible
_translate = QCoreApplication.translate

class MyWidget(QWidget):
    def __init__(self, bk, prefs):
        super().__init__()

        self.bk = bk
        self.prefs = prefs

        # Look for  pyqt5sample_<lang_code>.qm in 'translations' folder.
        # if the language code provided is it_IT then translator looks first for a file named
        # "pyqt5sample_it_IT.qm". If that isn't found, it looks for "pyqt5sample_it.qm".
        # If that's not found, the original strings in the code are used.
        translator = QTranslator()

        # Provide a preference override so the user can use a language different
        # from Sigil's UI language for the plugin's strings.
        if prefs['language_override'] is not None:
            print('Looking for language file matching the override from prefs')
            qmf = '{}_{}'.format(bk._w.plugin_name.lower(), prefs['language_override'])
        else:
            print('Looking for language file matching Sigil\'s UI language')
            qmf = '{}_{}'.format(bk._w.plugin_name.lower(), bk.sigil_ui_lang)
        translator.load(qmf, os.path.join(bk._w.plugin_dir, bk._w.plugin_name, 'translations'))
        print('Looking for {} in {}:'.format(qmf, os.path.join(bk._w.plugin_dir, bk._w.plugin_name, 'translations')))
        installed = QApplication.installTranslator(translator)
        print('Translation dictionary is being used: {}'.format(installed))

        self.initUi()

    def initUi(self):
        main_layout = QVBoxLayout(self)

        self.grp_layout = QVBoxLayout()
        self.a_label = QLabel()
        self.a_label.setAlignment(Qt.AlignCenter)
        self.grp_layout.addWidget(self.a_label)
        self.a_button = QPushButton()
        self.a_button.clicked.connect(self._button_clicked)
        self.grp_layout.addWidget(self.a_button)
        main_layout.addLayout(self.grp_layout)

        self.retranslateUi(self)
        # Sigil's json prefs routines can't serialize bytearrays so use binascii encoding/decoding to save/restore Qt window geometry.
        if self.prefs['qt_geometry'] is not None:
            self.restoreGeometry(binascii.a2b_base64(self.prefs['qt_geometry'].encode('ascii')))

    def retranslateUi(self, App):
        # Use PyQt5's pylupdate5 command to generate *.ts files from this file that translators can complete with
        # Qt Linguist. Use Qt's lrelease command to create *.qm files from the completed *.ts files and place them
        # in the plugin's 'translation' folder (make sure to include the 'translation folder with the plugin).
        # Note the naming convention (for this plugin) in the __init__ section (ex: "pyqt5sample_fr.qm").
        self.setWindowTitle(_translate('MyWidget', 'Sample Plugin'))
        self.a_label.setText(_translate('MyWidget', 'Sample Label'))
        self.a_button.setText(_translate('MyWidget', 'Push the button'))

        # Note: you don't have to use a separate retranslateUi class def as I have. You can also use the
        # _translate function in the widget's creation in the initUI directly.
        # ex: self.a_label = QLabel(_translate('MyWidget', 'Sample Label'))


    @pyqtSlot()
    def _button_clicked(self):
        global _DETAILS
        _DETAILS['button_pushed'] = 'True'

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        caption = 'Select file'
        initial_dir = self.prefs['last_dir']
        ffilter = '{} (*.*)'.format('All Files')
        fpath, _ = QFileDialog.getOpenFileName(self, caption, initial_dir, ffilter, options=options)

        if fpath is not None and len(fpath):
            self.prefs['last_dir'] = os.path.dirname(fpath)
            _DETAILS['file_selected'] = fpath

        # Sigil's json prefs routines can't serialize bytearrays so use binascii encoding/decoding to save/restore Qt window geometry.
        self.prefs['qt_geometry'] = binascii.b2a_base64(self.saveGeometry()).decode('ascii')

        _DETAILS['time'] = str(datetime.now())

        self.bk.savePrefs(self.prefs)
        QCoreApplication.instance().quit()
