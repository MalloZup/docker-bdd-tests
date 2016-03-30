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
    assert re.match(r'.*Image is up to date for {}:latest.*'.format(images) , str(context.response)), "not got right image"

# scenario run commands on container
 
@when('run {cmd} in {images}')
def run_command(context, cmd, images):
    context.response = test.run(images, cmd)
    print (context.response)
@then('command executed on container')
def step_impl(context):
	pass

