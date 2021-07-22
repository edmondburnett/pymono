SERVICE_NAME = "api"
PG_HOSTNAME = "localhost"

try:
    from local_settings import *
except ImportError:
    pass