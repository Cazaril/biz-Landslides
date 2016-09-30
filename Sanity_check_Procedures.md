# Introduction to Business API ecosystem

.fx: cover

@conwet

---
# Installing Asset Plugins

The Business API Ecosystem is intended to support the monetization of
different kind of digital assets. The different kind of assets that may
be wanted to be monetized will be heterogeneous and potentially very
different between them.

Additionally, for each type of asset different validations and
activation mechanisms will be required. For example, if the asset is a
CKAN dataset, it will be required to validate that the provider is the
owner of the dataset. Moreover, when a customer acquires the dataset, it
will be required to notify CKAN that a new user has access to it.

---
# Installing Asset Plugins

The huge differences between the different types of assets that can be
monetized in the Business API Ecosystem makes impossible to include its
validations and characteristics as part of the core software. For this
reason, it has been created a plugin based solution, where all the
characteristics of an asset type are implemented in a plugin that can be
loaded in the Business API Ecosystem.

---
# Installing Asset Plugins

To include an asset plugin execute the following command in the Charging
Backend:

	!bash
    $ ./manage.py loadplugin ckandataset.zip

It is possible to list the existing plugins with the following command:

    !bash
    $ ./manage.py listplugins

---
# Installing Asset Plugins

To remove an asset plugin, execute the following command providing the
plugin id given by the *listplugins* command :

    !bash
    $ ./manage.py removeplugin ckan-dataset

> **note**
> 
> For specific details on how to create a plugin and its internal
> structure, have a look at the Business API Ecosystem Programmer Guide

---
# Installing Asset Plugins

At the time of writing, the following plugins are available:

  - [WireCloud
    Component](https://github.com/FIWARE-TMForum/wstore-wirecloud-plugin):
    Allows the monetization of WireCloud components, including Widgets,
    operators, and mashups
  - [Accountable
    Service](https://github.com/FIWARE-TMForum/wstore-orion-plugin) :
    Allows the monetization of services protected by the [Accounting
    Proxy](https://github.com/FIWARE-TMForum/Accounting-Proxy),
    including Orion Context Broker queries
  - [CKAN Dataset](https://github.com/FIWARE-TMForum/wstore-ckan-plugin)
    : Allows the monetization of CKAN datasets

---
.fx: back-cover

Thanks!

FIWARE                                FIWARE Lab
OPEN APIs FOR OPEN MINDS              Spark your imagination

         www.fiware.org               FIWARE Ops
twitter: @Fiware                      Easing your operations
