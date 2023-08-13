from aiogram import types, Dispatcher

from bot.keyboards.user_keyboards import get_main_kb, get_main_ikb


async def cmd_start(msg: types.Message) -> None:
    """Command start

    Args:
        msg(types.Message): msg object
    """
    
    reply_text = 'WiHN бот тут, смотри команды по кнопке снизу!'

    await msg.answer(
        text=reply_text,
        reply_markup=get_main_kb()
    )


async def cmd_help(msg: types.Message) -> None:
    """Command help

    Args:
        msg(types.Message): msg object
    """

    reply_text = """
<b>/help</b> - <em>путеводитель по боту</em>
<b>/start</b> - <em>начало работы с ботом</em>
<b>/description</b> - <em>описание бота</em>"""

    if msg.text == '/help' or msg.text == 'Помощь 🔎':
        await msg.answer(text=reply_text, parse_mode='HTML')


async def cmd_description(msg: types.Message) -> None:
    """Command descritption

    Args:
        msg(types.Message): msg object
    """
    
    reply_text = 'WiHN Bot - новостной бот в телеграм, который отслеживает и оповещает о самых последних новостях в мире!'

    if msg.text == '/description' or msg.text == 'Бот 📗':
        await msg.answer(text=reply_text)


def register_user_handlers(dp: Dispatcher) -> None:
    """Register user handlers
    """

    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_description)
    dp.register_message_handler(cmd_help)
    
    