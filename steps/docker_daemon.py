from behave import *
from  dockerBasic import *
import re

# scenario pull image (for moment opensuse)

test = DockerDaemon()
sut = Sut()

### scenario pulling images ###
@given('docker daemon running')
def daemon_run(context):
	test.statusDaemon()
@when('we pull image {images}')
def pull_image(context, images):
    context.response = test.pullImage(images) 
@then('we got {images} dockerized')
def assert_image(context, images):
  if (re.search(r'.*Downloaded newer image for {}:latest.*'.format(images) , str(context.response)) == None ):
        raise Exception("GOT: {} . EXPECTED \".*Downloaded newer image for <image>:latest.*\" FAIL".format(str(context.response)))
  print (str(context.response))


# scenario run commands on container ###
 
@when('run {cmd} in {images}')
def run_command(context, cmd, images):
    context.response = test.run(images, cmd)
    print (context.response)
@then('command executed on container')
def step_impl(context):
	pass

### logging bug ###
@when('journald enabled, run {cmd} with {images}')
def run_command(context, cmd, images):
    context.response = test.run(cmd, images)
    print (context.response)



@then('logs are in systemd')
def check_journal_log(context):
#  sut.run_sut("docker daemon --log-driver=journald &")
  journal_docker =  sut.run_sut("journalctl -u docker --no-pager")
  if (re.search(r'.*docker.*root'.format(images) , str(journal_docker)) == None ):
        raise Exception("FAIL to write in journal log, with Docker Container")

