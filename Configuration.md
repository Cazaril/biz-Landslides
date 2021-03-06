# Introduction to Business API ecosystem

.fx: cover

@conwet

---
# Configuration

At this step, the different components of the Business API Ecosystem are
installed. In the case of the TMForum APIs and the RSS, this
installation process has already required to configure their database
connection before their deployment, so they are already configured.
Nevertheless, this section contains an explanation of the function of
the different settings of the RSS properties files.

---
## Configuring the RSS

The RSS has its settings included in two files located at
*/etc/default/rss*. The file *database.properties* contains by default
the following fields:

    database.url=jdbc:mysql://localhost:3306/RSS
    database.username=root
    database.password=root
    database.driverClassName=com.mysql.jdbc.Driver

---
## Configuring the RSS

This file contains the configuration required in order to connect to the
database.

  - database.url: URL used to connect to the database, this URL includes
    the host and port of the database as well as the concrete database
    to be used
  - database.username: User to be used to connect to the database
  - database.password: Password of the database user
  - database.driverClassName: Driver class of the database. By default
    MySQL

---
## Configuring the RSS

The file *oauth.properties* contains by default the following fields (It
is recommended not to modify them) :

    config.grantedRole=Provider
    config.sellerRole=Seller
    config.aggregatorRole=aggregator

---
## Configuring the RSS

This file contains the name of the roles (registered in the idm) that
are going to be used by the RSS.

  - config.grantedRole: Role in the IDM of the users with admin
    privileges
  - config.sellerRole: Role in the IDM of the users with seller
    privileges
  - config.aggregatorRole: Role of the users who are admins of an store
    instance. In the context of the Business API Ecosystem there is only
    a single store instance, so you can safely ignore this flag

---
## Configuring the Charging Backend

The Charging Backend creates some objects and connections in the
different APIs while working, so the first step is configuring the
different URLs of the Business API Ecosystem components by modifying the
file *services\_settings.py*, which by default contains the following
content:

    INVENTORY = 'http://localhost:8080/DSProductInventory'
    ORDERING = 'http://localhost:8080/DSProductOrdering'
    BILLING = 'http://localhost:8080/DSBillingManagement'
    RSS = 'http://localhost:8080/DSRevenueSharing'
    USAGE = 'http://localhost:8080/DSUsageManagement'
    AUTHORIZE_SERVICE = 'http://localhost:8004/authorizeService/apiKeys'

---
## Configuring the Charging Backend

This settings points to the different APIs accessed by the charging
backend. Concretely:

  - INVENTORY: URL of the inventory API including its path
  - ORDERING: URL of the ordering API including its path
  - BILLING: URL of the billing API including its path
  - RSS: URL of the RSS including its path
  - USAGE: URL of the Usage API including its path
  - AUTHORIZE\_SERVICE: Complete URL of the usage authorization service.
    This service is provided by the logic proxy, and is used to generate
    API Keys to be used by accounting systems when providing usage
    information.

---
## Configuring the Charging Backend

Once the services has been configured, the next step is configuring the
database. In this case, the charging backend uses MongoDB, and its
connection can be configured modifying the *DATABASES* setting of the
*settings.py* file. :

    DATABASES = {
        'default': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': 'wstore_db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            'TEST_NAME': 'test_database',
        }
    }

---
## Configuring the Charging Backend

This setting contains the following fields:

  - ENGINE: Database engine, must be fixed to django\_mongodb\_engine
  - NAME: Name of the database to be used
  - USER: User of the database. If empty the software creates a non
    authenticated connection
  - PASSWORD: Database user password. If empty the software creates a
    non authenticated connection
  - HOST: Host of the database. If empty it uses the default *localhost*
    host
  - PORT: Port of the database. If empty it uses the default *27017*
    port
  - TEST\_NAME: Name of the database to be used when running the tests

---
## Configuring the Charging Backend

Once the database connection has been configured, the next step is
configuring the name of the IdM roles to be used by updating
*settings.py* :

    ADMIN_ROLE = 'provider'
    PROVIDER_ROLE = 'seller'
    CUSTOMER_ROLE = 'customer'

---
## Configuring the Charging Backend

This settings contain the following values:

  - ADMIN\_ROLE: IDM role of the system admin
  - PROVIDER\_ROLE: IDM role of the users with seller privileges
  - CUSTOMER\_ROLE: IDM role of the users with customer privileges

---
## Configuring the Charging Backend

The Charging Backend component is able to send email notifications to
the users when they are charged or receive a payment. In this way, it is
possible to provide email configuration in the *settings.py* file by
modifying the following fields: :

    WSTOREMAILUSER = 'email_user'
    WSTOREMAIL = 'wstore_email'
    WSTOREMAILPASS = 'wstore_email_passwd'
    SMTPSERVER = 'wstore_smtp_server'
    SMTPPORT = 587

---
## Configuring the Charging Backend

This settings contain the following values:  WSTOREMAILUSER: Username
used for authenticating in the email server \* WSTOREMAIL: Email to be
used as the sender of the notifications \* WSTOREMAILPASS: Password of
the user for authenticating in the email server \* SMTPSERVER: Email
server host \* SMTPPORT: Email server port

> **note**
> 
> The email configuration in optional. However, the field WSTOREMAIL
> must be provided since it is used internally for RSS configuration

---
## Configuring the Charging Backend

Additionally, the Charging Backend is the component that charges
customers and pays providers. For this purpose it uses PayPal. For
configuring paypal, the first step is setting *PAYMENT\_METHOD* to
*paypal* in the *settings.py* file :

    PAYMENT_METHOD = 'paypal'

---
## Configuring the Charging Backend

Then, it is required to provide PayPal application credentials by
updating the file
*src/wstore/charging\_engine/payment\_client/paypal\_client.py* :

    PAYPAL_CLIENT_ID = ''
    PAYPAL_CLIENT_SECRET = ''
    MODE = 'sandbox'  # sandbox or live

---
## Configuring the Charging Backend

This settings contain the following values:

  - PAYPAL\_CLIENT\_ID: Id of the application provided by PayPal
  - PAYPAL\_CLIENT\_SECRET: Secret of the application provided by PayPal
  - MODE: Mode of the connection. It can be *sandbox* if using the
    PayPal sandbox for testing the system. Or *live* if using the real
    PayPal APIs

---
## Configuring the Charging Backend

Moreover, the Charging Backend is the component that activates the
purchased services. In this regard, the Charging Backend has the
possibility of signing its acquisition notifications with a certificate,
so the external system being offered can validate that is the Charging
Backend the one making the request. To use this functionality it is
needed to configure the Certificate and the private Key to be used by
providing its path in the following settings of the *settings.py* file :

    NOTIF_CERT_FILE = None
    NOTIF_CERT_KEY_FILE = None

---
## Configuring the Charging Backend

Finally, the last step is creating the context of the Charging Backend
by creating two sites using the provided command. First, create the
external site by executing the following command. Note that you have to
provide the real URL where the proxy will be running. :

	!bash
    $ ./manage.py createsite external http://<proxy_path>:<proxy_port>/

---
## Configuring the Charging Backend

Then, you have to create the local site by providing the real URL where
the Charging Backend will be running as follows :

    !bash
    $ ./manage.py createsite local http://localhost:<charging_port>/

---
## Configuring the Charging Backend

The Charging Backend uses a Cron task to check the status of recurring
and usage subscriptions, and for paying sellers. The periodicity of this
tasks can be configured using the CRONJOBS setting of settings.py using
the standard Cron format :

    CRONJOBS = [
        ('0 5 * * *', 'django.core.management.call_command', ['pending_charges_daemon']),
        ('0 6 * * *', 'django.core.management.call_command', ['resend_cdrs'])
    ]

---
## Configuring the Charging Backend

Once the Cron task has been configured, it is necessary to include it in
the Cron tasks using the command: :

    !bash
    $ ./manage.py crontab add

---
## Configuring the Charging Backend

It is also possible to show current jobs or remove jobs using the
commands:

	!bash
    $ ./manage.py crontab show
    
    $ ./manage.py crontab remove

---
## Configuring the Logic Proxy

The first step for configuring the proxy is creating the configuration
file by coping *config.js.template* to *config.js* :

     !bash
    $ cp config.js.template config.js

---
## Configuring the Logic Proxy

The first setting to be configured is the port where the proxy is going
to run, this setting is located in *config.js* :

    config.port = 80;

---
## Configuring the Logic Proxy

If you want to run the proxy in HTTPS you can update *config.https*
setting :

    config.https = {
        enabled: false,
        certFile: 'cert/cert.crt',
        keyFile: 'cert/key.key',
        caFile: 'cert/ca.crt',
        port: 443
    };

---
## Configuring the Logic Proxy

In this case you have to set *enabled* to true, and provide the paths to
certificate (*certFile*), to the private key (*keyFile*), and to the CA
certificate (*caFile*).

Then, it is possible to modify some of the URLs of the system.
Concretely, it is possible to provide a prefix for the API, a prefix for
the portal, and modifying the login and logout URLS :

    config.proxyPrefix = '';
    config.portalPrefix = '';
    config.logInPath = '/login';
    config.logOutPath = '/logOut';

---
## Configuring the Logic Proxy

Additionally, the proxy is the component that acts as the front end of
the Business API Ecosystem, both providing a web portal, and providing
the endpoint for accessing to the different APIs. In this regard, the
Proxy has to have the OAUth2 configuration of the FIWARE IDM.

---
## Configuring the Logic Proxy

To provide OAUth2 configuration, an application has to be created in an
instance of the FIWARE IdM (e.g https://account.lab.fiware.org),
providing the following information:

  - URL: http|<https://>\<proxy\_host\>:\<proxy\_port\>
  - Callback URL:
    http|<https://>\<PROXY\_HOST\>:\<PROXY\_PORT\>/auth/fiware/callback
  - Create a role *Seller*

---
## Configuring the Logic Proxy

Once the application has been created in the IdM, it is possible to
provide OAuth2 configuration by modifying the following settings :

    config.oauth2 = {
        'server': 'https://account.lab.fiware.org',
        'clientID': '<client_id>',
        'clientSecret': '<client_secret>',
        'callbackURL': 'http://<proxy_host>:<proxy_port>/auth/fiware/callback',
        'roles': {
            'admin': 'provider',
            'customer': 'customer',
            'seller': 'seller'
        }
    };

---
## Configuring the Logic Proxy

In this settings, it is needed to include the IDM instance being used
(*server*), the client id given by the IdM (*clientID*), the client
secret given by the IdM (*clientSecret*), and the callback URL
configured in the IdM (*callbackURL*)

---
## Configuring the Logic Proxy

Moreover, the Proxy uses MongoDB for maintaining some info, such as the
current shopping cart of a user. you can configure the connection to
MongoDB by updating the following setting: :

    config.mongoDb = {
        server: 'localhost',
        port: 27017,
        user: '',
        password: '',
        db: 'belp'
    };

---
## Configuring the Logic Proxy

In this setting you can configure the host (*server*), the port
(*port*), the database user (*user*), the database user password
(*password*), and the database name (*db*).

---
## Configuring the Logic Proxy

As already stated, the Proxy is the component that acts as the endpoint
for accessing the different APIs. In this way, the proxy needs to know
the URLs of them in order to redirect the different requests. This
endpoints can be configured using the following settings :

    config.appHost = 'localhost';    
    config.endpoints = {
        'catalog': {
            'path': 'DSProductCatalog',
            'port': '8080'
        },
        'ordering': {
             'path': 'DSProductOrdering',
            'port': '8080'
        },
    
        ...

---
## Configuring the Logic Proxy

The setting *config.appHost* contain the host where the APIs are
running. On the other hand, *config.endpoints* contains the specific
configuration of each of the APIs, including its *path*, and its *port*.

> **note**
> 
> The default configuration included in the config file is the one used
> by the installation script, so if you have used the script for
> installing the Business API Ecosystem you do not need to modify this
> fields

---
## Configuring the Logic Proxy

Finally, there are two fields that allow to configure the behaviour of
the system while running. On the one hand, *config.revenueModel* allows
to configure the default percentage that the Business API Ecosystem is
going to retrieve in all the transactions. On the other hand,
*config.usageChartURL* allows to configure the URL of the chart to be
used to display product usage to customers in the web portal.

---

.fx: back-cover

Thanks!

FIWARE                                FIWARE Lab
OPEN APIs FOR OPEN MINDS              Spark your imagination

         www.fiware.org               FIWARE Ops
twitter: @Fiware                      Easing your operations
