#!/bin/bash
#
# FileLogger
#
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# Functions for dealing with the work log
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

# cat the logfile that we are currently writing to
#
# $1 - display latest $1 lines
#
function wl()
{
    logfile=$(cwl)
    if [ -z "$1" ]; then
        echo "$(cat $logfile)"
    else
        echo "$(cat $logfile | tail -n${1})"
    fi
}

# get the current work log.
function cwl()
{
    echo "$HOME/.worklogs/$(ls $HOME/.worklogs | sort -r | head -n1)"
}
