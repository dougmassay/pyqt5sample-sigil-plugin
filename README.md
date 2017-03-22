PyQt5Sample
============

Sample Sigil plugin utilizing PyQt5 gui elements and basic translations.


Links
=====

* Sigil website is at <http://sigil-ebook.com>
* Sigil support forums are at <http://www.mobileread.com/forums/forumdisplay.php?f=203>

Building
========

First, clone the repo:

    $ git clone https://github.com/dougmassay/pyqt5sample-sigil-plugin.git

To generate *.ts file to be used for transaltions purpose,run the updatetsfiles script (this must be done anytime the python code is altered so that strings to be translated get moved to different lines of code).

    $python ./updatetsfiles (or just ./updatetsfiles if Python is on your PATH)

To create the plugin zip file, run the buildplugin script (root of the repository tree) with Python (2 or 3)

    $python ./buildplugin (or just ./buildplugin if Python is on your PATH)

This will create the PyQt5Sample_vX.X.X.zip file that can then be installed into Sigil's plugin manager.

Using NCXRemove
=================

Nothing to see, here really. It's a sample plugin. Run it and click the button.

* **language_override** : text value (defaults to Null). Change this to a language code (like en_US) if you don't want this plugin to try to use Sigil's UI language to find its translations (if any exist).

What's going on with translations?
=================

- There's lot's of documentation in the dialogs.py file file to get you going. A quick rundown on how to create/include language file to translate your plugin's gui to other languages.

- You'll need the Qt5 developers tools as well as PyQt5 dev tools to generate *.ts files from your code. See the documentation in dialogs.py to see how text is marked for translation.

- You use the pylupdate5 command (installed with PyQt5) to generate the .ts files from your code See the "updatetsfiles" script to see how I automate this process for my plugin (this must be done any time the python code is altered so that strings to be translated get moved to different lines of code).

- Then someone uses QtLinguist to edit the .ts files and add the translated text.

- Once the .ts files have been updated with the translated text, you use Qt5's lrelease tool to convert/compile the .ts files to .qm dictionaries that can be included with your plugin. I automate this process in the "buildplugin" script.

- Install the translator object early in your--as early as possible (line 40-57 of the dialogs.py file) to make your various .qm file avilable to your plugin.


Contributing / Modifying
============
From here on out, a proficiency with developing / creating Sigil plugins is assumed.
If you need a crash-course, an introduction to creating Sigil plugins is available at
http://www.mobileread.com/forums/showthread.php?t=251452.

The core plugin files (this is where most contributors will spend their time) are:

    > plugin.py
    > dialogs
    > plugin.xml


Files used for building/maintaining the plugin:

    > buildplugin  -- this is used to build the plugin.
    > setup.cfg -- used for flake8 style checking. Use it to see if your code complies.
    > updatetsfiles -- used to generate/update the ts files for use in QtLinguist



License Information
=======

###PyQt5Sample

Available under the terms of the [MIT license](http://opensource.org/licenses/mit-license.php)


Copyright (c) 2016 Doug Massay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
