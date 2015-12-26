#!/bin/sh

CONF=/mnt/var/lib/connman/wifi_eduroam.config 
if [ -f $CONF ]; then
    connmanctl connect wifi_80000b54929b_656475726f616d_managed_ieee8021x
else
    echo "Config file $CONF is missing. Won't be able to connect this way."
fi

