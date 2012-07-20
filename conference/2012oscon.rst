************************************************
OSCON 2012 Portland, OR - Georgy, Andrew, Myself
************************************************

Getting Better w/ Git Tutorial
==============================

Monday July 16th

Useful commands
---------------
* diff, fetch, log

::
    
    git diff --word-diff
    git diff --staged
    git diff HEAD (full story)
    git add -p <file> (interactive commit for hunks in a file)

    git log --stat
    git log --patch (-p)
    git log -p --color-words

    get fetch
    git log master..origin/master

* temporary shelving for work

::
    
    git stash
    git stash pop
    git checkout branchA
    get stash apply

* reset

::
   
    git reset --hard "HEAD^^" (go 2 commits back)


Mapping w/ Open-Source
======================

* support.mapbox.com
* http://blog.thenounproject.com/post/22660280513/designing-icons-for-web-cartography
* Mapnik -
* QGIS - desktop tool, can display geojson
* TileMill -

Where to get data
-----------------
* osm.org
* naturalearthdata.com
* us census geo/www/tiger
* local gov portals
* data.sfgov.org (shape files)
* d3js.org

Examples
--------
* http://gop.sites.devseed.com/
* http://www.npr.org/censusmap/
* https://etherpad.mozilla.org/

Embed into web
--------------
* use wax mapbox, connector
* sqlite base visual
* mbutil on github
* TileStache (python server for serving mbtiles)
* commandline app that will allow you to batch rerender map tiles
* Leaflet Example

::

    <html>
    <head>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.3.1/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet-0.3.1/leaflet.js"></script>
    </head>
    <body>
    <div id="map" style="width: 100%; height: 100%"></div>
    <script>
    var map = new L.Map('map');
    var osm = new L.TileLayer('http://tile.osm.org/{z}/{x}/{y}.png');
    map.setView(new L.LatLng(45.5, -122.65), 12).addLayer(osm);
    var pdx = { "type": "FeatureCollection", "features": [ { "type": "Feature",
    "properties": { "name": "PDX" },
    "geometry" : { "type": "Point","coordinates": [ -122.65, 45.5 ]}}]
    };
    map.addLayer(new L.GeoJSON(pdx));
    </script>
    </body>
    </html>


Wednesday Keynotes
==================

Open-source Learning Map
------------------------
By ...

* web can be the "librarian"
* common core standards initiative

Tim Orielly
-----------

* Nick Hanauer Ted talk
* The Gardens of Democracy - by Nick Hanauer
* Thomas the Train tank crashes on youtube
* focuses on building the "creative enonomy"
* relayrides -
* TedxTalk - Rodney Mullen


Python 3
========
By Wesley

* do "except Exception as e:" not "except Exception, e:"
* moved to ititerators PEP3106
* "what's new in py3 doc"
* use the -3 switch
* run 2to3 tool
* youtube pycon AU pannel video

Django e-commerce application
=============================
By Tangent ...

* Called django-oscar (on github)
* "domain driven design" book suggestion
* similar to Magento - messy to maintain 
* moved from php to python

  #. decimal support missing in php
  #. \*\*kwargs 
  #. mixins (useful in django views)

* get_model(), get_class() used for app subclassing w/ in django
* see the Facade design pattern (Service layer)
* domain modeling is key

Code Review at Netflix
======================
By ...

* makes it easy to stay on top of remote teams and expected deadlines

Don't focus on
--------------
#. Optimization
#. Personal Style

Tools
-----
* gerrit 
* fisheye

Test-driven UI Development
==========================
By Tradeshift

* Geb: Groovy based selenium
* Spock: groovy based, used for writing tests
* Web driver API

Bootstrapping Django w/ Ease
============================
By centric

authored
--------
* djenesis
* breakdown
* django-cachemodel

Bootstrapping
-------------
* requirements.txt used by pip to pull in lib reqs
 #. pip install -r requirements.txt

* use virtualenv
* put django apps in ./apps

Thursday Keynotes
=================

* www.orielly.com/animals

juju - from conicial
--------------------

encapsulated all the components from typical AWS pieces into
one easyily configurable env call juju

"Crowd sourcing operations"

* juju commands

 #. juju bootstrap
 #. juju deploy mongodb
 #. juju deploy -config file node-app subway
 #. juju add-relation mongodb subway
 #. juju status
 
* juju charms

 #. mongodb

* ubuntu desktop features

 #. the HUD (native apps & web apps)


Why Django Doesn't Scale
------------------------
By Jacob

* Cal Henderson's djangocon talk about "why I hate Django"
* data collection
 #. logging
 #. Sentry sentry.readthedocs.org
 #. python-statsd - django layer to graphite
 #. mmstats - 
 #. Metrology - best to get started with
   #. Goes into middleware
   #. Installs w/ statsd
   #. examples: query count, login attempts, 200 vrs. >=400, db transaction times

* caching
  #. "cache rules everything around me" - Burch, Silas
  #. Edge-side includes via django-esi
  #. Two-phased template rending via django-phased
  #. client-side via ajax
  #. Caching pattern in the view (dig out of slides)
  #. Celery

* Query count
  #. use select_related, prefetch_related, and raw

* ORM issues
  #. queryset cloning is slow
  #. model instantiation is slow - http://bit.ly/Muepgo
  #. model.save (saves all columns in a row) is slow as opposed to model.update

Scaling Django at Mozilla
-------------------------

* statsd navagition timing "stick"
* jingo for css minification
* cache-machine model level caching
* elastic search
* celery
* model.objects.values_list used to process large querysets in chunks
* django-toolbar
* queryset transform reduces large query counts
* mysql pooling was a big win
* django-waffle
* udp to sentry
* django-mysql-pool

Vagrant
-------

* vagrant up

* handles filesync 
* shared folders
* vagrant provision
  #. shell, chef, puppet, cfengine(soon)
* networking
  #. port forwarding
  #. host only



  






