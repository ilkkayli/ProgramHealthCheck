# ProgramHealthCheck

Author: ilkkayli
Monitors status of a certain program and re-starts it in case of unplanned shutdown.
I implemented this script when we had a proxy application running on Windows 2008 server and that proxy crashed every now and then preventing connections to Jenkins slaves. Script re-started the proxy when it crashed.


Prerequisities: Python 2, not tested with Python 3.