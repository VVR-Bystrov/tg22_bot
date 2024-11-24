
import telebot
import random
import threading
import time
from datetime import datetime

TOKEN = 'token'

bot = telebot.TeleBot(TOKEN)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_numbers():
    prime_numbers = []
    num = random.randint(1, 1000)
    while len(prime_numbers) < 10:
        if is_prime(num):
            prime_numbers.append(num)
        num = random.randint(1, 1000)
    return prime_numbers

def log_time():
    while True:
        with open('log_time.txt', 'a') as f:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{current_time}\n")
        time.sleep(300)  # 5 минут в секундах

# Запускаем функцию log_time в отдельном потоке
threading.Thread(target=log_time, daemon=True).start()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот. Как я могу помочь?")

@bot.message_handler(commands=['help'])
def handle_help(message):
    commands = [
        "/start - Начать общение с ботом",
        "/help - Получить помощь",
        "/perevorot <текст> - Перевернуть текст",
        "/cut <текст> - Удалить гласные из текста",
        "/num - Вывести первые десять случайных простых чисел"
    ]
    bot.send_message(message.chat.id, "Список доступных команд:\n" + "\n".join(commands))

@bot.message_handler(commands=['perevorot'])
def handle_perevorot(message):
    text = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else ''
    reversed_text = text[::-1]
    bot.send_message(message.chat.id, f"Перевернутый текст: {reversed_text}")

@bot.message_handler(commands=['cut'])
def handle_cut(message):
    vowels = 'aeiouAEIOUаАеЕиИоОуУяЯ'
    text = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else ''
    cut_text = ''.join([char for char in text if char not in vowels])
    bot.send_message(message.chat.id, f"Текст без гласных: {cut_text}")

@bot.message_handler(commands=['num'])
def handle_num(message):
    prime_numbers = generate_prime_numbers()
    bot.send_message(message.chat.id, f"Первые десять случайных простых чисел: {prime_numbers}")

bot.polling()
