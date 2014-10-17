"""
dustbusters project setup.py

Run:

    python setup.py install

to install the dustbusters package into your site-packages directory,
and to install the 'startdustbusters' command.
You may need to adjust your path to be able to run the startdustbusters command directly.

For development, use:

    python setup.py develop

..Note::

    on my (Linux) machine, this command makes three changes to the Python framework:

        - creates a dustbusters.egg-link file in /opt/venvpy/dustbusters-env/bin/lib/python2.7/dist-packages

        - in that same directory, adds a line to easy-install.pth giving the full
          path of the dustbusters/src directory,

        - adds the 'startwsdustbusters' executable to the /usr/local/bin directory.

To undo the effects of the 'python setup.py develop' you'll need to remove/alter these 3 files.

"""

from setuptools import find_packages, setup

setup(
    name="dustbusters",
    version="1.0",
    author="dustbusters",
    author_email="openjph@gmail.com",
    license="GPLv3",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'startdustbusters = dustbusters.scripts.startdustbusters:main'
        ],
    },
)
