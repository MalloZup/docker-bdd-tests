from behave import *
from  dockerBasic import *
import re

# scenario pull image (for moment opensuse)

test = DockerDaemon()
@given('docker daemon running')
def step_impl(context):
	test.statusDaemon()
@when('pull image opensuse')
def step_impl(context):
    context.response = test.pullImage("opensuse") 
@then('we got opensuse dockerized')
def step_impl(context):
    assert re.match(r'.*Image is up to date for opensuse:latest.*', str(context.response)), "not got opensuse"

# scenario run commands on container
 
@when('run command with docker')
def step_impl(context):
    context.response = test.run("opensuse","ls")
    print (context.response)
@then('command executed on container')
def step_impl(context):
	pass

