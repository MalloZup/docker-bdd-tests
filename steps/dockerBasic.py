#!/usr/bin/python

import subprocess
import re
### here we have the actual technical tests that are imported from docker.py

class DockerDaemon():
        ''' some basic functions for docker daemon testing'''
        def statusDaemon(self):
                subprocess.check_output("systemctl status docker", shell=True)
        def pullImage(self, image):
             return  subprocess.check_output("docker pull {}".format(image), shell=True)
        def run(self, image, cmd):
             print ( subprocess.check_output("docker run {} {}".format(image, cmd), shell=True) )

class Sut():
        ''' function for sut '''
        def run_sut(self, cmd):
                subprocess.check_output(cmd, shell=True)

