import sys
import os
import configparser

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

CONF_PATH = "conf/app.conf"
config_ini = configparser.ConfigParser()
config_ini.read(CONF_PATH, encoding="utf-8")

def get_config(key: str):
    re_property = None
    if key in "editor":
        re_property = config_ini.get("env", "editor")
    return re_property
    
