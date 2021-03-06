#!/bin/bash
rm */*.pyc
tar cf sac.tar ../sac/sac ../sac/bin/sacpython.so ../sac/webinterface ../sac/scripts ../sac/keys ../sac/res
echo -n 'galileoOne' > /tmp/sac/device_id
tar rf sac.tar -C /tmp sac/device_id
scp -6 sac.tar root@\[fe80::9a4f:eeff:fe01:cd8c%eth0\]:/tmp
ssh -6 root@fe80::9a4f:eeff:fe01:cd8c%eth0 "tar xf /tmp/sac.tar -C /opt/ && chown sac:sac /opt/sac -R && ln -s /usr/local/bin/python /opt/sac/bin/python && ln -s /opt/sac/bin/sacpython.so /usr/local/lib/python2.7/lib-dynload/sacpython.so"
