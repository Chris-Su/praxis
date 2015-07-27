from willie import module

questions = []

@module.commands('ask')
@module.example('.ask [question] | .ask questionlist')
def vote(bot, trigger):
    question = triggger[4:]
    if not question:
        bot.say("you have not asked a question")
    elif question == questionlist:
        for i in questions
        bot.say(i)
    elif question.length() < 100:
        questions.append(question)
    else:
        bot.say("error")
    return
    
