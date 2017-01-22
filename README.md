# IPR Downloader
Python library and command line tools for downloading open data provided by IPR

Taken from: https://github.com/ctu-geoforall-lab-projects/bp-jakl-2016/tree/master/src/iprdownloader

Author: Martin Jakl (2016)

## Usage

List available layers:

     ./iprdownloader.py
          
     Pražská integrovaná doprava - linky (aktuální stav)
     Pražská integrovaná doprava - zastávky (aktuální stav)
     Pražská integrovaná doprava - popis zastávek (aktuální stav)
     Pražská integrovaná doprava - trasy (aktuální stav)
     ...

List available layers with filter:

     ./iprdownloader.py --alike Vrstevnice
     
     Vrstevnice 5 m
     Vrstevnice 2 m
     Vrstevnice 1 m

Download selected layer:

     ./iprdownloader.py --alike toalety --download

Layer is downloaded in default CRS (S-JTSK, EPSG:5514) and data format
(Esri Shapefile). Downloaded layers are stored in directory called
'data'.

Download selected layer in WGS-84 CRS and GeoJSON format:

     ./iprdownloader.py --alike 'toalety' --download --crs WGS-84 --format=geojson

Download and import data into PostGIS DB:

     ./iprdownloader.py --alike 'pěší trasy' --dbname ipr
