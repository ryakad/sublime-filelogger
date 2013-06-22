#
# FileLogger
#
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# Logs where time based on what file is active in sublime. Logs are stored
# in $HOME/worklogs/[DATE]
#
# Bash function for viewing current work log from the command line.
#
# function wl()
# {
#     logfile="$HOME/.worklogs/$(ls $HOME/worklogs | sort -r | head -n1)"
#     echo -e "\nCurrent Log File: $logfile\n\n$(cat $logfile)\n"
# }
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import sublime_plugin
import time
import datetime
import os


class FileLogger(sublime_plugin.EventListener):
    """
    Keeps track of what files are being worked on at what times.

    This provides a blunt method for tracking time based on what files are
    being used through sublime text.
    """
    timestart = 0
    timeend = 0
    lastfile = ''

    def on_activated(self, view):
        self.timestart = time.time()

    def on_deactivated(self, view):
        self.timeend = time.time()
        if view.file_name() != self.lastfile and view.file_name() and self.timestart:
            # name the file after the start date
            file_name = datetime.datetime.fromtimestamp(self.timestart).strftime('%Y-%m-%d')

            start = datetime.datetime.fromtimestamp(self.timestart).strftime('%H:%M:%S')
            end = datetime.datetime.fromtimestamp(self.timeend).strftime('%H:%M:%S')

            directory = os.getenv("HOME") + "/.worklogs"
            if not os.path.exists(directory):
                os.makedirs(directory)

            f = open(directory + "/" + file_name, 'a+')
            f.write(str(start) + "\t" + str(end) + "\t" + str(view.file_name()) + "\n")

        self.lastfile = view.file_name()
