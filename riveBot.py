from rivescript import RiveScript

bot = RiveScript(utf8=True)
bot.load_directory("brain")  # brain
bot.sort_replies()


def chat(user_id, message):
    if message == "":
        return -1, {"message": "No Message to response"}
    else:
        response = bot.reply(str(user_id), message)
    if response == "":
        return -1, {"message": "No Message to response"}
    return 0, response
