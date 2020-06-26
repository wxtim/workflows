#!/usr/bin/python

from os import environ
from utils import hello

hello(environ['whom'])