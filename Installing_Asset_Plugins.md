# Introduction to Business API ecosystem

.fx: cover

@conwet

---
# Running the Business API Ecosystem

## Running the APIs and the RSS

Both the TM Forum APIs and the RSS are deployed in Glassfish; in this
regard, the only step for running them is starting Glassfish :

	!bash
    $ asadmin start-domain

---
## Running the Charging Backend

The Charging Backend creates some objects and connections on startup; in
this way, the Glassfish APIs must be up an running before starting it.

The Charging Backend can be started using the *runserver* command as
follows :

	!bash
    $ ./manage.py runserver 127.0.0.1:<charging_port>

---
## Running the Charging Backend

Or in background :

   !bash
    $ nohup ./manage.py runserver 127.0.0.1:<charging_port> &

> **note**
> 
> If you have created a virtualenv when installing the backend or used
> the installation script, you will need to activate the virtualenv
> before starting the Charging Backend

---
## Running the Logic Proxy

The Logic Proxy can be started using Node as follows :

    !bash
    $ node server.js

Or if you want to start it in background: :

    $ nohup node server.js &

---
.fx: back-cover

Thanks!

FIWARE                                FIWARE Lab
OPEN APIs FOR OPEN MINDS              Spark your imagination

         www.fiware.org               FIWARE Ops
twitter: @Fiware                      Easing your operations
