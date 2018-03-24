#!/bin/sh
### BEGIN INIT INFO
# Provides: TESTdaemon
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: daemon per TEST 0.1
# Description: descrizione del servizio con avvio automatico.
### END INIT INFO
 
NAME=test
DAEMON=/home/pi/ortensia_ws/bin/run
DAEMON_USER=root
DESC="Esempio di servizio test con avvio automatico."
 
test -x $DAEMON || exit 0
 
DIR=/var/run/test
PID=$DIR/$NAME.pid
RETRY=10
 
if test ! -d "$DIR"; then
    sudo mkdir "$DIR"
    sudo chown -R pi:pi "$DIR"
fi
		 
case "$1" in
  start)
    echo "Starting $NAME"
    start-stop-daemon --start --oknodo --pidfile $PID --exec $DAEMON
    ;;
  stop)
    echo -n "Shutting down $NAME"
    start-stop-daemon --stop --quiet --pidfile $PID --retry=TERM/10/KILL/5 && return 0
    start-stop-daemon --stop --oknodo --exec $DAEMON --name $NAME --retry=TERM/10/KILL/5
    ;;
  restart|force-reload)
    echo "Reoload.... $NAME"
    $0 stop
    $0 start
    ;;
  status)
    status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
  *)
    N=/etc/init.d/$NAME
    echo "Usage: $N {start|stop|restart|force-reload}" >&2
    ;;
esac
exit 0
