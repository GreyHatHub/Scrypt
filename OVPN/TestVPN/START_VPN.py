# -*- coding: UTF-8 -*-
from os import listdir
from random import *
import subprocess
import os

class VPNCommand:

    def conn(self):
        files = listdir("./TestVPN/")
        link='./TestVPN/'+files[randint(0,files.__len__()-1)]
        
        os.system('echo ---------------------------------')
        os.system('echo '+files[randint(0,files.__len__()-1)]+'\n')
        os.system('echo ---------------------------------')
        with open(link, 'r') as text:
            mylist = text.readlines()
        
        #mylist.append('auth-user-pass loginpas.txt')
        for index,ine in enumerate(mylist):
            if 'auth-user-pass' in ine:
                mylist[index]="auth-user-pass loginpas.txt\n"
            if 'cipher' in ine:
                	mylist[index]="data-ciphers AES-256-GCM:AES-128-GCM:AES-128-CBC\n"
                # mylist[index]="data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305\n"
                # mylist[index]="cipher AES-256-CBC\n"
                 
            
        MyFile = open ('VPN-new.ovpn', 'w') 
        MyFile.writelines(mylist) 
        MyFile.close()
        
        fi='echo ############ | sudo -S openvpn ./VPN-new.ovpn'
        os.system(fi)
        
    def main(self):
        for i in range(1):
            self.conn()
            print('#'*70)
            print('#'*70)
            print('#'*70)

if __name__ == '__main__':
    parser = VPNCommand()
    parser.main()
