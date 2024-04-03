from telebot import *
name=''
course_name=''
phone_number=''
bot=bot = telebot.TeleBot("Your_Bot_Token")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup=types.InlineKeyboardMarkup(row_width=1)
    courses=types.InlineKeyboardButton("Courses",callback_data='courses')
    markup.add(courses)
    bot.send_message(message.chat.id, "Hello and welcome friends,To see the list of available courses press the list of Courses button",reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def courses(callback):
    if callback.message:
        markup=types.InlineKeyboardMarkup(row_width=3)
        register=types.InlineKeyboardMarkup(row_width=1)
        course1=types.InlineKeyboardButton("Course 1",callback_data='course1')
        course2=types.InlineKeyboardButton("Course 2",callback_data='course2')
        course3=types.InlineKeyboardButton("Course 3",callback_data='course3')
        course4=types.InlineKeyboardButton("Course 4",callback_data='course4')
        course5=types.InlineKeyboardButton("Course 5",callback_data='course5')
        course6=types.InlineKeyboardButton("Course 6",callback_data='course6')
        markup.add(course1,course2,course3,course4,course5,course6)
        if callback.data=="send":
             bot.send_message(callback.message.chat.id,"our admin contact you soon")
             bot.send_message(1237295903,callback.message.text)
        if callback.data=="edit":
             edit_markup=markup=types.InlineKeyboardMarkup(row_width=1)
             nameB=types.InlineKeyboardButton("Firstname And Lastname",callback_data='name')
             cnameB=types.InlineKeyboardButton("Course Name",callback_data='cname')
             pnumberB=types.InlineKeyboardButton("Phone Number",callback_data='pnumber')
             edit_markup.add(nameB,cnameB,pnumberB)
             data=bot.send_message(callback.message.chat.id, "select the part you want to edit",reply_markup=edit_markup)
        if callback.data=="name":
             data=bot.send_message(callback.message.chat.id, "Enter your firstname and last name again")
             bot.register_next_step_handler(data,edit_name)
        if callback.data=="cname":
             data=bot.send_message(callback.message.chat.id, "Enter your desired course name again")
             bot.register_next_step_handler(data,edit_course)    
        if callback.data=="pnumber":
             data=bot.send_message(callback.message.chat.id, "Enter your Phone number again")
             bot.register_next_step_handler(data,get_number)    
        if callback.data=="policy":
            data=bot.send_message(callback.message.chat.id, "Enter your first name and last name")
            bot.register_next_step_handler(data , get_name)
        if callback.data=="courses":
            bot.send_message(callback.message.chat.id,"Courses List",reply_markup=markup)
            bot.send_message(callback.message.chat.id,"For registeration use command /register ")
        elif callback.data=="course1":
             bot.send_message(callback.message.chat.id,"Course 1 descriptions:\n About Course Course capacity Course time Course duration Registration fee,etc",reply_markup=register)
        elif callback.data=="course2":
             bot.send_message(callback.message.chat.id,"Course 2 descriptions:\n About Course Course capacity Course time Course duration Registration fee,etc",reply_markup=register) 
        elif callback.data=="course3":
             bot.send_message(callback.message.chat.id,"Course 3 descriptions:\n About Course Course capacity Course time Course duration Registration fee,etc",reply_markup=register) 
        elif callback.data=="course4":
             bot.send_message(callback.message.chat.id,"Course 4 descriptions:\n About Course Course capacity Course time Course duration Registration fee,etc",reply_markup=register) 
        elif callback.data=="course5":
             bot.send_message(callback.message.chat.id,"Course 5 descriptions:\n About Course Course capacity Course time Course duration Registration fee,etc",reply_markup=register) 
        elif callback.data=="course6":
             bot.send_message(callback.message.chat.id,"Course 6 descriptions:\n About Course Course capacity Course time Course duration Registration fee,etc",reply_markup=register)        
@bot.message_handler(commands=['register'])
def handle_text(message):
    policy_markup=types.InlineKeyboardMarkup(row_width=1)
    policy=types.InlineKeyboardButton("I agree",callback_data='policy')
    policy_markup.add(policy)
    cid = message.chat.id
    bot.send_message(cid, "our courses policies and other informations",reply_markup=policy_markup)

def get_name(message):
     global name
     name=message.text 
     data=bot.send_message(message.chat.id,"Enter your desired course")
     bot.register_next_step_handler(data , get_course)
def get_course(message):
     global course_name
     course_name=message.text 
     data=bot.send_message(message.chat.id,"Enter your phone number")
     bot.register_next_step_handler(data , get_number)
def get_number(message):
     global phone_number
     global course_name
     global name
     a=message.text 
     editsend_markup=types.InlineKeyboardMarkup(row_width=2)
     send=types.InlineKeyboardButton("Send",callback_data='send')
     edit=types.InlineKeyboardButton("Edit",callback_data='edit')
     editsend_markup.add(send,edit)
     if a[0]=='0' and a[1]=='9' and len(a)==11:
          phone_number=message.text 
          test="your information: "+"\n"+ name +"\n"+ course_name +"\n"+ phone_number
          bot.send_message(message.chat.id,test,reply_markup=editsend_markup)  
     elif  a[0]=='\u06F0'and a[1]=='\u06F9' and len(a)==11:
          phone_number=message.text 
          test="your information: "+"\n"+ name +"\n"+ course_name +"\n"+ phone_number
          bot.send_message(message.chat.id,test,reply_markup=editsend_markup)   
     else:
         data=bot.send_message(message.chat.id,"it's not a phone number try again")
         bot.register_next_step_handler(data , get_number)
     
def edit_name(message):
     global name
     name=message.text 
     editsend_markup=types.InlineKeyboardMarkup(row_width=2)
     send=types.InlineKeyboardButton("Send",callback_data='send')
     edit=types.InlineKeyboardButton("Edit",callback_data='edit')
     editsend_markup.add(send,edit)
     test="your information: "+"\n"+ name +"\n"+ course_name +"\n"+ phone_number
     bot.send_message(message.chat.id,test,reply_markup=editsend_markup) 
def edit_course(message):
     global course_name
     course_name=message.text
     editsend_markup=types.InlineKeyboardMarkup(row_width=2)
     send=types.InlineKeyboardButton("Send",callback_data='send')
     edit=types.InlineKeyboardButton("Edit",callback_data='edit')
     editsend_markup.add(send,edit)
     test="your information: "+"\n"+ name +"\n"+ course_name +"\n"+ phone_number
     bot.send_message(message.chat.id,test,reply_markup=editsend_markup)   
bot.infinity_polling()
