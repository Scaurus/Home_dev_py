# -*- coding: utf-8 -*-
from commands import *
f = open('ip_to_block')
line = f.readline()
while line:
    line = f.readline()
    tex1t = getoutput('iptables -I INPUT -s ' + line +' -j DROP')
save = getoutput('/sbin/iptables-save')
f.close()



