from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import random
#для генерации рандомного id
import time
import os
def send(message=None, attachment=None, keyboard=None):
  vk.messages.send(peer_id=event.peer_id, message=message, attachment=attachment, keyboard=keyboard, random_id=random.randint(-2147483648,+2147483648))
#всё пишется с отступом
def create_keys():
  keyboard = VkKeyboard(one_time = False)

  keyboard.add_button('Связь с нами', color=VkKeyboardColor.DEFAULT)
#наши контакты
  keyboard.add_button('Статус', color=VkKeyboardColor.DEFAULT)
#статус(для проверки)
  keyboard.add_line()
  keyboard.add_button('О боте', color=VkKeyboardColor.DEFAULT)
  keyboard.add_button('Помощь', color=VkKeyboardColor.DEFAULT)
#о боте
  keyboard.add_line()
  keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)
#закрытие клавы
  keyboard = keyboard.get_keyboard()
  return keyboard

def close_keys():
  keyboard = VkKeyboard(one_time = True)
  return keyboard.get_empty_keyboard()

token = "YourToken"
vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
start_time = time.monotonic()
while(1 == 1):
  for event in longpoll.listen():
      if(event.type == VkEventType.MESSAGE_NEW):
        keyboard = create_key(event)
        Close = close_keys()
        response = event.text.lower()
        print(response)
        if(event.from_user and not event.from_me):
          kolvo = kolvo + 1
          if(response == 'связь с нами'):
            send(message='''
С администратором можно связаться используя почту: admin@thesimpleblog.site
Или в ВК - *karagozov (Андрей)
Если он не отвечает можно написать *557200191 (Олегу),
А если и он не отвечает, то напишите *nikanikto (Нике) или *aydova3 (Ире).
            ''')
          elif(response == 'статус'):
            direc = os.getcwd()
            time = start_time - time.monotonic()
            send(message='''
Рабочая директория - ''' +direc +'''
Время с момента запуска - ''' +str(time) +''' секунд
Всего боту отправлено - ''' +str(kolvo) +''' сообщений
            ''')
          elif(response == 'о боте'):
            send(message='''
Бот был разработан для написания статьи в блоге *karagozov (Андреем)
Бот исключительно для личных сообщений группы.
Код данного бота - opensourse, а также может свободно использоваться без указания автора
            ''')
          elif(response == 'помощь'):
            send(message='Вот, что я могу:', keyboard=keyboard)
          elif(response == 'закрыть'):
            send(message='&#13;', keyboard=Close)
