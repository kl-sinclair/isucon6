bind = 'unix:/tmp/gunicorn_isucon.sock'
backlog = 2048

workers = 10
worker_class = 'sync'
threads = 1500
worker_connections = 1500
timeout = 30
keepalive = 2

daemon = False
raw_env = [
]
pidfile = '/tmp/gunicorn.pid'
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = '/tmp/gunicorn.error.log'
#errorlog = '-'
loglevel = 'info'
accesslog = '/tmp/gunicorn.access.log'
#accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
