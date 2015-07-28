from willie import module

questions = []

@module.commands('ask')
@module.example('.ask [question] | .ask questionlist | .ask answer [question #]')
def vote(bot, trigger):
    question = triggger[4:]
    if not question:
        bot.say("you have not asked a question")
    elif trigger.group(2)
        if trigger.group(3).isdigit()
            bot.say('question ' + trigger.group(3) + ' has been answered')
            del questions[int(trigger.group(3)) - 1]
    elif question == questionlist:
        for i in questions
        bot.say(i)
    elif question.length() < 100:
        questions.append(question)
    else:
        bot.say("error")
    return
    
