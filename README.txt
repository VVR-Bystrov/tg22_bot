30-11-24
Программа tg22_bot.py

The previous version was throwing a 502 error
This version adds:
1. **Exception handling**:
`bot.polling()` is now wrapped in a `while True` loop,
which will retry connection if exceptions occur.

2. **Error logging**:
When exceptions occur, error information will be output to the console.

3. **`polling` parameters**:
`none_stop=True` and `timeout=60` parameters have been added so that the bot can run continuously.

При работе предыдущей версии возникала ошибка 502
В эту версию добавлено:
1. **Обработка исключений**: 
         Теперь `bot.polling()` обернут в цикл `while True`, 
         который будет повторять попытки подключения в случае возникновения исключений.
  
2. **Логирование ошибок**: 
        При возникновении исключений информация об ошибках будет выводиться в консоль.

3. **Параметры `polling`**: 
        Добавлен параметр `none_stop=True` и `timeout=60`, чтобы бот мог работать непрерывно.
