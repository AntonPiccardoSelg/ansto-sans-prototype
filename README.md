# Bilby Gui

[![Build Status](https://travis-ci.org/ANSTO-ACNS/bilby-gui.svg?branch=master)](https://travis-ci.org/ANSTO-ACNS/bilby-gui)

[![Coverage Status](https://coveralls.io/repos/github/ANSTO-ACNS/bilby-gui/badge.svg?branch=master)](https://coveralls.io/github/ANSTO-ACNS/bilby-gui?branch=master)


## Description

The Bilby Gui is a graphical user interface which allows Bilby users to setup and run reductions from within
[Mantid](http://www.mantidproject.org/Main_Page). It is provided as an external project which is meant to be used as a type of plugin for Mantid.


## Starting the Bilby Gui from Mantid

Before starting the Bilby Gui the first time, it has to be registered as a "plugin" in Mantid. The steps to achieve this are:
1. Get a copy of the Bilby Gui repository on your local machine
1. Open MantidPlot
1. Open `View > Manage Custom Menus ...`
1. Press `Add Scipt`
1. Select the path to `bilby.py` of you local copy of the Bilby Gui and press `Open`
1. Press `Add Menu`
1. Type *Ansto* and press `Ok`
1. Select *bilby* from the *Python Scripts* field and *Ansto* from the *Custom Menus* field
1. Press the `>>` button
1. Press `Ok`

You can now open the Bilby Gui whenever you press *Ansto > bilby*

The Bilby Gui depends on [Mantid's](http://www.mantidproject.org/Main_Page) Python configuration, hence an installed version of Mantid is required.

## Developing the Bilby Gui

As mentioned above, the Bilby Gui depends on Manitd's Python. There are several helper scripts which allow you to run the Bilby Gui
without opening MantidPlot. They are platform (Windows/Linux) specific and are discussed below.

There are some packages required which are not provided by Mantid's Python and
will have to install them via
`pip install -r path_to_bilby_gui/pip-requirements-dev.txt`.

#### Windows

For Windows the Bilby Gui assumes by default that you have a version of Mantid installed here: `C:\MantidInstall\`.
Should your copy of Mantid be installed somewhere else then you will have to edit the following scripts:
* start_ansto.bat
* test_runner.bat

Both make explicit use of `C:\MantidInstall\bin\mantidpython.bat`. If your Mantid installation is located in `my_path`,
change this to `my_path\bin\mantidpython.bat`.

##### Opening the Bilby Gui as a standalone

The Bilby Gui can be openend without envoking `MantidPlot` beforehand. This can be achieved by executing `start_ansto.bat`.
Note that integral elements such as MantidDock are not available in this case.

##### Running unit test

The unit tests can be executed by executing `test_runner.bat`

#### Linux

For Linux the Bilby Gui assumes by default that you have a version of Mantid installed here: `/opt/mantidnightly/`.

Should your copy of Mantid be installed somewhere else then you will have to edit the following scripts:
* start_ansto.sh
* test_runner.sh

Both make explicit use of `/opt/mantidnightly/bin/mantidpython`. If your Mantid installation is located in `my_path`, change this to `my_path/bin/mantidpython`.

##### Opening the Bilby Gui as a standalone

The Bilby Gui can be openend with envoking `MantidPlot` beforehand. This can be achieved by executing `start_ansto.sh`.
Note that integral elements such as MantidDock are not available in this case.

##### Running unit test

The unit tests can be executed by executing `test_runner.sh`
