import telebot
from token_1 import t
from telebot import types
bot = telebot.TeleBot(t)

array = dict()

    

count = dict()
player = dict()
@bot.message_handler(commands=["start"])
def inline(message):
    global player, array
    key = types.InlineKeyboardMarkup()
    array[message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    count [message.chat.id] = 0
    but_1 = types.InlineKeyboardButton(text=array[message.chat.id][0], callback_data=1)
    but_2 = types.InlineKeyboardButton(text=array[message.chat.id][1], callback_data=2)
    but_3 = types.InlineKeyboardButton(text=array[message.chat.id][2], callback_data=3)
    but_4 = types.InlineKeyboardButton(text=array[message.chat.id][3], callback_data=4)
    but_5 = types.InlineKeyboardButton(text=array[message.chat.id][4], callback_data=5)
    but_6 = types.InlineKeyboardButton(text=array[message.chat.id][5], callback_data=6)
    but_7 = types.InlineKeyboardButton(text=array[message.chat.id][6], callback_data=7)
    but_8 = types.InlineKeyboardButton(text=array[message.chat.id][7], callback_data=8)
    but_9 = types.InlineKeyboardButton(text=array[message.chat.id][8], callback_data=9)
    
    key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
    bot.send_message(message.chat.id, "Ход ❌", reply_markup=key)
    


@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    
    global  count, array
    key = types.InlineKeyboardMarkup()

    count [c.message.chat.id] += 1

   
    if count [c.message.chat.id] % 2 != 0 and count [c.message.chat.id] < 10:
        array[c.message.chat.id][int(c.data)-1] = '❌'
        
        but_1 = types.InlineKeyboardButton(text=array[c.message.chat.id][0], callback_data=1)
        but_2 = types.InlineKeyboardButton(text=array[c.message.chat.id][1], callback_data=2)
        but_3 = types.InlineKeyboardButton(text=array[c.message.chat.id][2], callback_data=3)
        but_4 = types.InlineKeyboardButton(text=array[c.message.chat.id][3], callback_data=4)
        but_5 = types.InlineKeyboardButton(text=array[c.message.chat.id][4], callback_data=5)
        but_6 = types.InlineKeyboardButton(text=array[c.message.chat.id][5], callback_data=6)
        but_7 = types.InlineKeyboardButton(text=array[c.message.chat.id][6], callback_data=7)
        but_8 = types.InlineKeyboardButton(text=array[c.message.chat.id][7], callback_data=8)
        but_9 = types.InlineKeyboardButton(text=array[c.message.chat.id][8], callback_data=9)
        
        key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
        bot.delete_message(c.message.chat.id, c.message.message_id)
        bot.send_message(c.message.chat.id, "Ход ⭕", reply_markup=key)
        
        if array[c.message.chat.id][0] == '❌' and array[c.message.chat.id][1] == '❌' and array[c.message.chat.id][2] == '❌':
            bot.send_message(c.message.chat.id, "❌ победили")
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][3] == '❌' and array[c.message.chat.id][4] == '❌' and array[c.message.chat.id][5] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][6] == '❌' and array[c.message.chat.id][7] == '❌' and array[c.message.chat.id][8] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            bot.close()
        elif array[c.message.chat.id][0] == '❌' and array[c.message.chat.id][4] == '❌' and array[c.message.chat.id][8] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()       
        elif array[c.message.chat.id][2] == '❌' and array[c.message.chat.id][4] == '❌' and array[c.message.chat.id][6] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][0] == '❌' and array[c.message.chat.id][3] == '❌' and array[c.message.chat.id][6] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close() 
        elif array[c.message.chat.id][1] == '❌' and array[c.message.chat.id][4] == '❌' and array[c.message.chat.id][7] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][2] == '❌' and array[c.message.chat.id][5] == '❌' and array[c.message.chat.id][8] == '❌':
            bot.send_message (c.message.chat.id, '❌ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()

    elif count [c.message.chat.id] % 2 == 0 and count [c.message.chat.id] < 10:
        array[c.message.chat.id][int(c.data)-1] = '⭕'
        but_1 = types.InlineKeyboardButton(text=array[c.message.chat.id][0], callback_data=1)
        but_2 = types.InlineKeyboardButton(text=array[c.message.chat.id][1], callback_data=2)
        but_3 = types.InlineKeyboardButton(text=array[c.message.chat.id][2], callback_data=3)
        but_4 = types.InlineKeyboardButton(text=array[c.message.chat.id][3], callback_data=4)
        but_5 = types.InlineKeyboardButton(text=array[c.message.chat.id][4], callback_data=5)
        but_6 = types.InlineKeyboardButton(text=array[c.message.chat.id][5], callback_data=6)
        but_7 = types.InlineKeyboardButton(text=array[c.message.chat.id][6], callback_data=7)
        but_8 = types.InlineKeyboardButton(text=array[c.message.chat.id][7], callback_data=8)
        but_9 = types.InlineKeyboardButton(text=array[c.message.chat.id][8], callback_data=9)
        key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
        bot.delete_message(c.message.chat.id, c.message.message_id)
        bot.send_message(c.message.chat.id, "Ход ❌", reply_markup=key)
        if array[c.message.chat.id][0] == '⭕' and array[c.message.chat.id][1] == '⭕' and array[c.message.chat.id][2] == '⭕':
            bot.send_message (c.message.chat.id, 'Y победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][3] == '⭕' and array[c.message.chat.id][4] == '⭕' and array[c.message.chat.id][5] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][6] == '⭕' and array[c.message.chat.id][7] == '⭕' and array[c.message.chat.id][8] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][0] == '⭕' and array[c.message.chat.id][4] == '⭕' and array[c.message.chat.id][8] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()      
        elif array[c.message.chat.id][2] == '⭕' and array[c.message.chat.id][4] == '⭕' and array[c.message.chat.id][6] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][0] == '⭕' and array[c.message.chat.id][3] == '⭕' and array[c.message.chat.id][6] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][1] == '⭕' and array[c.message.chat.id][4] == '⭕' and array[c.message.chat.id][7] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
        elif array[c.message.chat.id][2] == '⭕' and array[c.message.chat.id][5] == '⭕' and array[c.message.chat.id][8] == '⭕':
            bot.send_message (c.message.chat.id, '⭕ победили')
            array[c.message.chat.id] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count [c.message.chat.id] = 0
            bot.close()
    
bot.infinity_polling()