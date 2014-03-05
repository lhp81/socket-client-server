from lettuce import step
from lettuce import world
from client import run_client


@step('the string: (.+$)')
def the_string(step, message):
    world.message = message


@step('I send with echo_client')
def call_echo_client(step):
    world.es = run_client(world.message)


@step('I see (.+$)')
def compare(step, expected):
    expected == world.message
    assert world.es == expected, world.es
