#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from subprocess import Popen, DEVNULL

star = "**********************************************************************"

print(star)

ip_araligi_deger = input("IP Aralığını giriniz ( example: 192.168.0 ) ---> ")

print(star)

print("Taranan ip aralığı ", ip_araligi_deger)

print(star)

if ip_araligi_deger == "":
    print(star)
    print("Geçerli bir ip aralığını deneyiniz...")
    print(star)
    sys.exit()

p = []
aktif = 0
yanit_yok = 0
pasif = 0

for aralik in range(0, 255):
    ip = ip_araligi_deger + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=DEVNULL, stderr=DEVNULL)))

while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s Aktif' % ip)
                aktif += 1
            elif proc.returncode == 1:
                print('%s Yanıt yok' % ip)
                yanit_yok += 1
            else:
                print('%s Pasif' % ip)
                pasif += 1
    time.sleep(0.04)

print(star)

print(star)

print("Geçerli işletim sistemi", os.name)
print("Ağ Durumu")
print("Aktif Ipler  [", aktif, "]")
print("Pasif IPler [", pasif, "]")
print("Yanıt Yok  [", yanit_yok, "]")

print(star)

bitis_mesaj = "Tarama tamamlandı.."

print(bitis_mesaj)

print(star)

