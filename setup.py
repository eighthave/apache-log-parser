#!/usr/bin/env python3

from setuptools import setup


setup(name="apache-log-parser",
      version='1.8.0a',
      author="Rory McCann",
      author_email="rory@technomancy.org",
      packages=['apache_log_parser'],
      install_requires = [
        'PyYAML',
        'user-agents>=1.1.0',
      ],
      license = 'GPLv3+',
      description = "Parse lines from an apache log file",
      test_suite='apache_log_parser.tests',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
)
