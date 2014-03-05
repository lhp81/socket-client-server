from lettuce import step
from lettuce import world
from client import *


@step('the string (.+$)')
def the_string(step, message):
    world.message = message


@step('I send with echo client')
def send_with_echo_client(step):
    world.es = run_client(world.message)


@step('I see (.+$)')
def i_see(step, expected):
    expected == world.message
    assert world.es == expected, world.es
