import json
import os

# define file directories
script_dir = os.path.dirname(__file__)
config_path = 'config.json'
config_file = os.path.join(script_dir, config_path)

# open config file of 
with open(config_file) as f:
    # load configuration file as config
    config = json.load(f)

    # bot properties
    discordtoken = config['SETTINGS']['discordtoken'].strip()
    prefix = config['SETTINGS']['default_prefix'].strip()
    server = int(config['SETTINGS']['guildID'].strip())
    owner = config['SETTINGS']['owner'].strip()