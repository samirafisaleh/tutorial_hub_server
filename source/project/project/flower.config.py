import os
import dotenv

env_file = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), ".env"
)
dotenv.load_dotenv(env_file, override=True)

keyword = "FLOWER_ADDRESS"
if FLOWER_ADDRESS := os.getenv(keyword, None):
    address = FLOWER_ADDRESS
    print(f"{keyword}: ".ljust(40) + str(address))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_ADDRESS


keyword = "FLOWER_AUTH"
if FLOWER_AUTH := os.getenv(keyword, None):
    auth = FLOWER_AUTH
    print(f"{keyword}: ".ljust(40) + str(auth))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_AUTH


keyword = "FLOWER_AUTH_REFRESH"
if FLOWER_AUTH_REFRESH := os.getenv(keyword, None):
    FLOWER_AUTH_REFRESH = int(FLOWER_AUTH_REFRESH)
    auto_refresh = FLOWER_AUTH_REFRESH
    print(f"{keyword}: ".ljust(40) + str(auto_refresh))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_AUTH_REFRESH


keyword = "FLOWER_BASIC_AUTH"
if FLOWER_BASIC_AUTH := os.getenv(keyword, None):
    basic_auth = FLOWER_BASIC_AUTH
    print(f"{keyword}: ".ljust(40) + str(basic_auth))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_BASIC_AUTH


keyword = "FLOWER_BROKER_API"
if FLOWER_BROKER_API := os.getenv(keyword, None):
    broker_api = FLOWER_BROKER_API
    print(f"{keyword}: ".ljust(40) + str(broker_api))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_BROKER_API


keyword = "FLOWER_CA_CERTS"
if FLOWER_CA_CERTS := os.getenv(keyword, None):
    ca_certs = FLOWER_CA_CERTS
    print(f"{keyword}: ".ljust(40) + str(ca_certs))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_CA_CERTS


keyword = "FLOWER_CERTFILE"
if FLOWER_CERTFILE := os.getenv(keyword, None):
    certfile = FLOWER_CERTFILE
    print(f"{keyword}: ".ljust(40) + str(certfile))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_CERTFILE


keyword = "FLOWER_CONF"
if FLOWER_CONF := os.getenv(keyword, None):
    conf = FLOWER_CONF
    print(f"{keyword}: ".ljust(40) + str(conf))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_CONF


keyword = "FLOWER_DB"
if FLOWER_DB := os.getenv(keyword, None):
    db = FLOWER_DB
    print(f"{keyword}: ".ljust(40) + str(db))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_DB


keyword = "FLOWER_DEBUG"
if FLOWER_DEBUG := os.getenv(keyword, None):
    FLOWER_DEBUG = bool(int(FLOWER_DEBUG))
    debug = FLOWER_DEBUG
    print(f"{keyword}: ".ljust(40) + str(debug))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_DEBUG


keyword = "FLOWER_ENABLE_EVENTS"
if FLOWER_ENABLE_EVENTS := os.getenv(keyword, None):
    FLOWER_ENABLE_EVENTS = bool(int(FLOWER_ENABLE_EVENTS))
    enable_events = FLOWER_ENABLE_EVENTS
    print(f"{keyword}: ".ljust(40) + str(enable_events))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_ENABLE_EVENTS


keyword = "FLOWER_FORMAT_TASK"
if FLOWER_FORMAT_TASK := os.getenv(keyword, None):
    format_task = FLOWER_FORMAT_TASK
    print(f"{keyword}: ".ljust(40) + str(format_task))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_FORMAT_TASK


keyword = "FLOWER_INSPECT_TIMEOUT"
if FLOWER_INSPECT_TIMEOUT := os.getenv(keyword, None):
    inspect_timeout = FLOWER_INSPECT_TIMEOUT
    print(f"{keyword}: ".ljust(40) + str(inspect_timeout))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_INSPECT_TIMEOUT


keyword = "FLOWER_KEYFILE"
if FLOWER_KEYFILE := os.getenv(keyword, None):
    keyfile = FLOWER_KEYFILE
    print(f"{keyword}: ".ljust(40) + str(keyfile))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_KEYFILE


keyword = "FLOWER_MAX_WORKERS"
if FLOWER_MAX_WORKERS := os.getenv(keyword, None):
    FLOWER_MAX_WORKERS = int(FLOWER_MAX_WORKERS)
    max_workers = FLOWER_MAX_WORKERS
    print(f"{keyword}: ".ljust(40) + str(max_workers))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_MAX_WORKERS


keyword = "FLOWER_MAX_TASKS"
if FLOWER_MAX_TASKS := os.getenv(keyword, None):
    FLOWER_MAX_TASKS = int(FLOWER_MAX_TASKS)
    max_tasks = FLOWER_MAX_TASKS
    print(f"{keyword}: ".ljust(40) + str(max_tasks))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_MAX_TASKS


keyword = "FLOWER_NATURAL_TIME"
if FLOWER_NATURAL_TIME := os.getenv(keyword, None):
    FLOWER_NATURAL_TIME = bool(int(FLOWER_NATURAL_TIME))
    natural_time = FLOWER_NATURAL_TIME
    print(f"{keyword}: ".ljust(40) + str(natural_time))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_NATURAL_TIME


keyword = "FLOWER_PERSISTENT"
if FLOWER_PERSISTENT := os.getenv(keyword, None):
    FLOWER_PERSISTENT = bool(int(FLOWER_PERSISTENT))
    persistent = FLOWER_PERSISTENT
    print(f"{keyword}: ".ljust(40) + str(persistent))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_PERSISTENT


keyword = "FLOWER_PORT"
if FLOWER_PORT := os.getenv(keyword, None):
    FLOWER_PORT = int(FLOWER_PORT)
    port = FLOWER_PORT
    print(f"{keyword}: ".ljust(40) + str(port))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_PORT


keyword = "FLOWER_STATE_SAVE_INTERVAL"
if FLOWER_STATE_SAVE_INTERVAL := os.getenv(keyword, None):
    FLOWER_STATE_SAVE_INTERVAL = int(FLOWER_STATE_SAVE_INTERVAL)
    state_save_interval = FLOWER_STATE_SAVE_INTERVAL
    print(f"{keyword}: ".ljust(40) + str(state_save_interval))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_STATE_SAVE_INTERVAL


keyword = "FLOWER_STATE_SAVE_INTERVAL"
if FLOWER_XHEADERS := os.getenv(keyword, None):
    FLOWER_XHEADERS = bool(int(FLOWER_XHEADERS))
    xheaders = FLOWER_XHEADERS
    print(f"{keyword}: ".ljust(40) + str(xheaders))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_XHEADERS


keyword = "FLOWER_TASKS_COLUMNS"
if FLOWER_TASKS_COLUMNS := os.getenv(keyword, None):
    tasks_columns = FLOWER_TASKS_COLUMNS
    print(f"{keyword}: ".ljust(40) + str(tasks_columns))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_TASKS_COLUMNS


keyword = "FLOWER_URL_PREFIX"
if FLOWER_URL_PREFIX := os.getenv(keyword, None):
    url_prefix = FLOWER_URL_PREFIX
    print(f"{keyword}: ".ljust(40) + str(url_prefix))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_URL_PREFIX


keyword = "FLOWER_UNIX_SOCKET"
if FLOWER_UNIX_SOCKET := os.getenv(keyword, None):
    unix_socket = FLOWER_UNIX_SOCKET
    print(f"{keyword}: ".ljust(40) + str(unix_socket))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_UNIX_SOCKET


keyword = "FLOWER_UNIX_SOCKET"
if FLOWER_COOKIE_SECRET := os.getenv(keyword, None):
    cookie_secret = FLOWER_COOKIE_SECRET
    print(f"{keyword}: ".ljust(40) + str(cookie_secret))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_COOKIE_SECRET


keyword = "FLOWER_AUTH_PROVIDER"
if FLOWER_AUTH_PROVIDER := os.getenv(keyword, None):
    auth_provider = FLOWER_AUTH_PROVIDER
    print(f"{keyword}: ".ljust(40) + str(auth_provider))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_AUTH_PROVIDER


keyword = "FLOWER_PURGE_OFFLINE_WORKERS"
if FLOWER_PURGE_OFFLINE_WORKERS := os.getenv(keyword, None):
    purge_offline_workers = FLOWER_PURGE_OFFLINE_WORKERS
    print(f"{keyword}: ".ljust(40) + str(purge_offline_workers))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_PURGE_OFFLINE_WORKERS


keyword = "FLOWER_TASK_RUNTIME_METRICS_BUCKETS"
if FLOWER_TASK_RUNTIME_METRICS_BUCKETS := os.getenv(keyword, None):
    task_runtime_metric_buckets = FLOWER_TASK_RUNTIME_METRICS_BUCKETS
    print(f"{keyword}: ".ljust(40) + str(task_runtime_metric_buckets))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_TASK_RUNTIME_METRICS_BUCKETS


keyword = "FLOWER_OAUTH2_KEY"
if FLOWER_OAUTH2_KEY := os.getenv(keyword, None):
    oauth2_key = FLOWER_OAUTH2_KEY
    print(f"{keyword}: ".ljust(40) + str(oauth2_key))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_OAUTH2_KEY


keyword = "FLOWER_OAUTH2_SECRET"
if FLOWER_OAUTH2_SECRET := os.getenv(keyword, None):
    oauth2_secret = FLOWER_OAUTH2_SECRET
    print(f"{keyword}: ".ljust(40) + str(oauth2_secret))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_OAUTH2_SECRET


keyword = "FLOWER_REDIRECT_URI"
if FLOWER_REDIRECT_URI := os.getenv(keyword, None):
    redirect_uri = FLOWER_REDIRECT_URI
    print(f"{keyword}: ".ljust(40) + str(redirect_uri))
else:
    print(f"{keyword}: ".ljust(40) + "(default)")
del FLOWER_REDIRECT_URI
