#!/usr/bin/env python
# encoding: utf-8
"""
test_modapsclient.py

Created by Chris Waigl on 2015-04-21.
"""

from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals
from builtins import str
import modapsclient
import pytest
from .modapsdummydata import modapsresponses


def mockedresponse(url, data=None):
    try:
        return modapsresponses[url]
    except KeyError:
        return modapsresponses['invalid']


def fakeurl(fakepath, TLS=True):
    return fakepath


@pytest.fixture(scope='module')
def mockmodaps():
    a = modapsclient.ModapsClient()
    a._makeurl = fakeurl
    a._rawresponse = mockedresponse
    return a


@pytest.fixture(scope='module')
def realmodaps():
    a = modapsclient.ModapsClient()
    return a


def test_modapsclient_patching():
    assert len(list(modapsresponses.keys())) == 7


def test_modapsclient_creation(mockmodaps):
    assert mockmodaps.headers['User-Agent'] == 'satellite RS data fetcher'


def test_startswithax():
    assert modapsclient.modapsclient._startswithax('xmlns:axlskdjf')


# complete this
# def test_parselistofdicts():
#     b = '<container><prefix:key1>VAL1</prefix:key1></container>'

def test_fileURLs(mockmodaps):
    assert mockmodaps.getFileUrls(1)[0].strip() == (
        u'ftp://ladsweb.nascom.nasa.gov/allData/5/MOD021KM/2004/201/'
        u'MOD021KM.A2004201.2130.005.2010141190341.hdf'
    )


def test_satelliteInstruments(mockmodaps):
    assert mockmodaps.listSatelliteInstruments() == {
        u'AM1M': u'Terra MODIS',
        u'AMPM': u'Combined Aqua & Terra MODIS',
        u'ANC': u'Ancillary Data',
        u'NPP': u'Suomi NPP VIIRS',
        u'PM1M': u'Aqua MODIS'
    }


def test_realrequest(realmodaps):
    satinst = realmodaps.listSatelliteInstruments()
    assert isinstance(list(satinst.keys())[0], str)
