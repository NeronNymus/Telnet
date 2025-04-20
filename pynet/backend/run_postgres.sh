#!/bin/bash

# Run the cluster that resides on Arch if running Ubuntu if running Ubuntu if running Ubuntu if running Ubuntu
sudo -u postgres /usr/lib/postgresql/17/bin/postgres -D /media/Arch/var/lib/postgres/data -p 2356 &

# Then connect to the server for query execution
sudo -u postgres /usr/lib/postgresql/17/bin/psql -h localhost -p 2356
