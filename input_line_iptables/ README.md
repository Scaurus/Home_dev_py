1) сохранить настройки правил. iptables-restore < /etc/iptables.rules
2) так же надо добавить в файл ( если использовать synology nas ) /etc/rc.network строку:
iptables-restore < /etc/iptables.rules  что бы восстановить правила после перезагрузки.

