from lettuce import world
from lettuce import step
import server
import socket

@step('a message (\d+)')
def a_message(step, message):
    world.message = message
    