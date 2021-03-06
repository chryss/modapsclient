modapsclient
============

Python RESTful client for NASA’s MODIS Adaptive Processing System
(MODAPS) data archive at the Level-1 and Atmosphere Archive &
Distribution System (LAADS) Distributed Active Archive Center (DAAC).

MIT License.

Installation
------------

.. code:: python

	pip install modapsclient

pygaarst.modapsclient
---------------------

This is a REST-full web service client that implements the NASA LAADSWEB
data API (see
https://ladsweb.modaps.eosdis.nasa.gov/tools-and-services/lws-classic/quick-start.php)

``class ModapsClient(object)``

Usage:

.. code:: python

    import modapsclient as m
    a = m.ModapsClient()
    b = a.[methodname](args)

Implements the methods from http://ladsweb.nascom.nasa.gov/data/api.html
, except for (currently) those related to OpenSearch (which don’t appear
to be working reliably server-side) and ordering (TBD). Implemented
methods are marked with an x.

+-------------+--------------------------------------+
| implemented | methodname                           |
+=============+======================================+
| x           | ``getAllOrders``                     |
+-------------+--------------------------------------+
| x           | ``getBands``                         |
+-------------+--------------------------------------+
| x           | ``getBrowse``                        |
+-------------+--------------------------------------+
| x           | ``getCollections``                   |
+-------------+--------------------------------------+
| x           | ``getDataLayers``                    |
+-------------+--------------------------------------+
| x           | ``getDateCoverage``                  |
+-------------+--------------------------------------+
| x           | ``getFileOnlineStatuses``            |
+-------------+--------------------------------------+
| x           | ``getFileProperties``                |
+-------------+--------------------------------------+
| x           | ``getFileUrls``                      |
+-------------+--------------------------------------+
| x           | ``getMaxSearchResults``              |
+-------------+--------------------------------------+
|             | ``getOpenSearch``                    |
+-------------+--------------------------------------+
|             | ``getOrderStatus``                   |
+-------------+--------------------------------------+
|             | ``getOrderUrl``                      |
+-------------+--------------------------------------+
|             | ``getOSDD``                          |
+-------------+--------------------------------------+
| x           | ``getPostProcessingTypes``           |
+-------------+--------------------------------------+
| x           | ``listCollections`` (deprecated)     |
+-------------+--------------------------------------+
| x           | ``listMapProjections``               |
+-------------+--------------------------------------+
| x           | ``listProductGroups``                |
+-------------+--------------------------------------+
| x           | ``listProducts``                     |
+-------------+--------------------------------------+
| x           | ``listProductsByInstrument``         |
+-------------+--------------------------------------+
| x           | ``listReprojectionParameters``       |
+-------------+--------------------------------------+
| x           | ``listSatelliteInstruments``         |
+-------------+--------------------------------------+
|             | ``orderFiles``                       |
+-------------+--------------------------------------+
|             | ``orderFilesProcessed`` (deprecated) |
+-------------+--------------------------------------+
|             | ``releaseOrder``                     |
+-------------+--------------------------------------+
|             | ``searchDatasets``                   |
+-------------+--------------------------------------+
| x           | ``searchForFiles``                   |
+-------------+--------------------------------------+
| x           | ``searchForFilesByName``             |
+-------------+--------------------------------------+

Caveats and limitations
-----------------------

This API is listed as “classic” by NASA EOSDIS, so it’s unlikely it’ll
receive much attention in the future. Hardly anyone will use the “order”
feature as the files are usually available on the public file server.
For these two reasons, the unimplemented functionality is also unlikely
to ever be implemented.

From experience, products listed via ``listProducts``  are not 
necessarily in actual fact available in the NASA EOSDIS LAADS archive. 
In this case, you may receive an error when searching for files. 

The MODAPS web service has the tendency to return a 500 Internal Server
Error for *any* error, including unsupported values for query string variables.

Further docuementation
----------------------

See the ``ipynb/`` folder for Jupyter Notebooks.

TODO
----

Add OPeNDAP client functionality.
