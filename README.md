# modapsclient

Python RESTful client for NASA's MODIS Adaptive Processing System (MODAPS) data archive 
at the Level-1 and Atmosphere Archive &amp; Distribution System (LAADS) Distributed Active Archive Center (DAAC)

MIT License.

pygaarst.modapsclient
---------------------

This is a REST-full web service client that implements the NASA LAADSWEB data API (see https://ladsweb.modaps.eosdis.nasa.gov/tools-and-services/lws-classic/quick-start.php)

`class ModapsClient(object)` |

Usage:

```python
from pygaarst import modapsclient as m
a = m.ModapsClient()
b = a.[methodname](args)
```

Implements the methods from http://ladsweb.nascom.nasa.gov/data/api.html , except for (currently) those related to OpenSearch (which don't appear to be working reliably server-side) and ordering (TBD). Implemented methods are marked with an x. 

| implemented | methodname |
|-------------|------------|
| x | `getAllOrders` |
| x | `getBands` |
| x | `getBrowse` |
| x | `getCollections` |
| x | `getDataLayers` |
| x | `getDateCoverage` |
| x | `getFileOnlineStatuses` |
| x | `getFileProperties` |
| x | `getFileUrls` |
| x | `getMaxSearchResults` |
| | `getOpenSearch` |
| | `getOrderStatus` |
| | `getOrderUrl` |
| | `getOSDD` |
| x | `getPostProcessingTypes` |
| x | `listCollections` (deprecated)  
| x | `listMapProjections` |
| x | `listProductGroups` |
| x | `listProducts` |
| x | `listProductsByInstrument` |
| x | `listReprojectionParameters` |
| x | `listSatelliteInstruments` |
| | `orderFiles` |
| | `orderFilesProcessed` (deprecated)  
| | `releaseOrder` |
| | `searchDatasets` |
| x | `searchForFiles` |
| x | `searchForFilesByName` |