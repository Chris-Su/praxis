from willie import module

questions = []

@module.commands('ask')
@module.example('.ask [question] | .ask questionlist | ')
def vote(bot, trigger):
    question = triggger[4:]
    if not question:
        bot.say("you have not asked a question")
        return
    elif question == questionlist:
        for i in questions
        bot.say(i)
        return
    else:
        bot.say("error")
    
