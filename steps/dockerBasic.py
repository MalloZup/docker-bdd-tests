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
	def run(self, cmd, image):
	     print ( subprocess.check_output("docker run {} {}".format(cmd, image), shell=True) )
