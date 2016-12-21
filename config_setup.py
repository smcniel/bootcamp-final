import configparser

config = configparser.ConfigParser()

# create config file settings for gmail with 2-step verification
config.add_section('server')
config.set('server', 'hostname', 'imap.gmail.com')
config.set('server', 'port', '993')

config.add_section('account')
# replace username and password with own
config.set('account', 'username', 'youremail@gmail.com')
config.set('account', 'password', 'generated_app_password')

with open('gmail.ini', 'w') as configfile:
    config.write(configfile)
