import willie.module
from enum import Enum
from pprint import pprint
import pg8000

class Modes(Enum):
  IDLE = 0
  OPEN = 1
  CLOSED = 2

mode = Modes.IDLE
db_connection = None
db_cursor = None

def setup(config):
  global db_connection
	global db_cursor
	db_connection = pg8000.connect(user="jafoster", database="jafoster")
	db_connection.autocommit = True
	db_cursor = db_connection.cursor()

def shutdown(willie):
	global db_connection
	global db_cursor
	db_cursor.close()
	db_connection.close()

@willie.module.commands('askq')
@willie.module.example('.askq QUESTION')
def ask(bot, trigger):
	"""
	Asks each user in a channel (separately) to answer the given question using .answerq
	Use .closeq to stop accepting answers.
	"""
	global mode

	pprint( bot.privileges['#praxis'] )

	if ( ( mode is Modes.IDLE ) or ( mode is Modes.CLOSED ) ):

		question = trigger.group(2)

		if ( question is None ):
			bot.reply( 'You must specify a question.' )
			return

		mode = Modes.OPEN
		
		users = bot.privileges['#praxis']

		for nick in users:
			# TODO: need a better way to filter out people who shouldn't be asked (aka. Teaching Team)
			if ( nick == trigger.nick):
				continue
			bot.msg( nick, question )
			bot.msg( nick, 'Submit your answer using .answerq' )
	elif ( mode is Modes.OPEN ):
		bot.reply( 'You can''t ask a new question without first closing the open question with .closeq' )
	else:
		bot.reply( 'We have a problem with the state machine!' )

@willie.module.commands('answerq')
@willie.module.example('.answerq ANSWER')
def answer(bot, trigger):
	"""
	Answers the current question. Answering multiple times overwrites your previous answer.
	"""
	global mode
	global db_cursor
	
	if ( mode is Modes.IDLE ):
		bot.reply( 'No questions have been asked.' )
	elif ( mode is Modes.OPEN ):
		user = 	trigger.user
		answer = trigger.group(2)
		if ( answer is None ):
			bot.reply( 'You must specify an answer.' )
		else:
			# TODO: how to actually store answers?!
			#    definitely should include the actual UTORid though!
			sql = "insert into qa.answers values ('{}','{}');".format( user,answer )
			db_cursor.execute( sql )
			bot.reply( 'Your answer has been recorded.' )
	elif ( mode is Modes.CLOSED ):
		bot.reply( 'The question has been closed -- reply faster next time!' )
	else:
		bot.reply( 'We have a problem with the state machine!' )
		
@willie.module.commands('closeq')
@willie.module.example('.closeq')
def close(bot, trigger):
	"""
	Stops accepting answers.
	"""
	global mode

	if ( ( mode is Modes.IDLE ) or ( mode is Modes.CLOSED ) ):
		bot.reply( 'You can''t close a question without first asking one with .askq' )
	elif ( mode is Modes.OPEN ):
		mode = Modes.CLOSED
		bot.reply( 'The question has been closed.' )		
	else:
		bot.reply( 'We have a problem with the state machine!' )
