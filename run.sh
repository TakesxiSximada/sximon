#! /usr/bin/env sh
echo PORT NUMBER IS $VCAP_APP_PORT
pip uninstall -y sximon
pip install -Ue .
pserve development.ini http_port=$VCAP_APP_PORT
