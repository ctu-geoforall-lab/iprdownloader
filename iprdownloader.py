#!/usr/bin/env python
#########################################################################
#
# Command-line tool for downloading IPR data and importing into PostGIS
# http://www.iprpraha.cz/clanek/1313/otevrena-data-open-data (in Czech)
#
# 2016 (c) by Martin Jakl (OSGeoREL CTU in Prague)
#
# Licence: GNU GPL v2+
#
#########################################################################


import sys
import urllib2
import xmltodict
import argparse

from IprBase import IprDownloader, IprError
from IprPg   import IprDownloaderPg


def main(alike=None, crs=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--alike", type=lambda s: unicode(s, 'utf8'), help = "search name title alike given string")
    parser.add_argument("--crs",   type=str,default = "S-JTSK",       help = "specify coordinate system (WGS-84 or S-JTSK > default: S-JTSK")
    parser.add_argument("--format",type=str,default = "shp",          help = "specify file format (default: shp) ..for rasters tiff,png..")
    parser.add_argument("--outdir",type=str,default = "data",         help = "define the folder to save (default: data)")
    parser.add_argument("--download", action='store_true',            help = "download selected data")
    parser.add_argument("--dbname",type=str,                          help = "DB name")
    parser.add_argument("--dbschema",type=str,                        help = "DB schema (default: public)")
    parser.add_argument("--dbhost",type=str,                          help = "DB hostname")
    parser.add_argument("--dbport",type=str,                          help = "DB port")
    parser.add_argument("--dbuser",type=str,                          help = "DB username")
    parser.add_argument("--dbpasswd",type=str,                        help = "DB password")
    parser.add_argument("--overwrite", action='store_true',           help = "overwrite existing file")
    parser.add_argument("--import_only", action='store_true',         help = "dont download file, only import")  
    
    args = parser.parse_args()
 

    if args.crs == "5514":
        args.crs = "S-JTSK"
    elif args.crs == "4326":
        args.crs = "WGS 84"
    else:
        args.crs = args.crs.upper()
        if args.crs == 'WGS-84':
            args.crs = args.crs.replace('-', ' ')

    if args.crs not in ('S-JTSK', 'WGS 84'):
        sys.exit("Unsupported coordinate system: {0}. Valid options: S-JTSK, WGS-84".format(args.crs))

    ipr = IprDownloaderPg(args.dbname,args.dbhost, args.dbport,
                          args.dbuser, args.dbpasswd, args.dbschema)

    ipr.filter(args.alike, args.crs, args.format)

    if (args.download or args.dbname):
        ipr.download(args.outdir,args.import_only)
        if args.dbname:
            try:
                ipr.import_data(args.crs, args.overwrite)
            except IprError as e:
                sys.exit('ERROR: {}'.format(e))
    else:
        ipr.print_items()


    return 0

if __name__ == "__main__":
    sys.exit(main())

