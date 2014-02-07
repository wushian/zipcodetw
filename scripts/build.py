#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from zipcodetw.util import Directory

def build(chp_csv_path, db_path):
    '''Build ZIP code index in SQLite from Chunghwa Post's CSV file.

    Options:

         -i, --chp-csv-path  The path of input CSV file.
         -o, --db-path       The path of output SQLite.
    '''

    print 'It may take about 10 mins.'
    print 'Processing ...'
    start = datetime.now()
    dir_ = Directory(db_path)
    dir_.load_chp_csv(open(chp_csv_path))
    print 'Done.'
    print 'It took %s to build.' % (datetime.now()-start)

if __name__ == '__main__':
    try:
        import clime.now
    except ImportError:
        import sys
        build(*sys.argv[1:])
