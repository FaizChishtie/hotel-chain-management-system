import re
CURRENT_USER = None
WHICH_CONFIG = 'CONFIG'


USERNAME = re.search(
    '^USERNAME\s*=\s*"([^"]+)"',
    open(WHICH_CONFIG).read(),
    re.M
    ).group(1)

PASSWORD = re.search(
    '^PASSWORD\s*=\s*"([^"]+)"',
    open(WHICH_CONFIG).read(),
    re.M
    ).group(1)

DATA = [['Empty']]

HEADER = ['Empty']