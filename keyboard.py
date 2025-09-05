from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class keyboards:
    
    def get_inline_keyboard_start():
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅ Проверить подписку 📢", callback_data="subscription")]
        ])
        return keyboard
    
    def get_inline_keyboard_menu():
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="👤 Профиль", callback_data="profile"),
                InlineKeyboardButton(text="📚 Обучение", callback_data="training"),
                InlineKeyboardButton(text="🛒 Магазин", callback_data="shop")
            ]
        ])
        return keyboard