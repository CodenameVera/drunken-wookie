#! /usr/bin/env python2.7
try:
    from setuptools import setup, find_packages
except ImportError as e:
    import ez_setup
    ez_setup.use_setuptools()
finally:
    from setuptools import setup, find_packages

setup(name="ircdd",
      version="alpha",
      description="Distributed IRC Daemon",
      url="github.com/kzvezdarov/ircdd",
      )
