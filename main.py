import smtplib
import os

smtp_header = '''\
From: temporarydvm@yandex.ru
To: temporarydvm@yandex.ru
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";\n
'''

letter_template = '''
Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''

letter = letter_template.format(friend_name='Максим', my_name='Тимур', website='dvmn.org')
smtp_message = smtp_header + letter

login = os.getenv('YANDEX_LOGIN')
password = os.getenv('YANDEX_PASSWORD')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail('temporarydvm@yandex.ru', 'temporarydvm@yandex.ru', smtp_message.encode('UTF-8'))
server.quit()


