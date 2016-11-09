#!/bin/sh

ADDRESS='127.0.0.1'
GUNICORN="/path/to/project/env/bin/gunicorn"
PROJECTLOC="/path/to/project/src"
MANAGELOC="$PROJECTLOC/manage.py"
DEFAULT_ARGS="wsgi:application -c gunicorn.py --daemon --bind=$ADDRESS:"

BASE_CMD="$GUNICORN $DEFAULT_ARGS"

SERVER_PORT='8000'
SERVER_PID="$PROJECTLOC/server-$SERVER_PORT.pid"


start_server () {
  if [ -f $1 ]; then
    #pid exists, check if running
    if [ "$(ps -p `cat $1` | wc -l)" -gt 1 ]; then
       echo "Server already running on ${ADDRESS}:${2}"
       return
    fi
  fi
  export DJANGO_IS_DEBUG=0
  cd $PROJECTLOC
  #Activate virtualenv
  . ../env/bin/activate

  echo "starting ${ADDRESS}:${2}"
  $BASE_CMD$2 --pid=$1
}


stop_server (){
  if [ -f $1 ] && [ "$(ps -p `cat $1` | wc -l)" -gt 1 ]; then
    echo "stopping server ${ADDRESS}:${2}"
    kill -9 `cat $1`
    rm $1
  else
    if [ -f $1 ]; then
      echo "server ${ADDRESS}:${2} not running"
    else
      echo "No pid file found for server ${ADDRESS}:${2}"
    fi
  fi
}


case "$1" in
'start')
  start_server $SERVER_PID $SERVER_PORT
  ;;
'stop')
  stop_server $SERVER_PID $SERVER_PORT
  ;;
'restart')
  stop_server $SERVER_PID $SERVER_PORT
  sleep 10
  start_server $SERVER_PID $SERVER_PORT
  ;;
*)
  echo "Usage: $0 { start | stop | restart }"
  ;;
esac

exit 0
