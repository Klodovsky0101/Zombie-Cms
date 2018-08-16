#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
import re
try:
        import socket
except:
        print "Khass Asat T install socket qlb fi google install socket in python 2.7 "
class revolution:
        def __init__(self):
                os.system('color c')
                os.system('cls')
                banner = """
   _____            _                                  ______                    
  / ___/   ____    (_)    ____   ___    _____         / ____/   ____ ___    _____
  \__ \   / __ \  / /    / __ \ / _ \  / ___/ ______ / /       / __ `__ \  / ___/
 ___/ /  / / / / / /    / /_/ //  __/ / /    /_____// /___    / / / / / / (__  ) 
/____/  /_/ /_/ /_/    / .___/ \___/ /_/            \____/   /_/ /_/ /_/ /____/  
                      /_/                                                        

                """
                author = """
                CODED BY SAHARA H4xOR
                """
                
                print banner
                print author
                x = open(raw_input('List Sites:'),'r').readlines()
                for sites in x:
                        sites = sites.rstrip()
                        self.ips = socket.gethostbyname(sites)
                        self.reverse()
                        print """
                                Wordpress ::: wp.txt
                                  Joomla :: joomla.txt
                                  Drupal :: drupal.txt
                                  """
        def reverse(self):
                req = requests.get("http://api.hackertarget.com/reverseiplookup/?q="+self.ips)
                cont = req.content
                ope = open('x.txt','a').write(cont)
                self.getcms()
        def getcms(self):
                sitess = open('x.txt','r').readlines()
                for site in sitess:
                        site = site.rstrip()
                        jo = requests.get('http://'+site+'/templates/system/css/system.css').content
                        get = requests.get('http://'+site+'/').content
                        if 'Import project-level system CS' in jo:
                                hi = open('joomla.txt','a').write('http://'+site+'/'+'\n')
                        elif '/wp-content/' in get:
                                xa = open('wp.txt','a').write('http://'+site+'/'+'\n')
                        elif '/sites/default/' in get \
                           or 'content="Drupal' in get:
                                xw = open('drupal.txt','a').write('http://'+site+'/'+'\n')
        
        

rev = revolution()