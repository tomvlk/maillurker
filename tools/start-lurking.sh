#!/bin/bash

# Start lurker.
cd ${TRAVIS_BUILD_DIR}/src
python manage.py start_lurking&
