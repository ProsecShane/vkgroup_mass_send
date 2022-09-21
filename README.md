# VK Group: Mass Message Sending Bot
## By ProsecShane

_(На русском языке ниже)_

This bot gives you the ability to send the same message to VK group members.
Made in Python using Requests.

## Installation

- Install [Python 3][pyinstall] on your PC.
- Check if Python 3 has been installed correctly by typing this into the Command Prompt:
```sh
python --version
```
- Install the Requests library. Wait until it fully installs.
```sh
pip install requests
```
- Clone this git repo (or install it's contents) and get ready to use it!

## Usage

- Please, do NOT rename the file names.
- Contact the admins of the Group you want to send the message from. Get the Access Token and make sure it allows to send messages. Clear the "token.txt" file and paste the token in there.
- Make sure that everyone, who you want to send the message to, has already sent any message (a sticker, for example) to the chat with the Group.
- Clear the "pages.txt" file and paste the pages of the recievers in there. The links to them can be in any format, however it must have at the end the id or the nickname after a forward slash or without anything before it. Every page must be in its own row! Here are working examples:
```sh
nickname
id123456789
vk.com/id123456789
https://vk.com/nickname
```
- Clear the "message.txt" file and paste your message in there.
- Open the Command Prompt (or any "cmd.exe"-equivalent in other systems). Make sure to navigate to the working folder and launch the application by typing: 
```sh
python main.py
```
- Wait until it finishes!

**If you have any questions, you can contact me at _prosecshane@yandex.ru_**

# ВК Сообщества: Массовая рассылка сообщений - Бот
## Сделал ProsecShane

Этот бот позволяет вам отправлять одно и то же сообщение участникам Сообщества ВК.
Сделано в Python с помощью библиотеки Requests.

## Установка

- Установите [Python 3][pyinstall] на ваш компьютер.
- Проверьте, правильно ли установился Python 3. Сделать это можно с помощью команды для Командной Строки:
```sh
python --version
```
- Установите библиотеку Requests. Подождите, пока она полностью установится.
```sh
pip install requests
```
- Склонируйте эту репозиторию (или скачайте её содержимое) и вы можете начинать пользоваться ботом!

## Использование

- НЕ переименовывайте имена файлов!
- Обратитесь к администраторам группы, от имени которой вы хотите посылать сообщения. Получите Токен, который обязательно должен иметь доступ к отправке сообщений. Очистите содержимое файла "token.txt" и вставьте туда токен.
- Убедитесь, что каждый, кому вы хотите отправить сообщение, заранее отправил любое сообщение (например, стикер) как личное сообщение для группы.
- Очистите содержимое файла "pages.txt" и вставьте туда страницы получателей. Ссылки на страницы могут быть в любом формате, главное, чтобы в конце ссылки был либо ID, либо никнейм после слэша или в строке должен быть ТОЛЬКО либо ID, либо никнейм. Каждая страница должна быть в своей строке! Вот рабочие примеры:
```sh
nickname
id123456789
vk.com/id123456789
https://vk.com/nickname
```
- Очистите содержимое файла "message.txt" и вставьте туда своё сообщение.
- Откройте Командную строку (или любой её эквивалент вне Windows). Убедитесь, что вы перешли в рабочую папку и начните рассылку с помощью команды:
```sh
python main.py
```
- Теперь ждите, пока пройдёт рассылка!

**Если есть вопросы по работе программы, можете писать мне сюда: _prosecshane@yandex.ru_**

> "Клуб любителей чипсов"

[pyinstall]: <https://www.python.org/>