import logging
import logstash
import sys

# logging docs
# https://docs.python.org/3/library/logging.html#logrecord-attributes

# logstash docs
# https://pypi.org/project/python3-logstash/

logger = logging.getLogger('game-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('18.191.210.237', 5959, version=1))

# add extra field to logstash message
def make_game_start_log( game_id, game_responses, game_state, first_response ):
    extra = {
    'game_id': game_id,
    'game_responses': game_responses,
    'game_state': game_state,
    'start_response': first_response
    }

    logger.info('logging game start', extra=extra)

def make_game_end_log( game_id, game_responses, game_state, choices_made ):
    extra = {
    'game_id': game_id,
    'game_responses': game_responses,
    'game_state': game_state,
    'choices_made': choices_made
    }

    logger.info('logging game end', extra=extra)

def make_response_log( game_id, choice_1, choice_2, choice_3, choice_4 ):
    extra = {
    'game_id': game_id,
    'choice_1_made': choice_1,
    'choice_2_made': choice_2,
    'choice_3_made': choice_3,
    'choice_4_made': choice_4
    }

    logger.info('logging game choices', extra=extra)
