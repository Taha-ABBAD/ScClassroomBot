from logging import error
import telebot
import requests
from telebot import types

#Bot Token value
API_TOKEN = '1678093140:AAGzxd1ZCarqiZKi77_gFRHyzqPwo0vatXk'
# Initialize bot and dispatcher
bot = telebot.TeleBot(API_TOKEN)



#command start 
@bot.message_handler(commands=["start"])
def start_command(message: types.Message):
    
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('help โ๏ธ')
    btn2 = types.KeyboardButton('Go Cours ๐')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id,"Hi Every One!โ\nI'm CS Classroom BOT!๐ค\nPowered by GtgTeam๐ฅ\n\n\nLet's go!.",reply_markup=markup)
        

#Main menu
def mainMenu(message: types.Message) :
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('help โ๏ธ')
    btn2 = types.KeyboardButton('Go Cours ๐')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id,"Main Menu",reply_markup=markup)
        


#command help 
@bot.message_handler(commands=['help'])
def help_command(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
       types.InlineKeyboardButton(
           'Message the developer ๐ค', url='telegram.me/TAHA_iNecoTiNe'
       ) 
   )
    bot.send_message(message.chat.id,"it's my pleasure to help you ๐",reply_markup=markup)
    
#listener --> "help โ๏ธ"
@bot.message_handler(func=lambda message: message.text == 'help โ๏ธ' and message.content_type == 'text')
def goCours_message(message: types.Message):
    help_command(message)
#listener --> "Go Cours !"
@bot.message_handler(func=lambda message: message.text == 'Go Cours ๐' and message.content_type == 'text')
def goCours_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Bases de donnรฉes avancรฉes ๐')
    btn2 = types.KeyboardButton('Reseaux2 ๐')
    btn3 = types.KeyboardButton('Genie logiciel ๐')
    btn4 = types.KeyboardButton('Programmation objet ๐')
    btn5 = types.KeyboardButton('Technologie web2๐')
    btn6 = types.KeyboardButton('Systeme expert๐')
    btn7 = types.KeyboardButton('Curricula et evaluation educative๐')
    btn8 = types.KeyboardButton('Didactique๐')
    btn9 = types.KeyboardButton('Go Back ๐')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    markup.row(btn5)
    markup.row(btn6)
    markup.row(btn7)
    markup.row(btn8)
    markup.row(btn9)
    bot.send_message(message.chat.id,"Select a Cours ๐ :",reply_markup=markup)

#listener --> "Go Back ๐"
@bot.message_handler(func=lambda message: message.text == 'Go Back ๐' and message.content_type == 'text')
def goBack_message(message: types.Message):
    mainMenu(message)

#listener --> "Go Back ๐๐"
@bot.message_handler(func=lambda message: message.text == 'Go Back ๐๐' and message.content_type == 'text')
def goBack_message(message: types.Message):
    goCours_message(message)

#listener --> "Bases de donnรฉes avancรฉes ๐"
@bot.message_handler(func=lambda message: message.text == 'Bases de donnรฉes avancรฉes ๐' and message.content_type == 'text')
def c1_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD๐')
    btn2 = types.KeyboardButton('TP๐ป')
    btn3 = types.KeyboardButton('COURS๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('BDA Channel ๐ฅ', url='https://t.me/ensc_database_course_4B5'))
    bot.send_message(message.chat.id,"Bases de donnรฉes avancรฉes ๐ :",reply_markup=markup1)
    bot.send_message(message.chat.id,"Select a button ๐ : ",reply_markup=markup)

#listener --> "COURS๐"
@bot.message_handler(func=lambda message: message.text == 'COURS๐' and message.content_type == 'text')
def coursBDA(message: types.Message):
        link1 = 'https://drive.google.com/uc?export=download&id=19HL7nNcq5Ef7uanfhNMbbZ0wcH-2UacI'
        try :
           bot.send_document(message.chat.id, data=downDocs(link1,'Chapitre_1 _Rappel_sur_BD.pdf'))
        except:
            pass
        link2 = 'https://drive.google.com/uc?export=download&id=1Kr8ij8mh7rU7-w7xtAGxHgkecnyf6Nhi'
        try :
           bot.send_document(message.chat.id, data=downDocs(link2,'chapitre_2_model_Relationnel_Objet.pdf'))
        except:
            pass
        link3 = 'https://drive.google.com/uc?export=download&id=10OgITubvde4fnZN3Vcc0yHG1vUwUBkLp'
        try :
           bot.send_document(message.chat.id, data=downDocs(link3,'Chapitre_3_Distributed_Databases.pdf'))
        except:
            pass
        link4 = 'https://drive.google.com/uc?export=download&id=1lP6F6kSkfacctNgX5MzPsyIKU4l-unGf'
        try :
           bot.send_document(message.chat.id, data=downDocs(link4,'NoSQL_Databases'))
        except:
            pass
#listener --> "TD๐"
@bot.message_handler(func=lambda message: message.text == 'TD๐' and message.content_type == 'text')
def tdBDA(message: types.Message):
    bot.send_message(message.chat.id,"Sorry no data yet !")

#listener --> "TP๐ป"
@bot.message_handler(func=lambda message: message.text == 'TP๐ป' and message.content_type == 'text')
def tpBDA(message: types.Message):
        link1 = 'https://drive.google.com/uc?export=download&id=1evTqAzj9V1zwec50IVXtNeIp8iG7L3Au'
        try :
           bot.send_document(message.chat.id , data = downDocs(link1,'Tp1_2021_part_1.pdf'))
        except:
            pass
        link2 = 'https://drive.google.com/uc?export=download&id=1HlIDqlYm6o7ZXo-QKLodGpxQUo74Id5x'
        try :
           bot.send_document(message.chat.id , data = downDocs(link2,'TP_2_BDA_2021.pdf'))
        except:
            pass
        link3 = 'https://drive.google.com/uc?export=download&id=1Us2sk9AJ4fgDR1c9JcCBYNb7YzmteBQa'
        try :
           bot.send_document(message.chat.id , data = downDocs(link3,'TP_3_Expose_BDA_2021.pdf'))
        except:
            pass

#listener --> "Reseaux2 ๐"
@bot.message_handler(func=lambda message: message.text == 'Reseaux2 ๐' and message.content_type == 'text')
def c2_message(message: types.Message):  
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD ๐')
    btn2 = types.KeyboardButton('TP ๐ฅ๏ธ')
    btn3 = types.KeyboardButton('COURS ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Reseaux2 ๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "COURS ๐"
@bot.message_handler(func=lambda message: message.text == 'COURS ๐' and message.content_type == 'text')
def coursR(message: types.Message):
    link1 = 'https://drive.google.com/uc?export=download&id=1EErFQH_jjDM69WTt-ufof3I40vdeo83n'
    try :
        bot.send_document(message.chat.id, data=downDocs(link1,'sommaire.pptx'))
    except:
        pass    
    link2 = 'https://drive.google.com/uc?export=download&id=1QO_B3WlIGXOpOVJzDHQVV806botOYdBgG'
    try :
        bot.send_document(message.chat.id, data=downDocs(link2,'chapitre 4.pptx'))
    except:
        pass   
    link3 = 'https://drive.google.com/uc?export=download&id=1q9NO0nIXpqSj3ZoGH_x8GQxJueWgF-H7'
    try :
       bot.send_document(message.chat.id, data=downDocs(link3,'chapitre 5.pptx'))
    except:
        pass
    link4 = 'https://drive.google.com/uc?export=download&id=1rI3T7MCctReDRexKkLd9QiJGUD0Zcwtl'
    try :
       bot.send_document(message.chat.id, data=downDocs(link4,'chapitre 6.pptx'))
    except:
        pass         
#listener --> "TD ๐"
@bot.message_handler(func=lambda message: message.text == 'TD ๐' and message.content_type == 'text')
def tdR(message: types.Message):
    link1 = 'https://drive.google.com/uc?export=download&id=17O_3axoSCN3UGMZGRdv1RKpc_PZJ7_VJ'
    try :
        bot.send_document(message.chat.id, data=downDocs(link1,'exposรฉ 2021.docx'))
    except:
        pass
    link2 = 'https://drive.google.com/uc?export=download&id=15QjV5KVieKbTbMO8hW_2mINYnUleqMCw'
    try :
        bot.send_document(message.chat.id, data=downDocs(link2,'TD multicast.docx'))
    except:
        pass

#listener --> "TP ๐ฅ๏ธ"
@bot.message_handler(func=lambda message: message.text == 'TP ๐ฅ๏ธ' and message.content_type == 'text')
def tpR(message: types.Message):
    link1 = 'https://drive.google.com/uc?export=download&id=1Bj9c1KFhm5B0768Ch-8nKjpq-oSDrcnd'
    try :
       bot.send_document(message.chat.id , data = downDocs(link1,'TP switch.docx'))
    except:
        pass       


#listener --> "Genie logiciel ๐"
@bot.message_handler(func=lambda message: message.text == 'Genie logiciel ๐' and message.content_type == 'text')
def c3_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD  ๐')
    btn2 = types.KeyboardButton('TD Correction๐')
    btn3 = types.KeyboardButton('COURS  ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Genie logiciel ๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "COURS  ๐"
@bot.message_handler(func=lambda message: message.text == 'COURS  ๐' and message.content_type == 'text')
def coursGL(message: types.Message):
    
        link1 = 'https://drive.google.com/uc?export=download&id=1CJizbMLYOgWrJEZwSVMXikKGJwnZUO7w'
        try :
           bot.send_document(message.chat.id, data=downDocs(link1,'Cours 1.pdf'))
        except:
            pass
        link2 = 'https://drive.google.com/uc?export=download&id=1jWhyIwLG_cZI-AOp-PUbocv4u4euUNEl'
        try :
           bot.send_document(message.chat.id, data=downDocs(link2,'Cours 2.pdf'))
        except:
            pass
        link3 = 'https://drive.google.com/uc?export=download&id=19CwcGjFp8rkRpdx1QMC_8KQ31oJKDVan'
        try :
           bot.send_document(message.chat.id, data=downDocs(link3,'Annalyse des besoins.pdf'))
        except:
            pass
        link4 = 'https://drive.google.com/uc?export=download&id=170cn8bBPB8scLfcvaF2xK6lDyeBkCYKF'
        try :
           bot.send_document(message.chat.id, data=downDocs(link4,'conception des logiciels.pdf'))
        except:
            pass
        link5 = 'https://drive.google.com/uc?export=download&id=1nvJGezo7r_Vi6HrWiTBhUlNoPzFcnY3c'
        try :
           bot.send_document(message.chat.id, data=downDocs(link5,'Cycle de vie logiciel 2020.pdf'))
        except:
            pass
        link6 = 'https://drive.google.com/uc?export=download&id=13kjMobt_NnFRKAR8SYDfzBRz-rn2mRHZ'
        try :
           bot.send_document(message.chat.id, data=downDocs(link6,'Programmation, Test  Maintenance.pdf'))
        except:
            pass
        link7 = 'https://drive.google.com/uc?export=download&id=1MKStT0m-ekWQSuO8dvSTA5qsxsdvelE9'
        try :
           bot.send_document(message.chat.id, data=downDocs(link7,'Qualitรฉ logiciel.pdf'))
        except:
            pass

#listener --> "TD  ๐"
@bot.message_handler(func=lambda message: message.text == 'TD  ๐' and message.content_type == 'text')
def tdGL(message: types.Message):
        link = 'https://drive.google.com/uc?export=download&id=170cn8bBPB8scLfcvaF2xK6lDyeBkCYKF'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'conception des logiciels.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1W2SMPYn0P9k5c8xB1IhDtK6B1m_6ZWCN'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'suit TD1.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1-iOP7dtBh0v506BMkmFoMaDeCPK_dWYR'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'TD2.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1YLUSpxkW9cuE4kZqUNvb1vhrBYj0ATJv'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'TD3.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1yzNC6khnjASt8inid9zb_JIXPWztmIbn'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'TD4.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1lePCiV8usQuYZTWF4ork6ue7avkK9xrC'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'TD5.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1wE6Ni6slM5UZCWfLSDJgXcDfKjZXYzzv'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'TD6.pdf'))
        except:
            pass
        link = 'https://drive.google.com/uc?export=download&id=1DQoLBxk67fRv00gLcV94IEC1-rA3e7AG'
        try :
           bot.send_document(message.chat.id, data=downDocs(link,'TD7.pdf'))
        except:
            pass

#listener --> "TD Correction๐"
@bot.message_handler(func=lambda message: message.text == 'TD Correction๐' and message.content_type == 'text')
def ctGL(message: types.Message):
        link1 = 'https://drive.google.com/uc?export=download&id=1HSXGvzAr1CELn-ZTwfpp5utH39856xQH'
        try :
           bot.send_document(message.chat.id , data = downDocs(link1,'Correction TD1.pdf'))
        except:
            pass
        link2 = 'https://drive.google.com/uc?export=download&id=1BgROWIIVG0sBdt_rweKfH8uate3KeiKQ'
        try :
           bot.send_document(message.chat.id , data = downDocs(link2,'Correction TD2.pdf'))
        except:
            pass
        link3 = 'https://drive.google.com/uc?export=download&id=1r5ImCxee_-lEyAbTS65d5FT7rzHIFfO-'
        try :
           bot.send_document(message.chat.id , data = downDocs(link3,'Correction TD4.pdf'))
        except:
            pass
        link4 = 'https://drive.google.com/uc?export=download&id=1MyZb2Xi-Jm0eJQ-9lMGPiNVvR8LQQMsm'
        try :
           bot.send_document(message.chat.id , data = downDocs(link4,'Correction TD5.pdf'))
        except:
            pass
        link5 = 'https://drive.google.com/uc?export=download&id=1u9zAQfDeJ0BZO3RRcIwqPssYryduAIbZ'
        try :
           bot.send_document(message.chat.id, data=downDocs(link5,'Corrigรฉ EMD1 GL.pdf'))
        except:
            pass
        
#listener --> "Programmation objet ๐"
@bot.message_handler(func=lambda message: message.text == 'Programmation objet ๐' and message.content_type == 'text')
def c4_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD ๐')
    btn2 = types.KeyboardButton('TP ๐ป')
    btn3 = types.KeyboardButton('COURS ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Programmation objet ๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "Technologie web2๐"
@bot.message_handler(func=lambda message: message.text == 'Technologie web2๐' and message.content_type == 'text')
def c5_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TP ๐ป')
    btn2 = types.KeyboardButton('TP Correction ๐')
    btn3 = types.KeyboardButton('COURS ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Technologie web2๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "Systeme expert๐"
@bot.message_handler(func=lambda message: message.text == 'Systeme expert๐' and message.content_type == 'text')
def c6_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD ๐')
    btn2 = types.KeyboardButton('TP ๐ป')
    btn3 = types.KeyboardButton('COURS ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Systeme expert๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "Curricula et evaluation educative๐"
@bot.message_handler(func=lambda message: message.text == 'Curricula et evaluation educative๐' and message.content_type == 'text')
def c7_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD ๐')
    btn2 = types.KeyboardButton('TP ๐ป')
    btn3 = types.KeyboardButton('COURS ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Curricula et evaluation educative๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "Didactique๐"
@bot.message_handler(func=lambda message: message.text == 'Didactique๐' and message.content_type == 'text')
def c8_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('TD ๐')
    btn2 = types.KeyboardButton('TP ๐ป')
    btn3 = types.KeyboardButton('COURS ๐')
    btn4 = types.KeyboardButton('Go Back ๐๐')
    markup.row(btn3,btn2,btn1)
    markup.row(btn4)
    bot.send_message(message.chat.id,"Didactique๐\nSelect a button ๐ : ",reply_markup=markup)

#listener --> "TD ๐"
@bot.message_handler(func=lambda message: message.text == 'TD ๐' and message.content_type == 'text')
def tdM(message: types.Message):
    bot.send_message(message.chat.id,"Sorry no data yet !")


#listener --> "COURS ๐"
@bot.message_handler(func=lambda message: message.text == 'COURS ๐' and message.content_type == 'text')
def cM(message: types.Message):
    bot.send_message(message.chat.id,"Sorry no data yet !")

#listener --> "TP ๐ป"
@bot.message_handler(func=lambda message: message.text == 'TP ๐ป' and message.content_type == 'text')
def tpM(message: types.Message):
    bot.send_message(message.chat.id,"Sorry no data yet !")

#listener --> "TP Correction ๐"
@bot.message_handler(func=lambda message: message.text == 'TP Correction ๐' and message.content_type == 'text')
def cTM(message: types.Message):
    bot.send_message(message.chat.id,"Sorry no data yet !")

@bot.message_handler(func=lambda message: True)
def td_message(message: types.Message):
    bot.send_message(message.chat.id,"I didn't get that ! \n please pick one of the buttons \n or ask for /help ")    




#download documents function
def downDocs(url,fname):
    try :
        document=open(fname, 'rb')
    except :
        print('downloading...')
        r = requests.get(url, allow_redirects=True)
        open(fname, 'wb').write(r.content)
    
    finally :
        document=open(fname, 'rb')
    
    
    return document

#main function
if __name__ == "__main__":
    error = 0
    print('start...')
    while True :
        print('errors =  ', error)
        try :
            bot.polling(none_stop=True)
        except :
            error = error + 1

    
