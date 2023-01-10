import datetime
import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))
    if p_message == 'time':
        return str(datetime.datetime.now())
    if p_message == 'flip_coin':
        return 'Heads' if random.randint(0, 1) == 0 else 'Tails'        

    if p_message == '!help':
        return "Possible commands: 'hello', 'roll', time, flip coin"
    if p_message[0:4] =='play':
        play_music(p_message[5:])


def play_music(link):
    print("No music for now...")

    
    
    