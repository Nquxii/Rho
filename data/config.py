import json
import os
import sys
from dotenv import load_dotenv

# define file directories
script_dir = os.path.dirname(__file__)
config_path = 'config.json'
config_file = os.path.join(script_dir, config_path)

# load dotenv
load_dotenv()

# bot properties
discordtoken = str(os.getenv('TOKEN'))
owner = str(os.getenv('owner'))
prefix = str(os.getenv('default_prefix'))
server = str(os.getenv('guildID'))

if not discordtoken:
    sys.exit(".env file with token not found")
