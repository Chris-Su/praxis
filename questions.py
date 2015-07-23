from willie import module

response = {'yes': 0 , 'no': 0}

@module.commands('ask')
@module.example('.ask how much is this test worth?')
def vote(bot, trigger):
    question = triggger[4:]
    if not question:
        bot.say("you have not asked a question")
        return
    elif word == 'results':
        for i in response:
            bot.say(i + ' ' + str(response[i]))
        return
    elif word in response:
        response[word] += 1
        bot.reply("you have voted " + word)
        return
    else:
        bot.say(word + "is not a valid response")
    
