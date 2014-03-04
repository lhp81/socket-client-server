from lettuce import step
from lettuce import world
from client import run_client


@step('the string: (.)')
def the_string(step, message):
    world.cla = msg


@step('when I send it with the echo_client')
def call_echo_client(step):
    world.client = run_client(world.cla)


@step('Then I see: (.)')
def compare(step, expected):
    assert world.client == expected, world.client
