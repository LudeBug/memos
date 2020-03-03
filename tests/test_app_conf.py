#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import pytest
import configparser

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from memos import app_conf

CONF_PATH = "conf/app.conf"
config_ini = configparser.ConfigParser()
config_ini.read(CONF_PATH, encoding="utf-8")

def test_conf_get_001():
    conf_001 = config_ini.get("env", "editor")
    assert app_conf.get_config("editor") == conf_001
    

