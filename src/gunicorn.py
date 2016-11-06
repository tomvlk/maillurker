"""
Gunicorn Config.
"""
import multiprocessing

bind = '127.0.0.1:8000'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False
