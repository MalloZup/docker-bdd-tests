from behave import *
from  dockerBasic import *
import re

# scenario pull image (for moment opensuse)

test = DockerDaemon()
@given('docker daemon running')
def daemon_run(context):
	test.statusDaemon()
@when('we pull image {images}')
def pull_image(context, images):
    context.response = test.pullImage(images) 
@then('we got {images} dockerized')
def assert_image(context, images):
  if (not re.match(r'.*Downloaded newer image for {}:latest.*'.format(images) , str(context.response))):
        raise Exception("GOT: {} . EXPECTED \"*Downloaded newer image for <image>:latest.*\" FAIL".format(str(context.response)))

# scenario run commands on container
 
@when('run {cmd} in {images}')
def run_command(context, cmd, images):
    context.response = test.run(images, cmd)
    print (context.response)
@then('command executed on container')
def step_impl(context):
	pass

