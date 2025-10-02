from os import getenv
from sys import stderr, exit as sys_exit

GOTIFY_URL = getenv("GOTIFY_URL", "https://g.bvip.eu.org")
GOTIFY_TOKEN = getenv("GOTIFY_TOKEN", "CfK1Qs0PjSfTBxy")

if not GOTIFY_TOKEN:
    print("GOTIFY_TOKEN not set", file=stderr, flush=True)
    sys_exit(1)

