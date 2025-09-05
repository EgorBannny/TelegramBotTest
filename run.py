# Библиотеки
import asyncio
import logging
# Файлы бота
from config import config
from text_message import texts
from keyboard import keyboards
# aiogram
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

bot = Bot(config.TOKEN)
dp = Dispatcher()

# Команды 
@dp.message(Command('start'))
async def cmd_start(message: Message): 
    await message.answer(texts.welcome_text, reply_markup=keyboards.get_inline_keyboard_start())

# Обработка кнопок
@dp.callback_query(lambda call: call.data == "subscription")
async def check_subscription(call: CallbackQuery):
    user_id = call.from_user.id

    try:
        
        member = await bot.get_chat_member(config.CHANNEL_ID, user_id)
        if member.status in ["member", "administrator", "creator"]:
            
            try:
                await call.message.delete()
            except:
                pass  
            
            await bot.send_message(
                chat_id=call.message.chat.id,
                text=texts.menu_caption,  
                reply_markup=keyboards.get_inline_keyboard_menu()
            )
            await call.answer("✅ Вы подписаны!", show_alert=True)
        else:
            await call.answer("❌ Вы не подписаны!", show_alert=True)
    except Exception as e:
        print(f"Ошибка: {e}")
        await call.answer("❌ Ошибка проверки", show_alert=True)
        
# Запуск бота
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')