APACHE_CONF = '/path/to/apache2.conf'
SERVER_ROOTS = ('/srv/www/server1', '/srv/www/server2')
BEGIN_SENTINEL = '# BEGIN no-htaccess'
END_SENTINEL = '# END no-htaccess'
CONFIG_NAME = '.htaccess'

all_configs = {}

def read_file(path):
    with open(str(path)) as file:
        return [l.rstrip() for l in file.readlines()]

from pathlib import Path
for root in SERVER_ROOTS:
    for path in Path(root).rglob(CONFIG_NAME):
        directory = str(path.parent)
        lines = read_file(path)
        all_configs[directory] = lines   

def print_all_configs():
    for root in SERVER_ROOTS:
        print('<Directory ' + root + '/>')
        print('  AllowOverride none')
        print('</Directory>')
    for directory in all_configs.keys():
        print('<Directory ' + directory + '/>')
        for line in all_configs[directory]:
            print('  ' + line)
        print('</Directory>')

BEFORE = 0
INSIDE = 1
AFTER = 2
state = BEFORE

for line in read_file(APACHE_CONF):
    if state == BEFORE:
        print(line)
        if line == BEGIN_SENTINEL:
            state = INSIDE
            print_all_configs()
    elif state == INSIDE:
        if line == END_SENTINEL:
            print(line)
            state = AFTER
    elif state == AFTER:
        print(line)

