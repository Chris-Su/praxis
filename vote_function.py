from willie import module

#the response types
type1 = {'YES': 0 , 'NO': 0}
type2 = {'A': 0 , 'B': 0, 'C': 0, 'D': 0}
response = None

@module.commands('echo')
@module.example('.vote start (1/2) | .vote end | .vote [option] | .vote results')
def vote(bot, trigger):
    if triggger.group(2).lower() == 'start'
        if triggger.group(3) == 1
            response == type1
        elif triggger.group(3) == 2
            response == type2
        return

    if response
        word = triggger.group(2).upper()
        if not word:
            bot.say("you have not voted for anything")
        elif word == 'RESULTS':
            for i in response:
                bot.say(i + ' ' + str(response[i]))
        elif word == 'END'
            for i in response:
                bot.say(i + ' ' + str(response[i]))
            response == None
            return
        elif word in response:
            response[word] += 1
            bot.reply("you have voted " + word)
        else:
            bot.say(word + "is not a valid response")
        return
