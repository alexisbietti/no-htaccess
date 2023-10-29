# no-htaccess
This script scans all .htaccess files in a server directory and generates an apache2.conf containing all their directives.
It's faster than scanning the server tree for overrides for every request.

## Usage
python no-htaccess.py > apache2.conf

## Prerequisite
Instrument your apache2.conf file with two markers lines:
* `# BEGIN no-htaccess`
* `# END no-htaccess`

The .htaccess directives will be inserted between these lines.
