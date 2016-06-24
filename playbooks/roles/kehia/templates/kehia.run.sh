#!/usr/bin/env bash

cd {{install_dir}}
source {{venv_dir}}/bin/activate
source {{install_dir}}/env.sh
workers=$(expr $(nproc) \* 2 + 1)

exec gunicorn --workers $workers --bind 127.0.0.1:{{kehia_port}} config.wsgi  --access-logfile {{log_dir}}/gunicorn.access.log --error-logfile {{log_dir}}/gunicorn.error.log --log-level info
