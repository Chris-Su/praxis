from willie import module

response = {'yes': 0 , 'no': 0}

@module.commands('echo')
@module.example('.vote yes')
def vote(bot, trigger):
    word = triggger.group(2).lower()
    if not word:
        bot.say("you have not voted for anything")
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
    
        
    