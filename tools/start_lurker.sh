#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
DIR=$( dirname "${DIR}" )

case "$1" in
  start)
    screen -dmS maillurker_lurker bash
    screen -S maillurker_lurker -X stuff "export DJANGO_IS_DEBUG=0 && cd $DIR/src && . ../env/bin/activate && python manage.py start_lurking "$(echo -ne '\015')
    echo "Lurker SMTPD is started in screen session"
    ;;
  stop)
    screen -X -S celery_flower kill
    echo "Lurker SMTPD is stopped"
    ;;
  *)
    echo "Usage: start_lurker {start|stop}"
    ;;
esac
