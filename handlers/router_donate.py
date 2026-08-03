from aiogram import Router, F
from aiogram.types import Message, LabeledPrice
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.pre_checkout_query import PreCheckoutQuery
from config import Bot

router_donate = Router()

def pay_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⭐ Донат ⭐", pay=True)
    return builder.as_markup()

@router_donate.message(Command("donate"))
async def donate(message: Message, command: CommandObject):
    if message.chat.type == "private":

        try:
            price = int(command.args)
            prices = [LabeledPrice(label="XTR", amount=price)]
            if price  > 2500:
                await message.answer("Извини, телеграмм не даёт донатить больше 2500 звёзд за раз.")
                return

            elif price <= 0:
                await message.answer("Ты чо еблан")
                return

            await message.answer_invoice(
                title=f"Донат на сумму {price} звёзд",
                description="Донат",
                prices=prices,
                provider_token="",
                payload="channel_support",
                currency="XTR",
                reply_markup=pay_keyboard()
            )
        except Exception as e:
            print(e)
            await message.answer("Ты неправильно ввёл сумму доната (например:\n/donate 5\nчтобы задонанить 5 звёзд)")
    else:
        await message.answer("Донатить можно только в личном чате с ботом.")

@router_donate.pre_checkout_query()
async def check(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)

@router_donate.message(Command("refund"))
async def refund(message: Message, bot: Bot, command: CommandObject):
    donate_id = command.args
    try:
        await bot.refund_star_payment(
            user_id = message.from_user.id,
            telegram_payment_charge_id=donate_id
        )
    except Exception as e:
        print(e)
        await message.answer("Произошла ошибка, может ты неправильно ввёл id доната.\nОшибка: {e}")

@router_donate.message(F.successful_payment)
async def refund_id(message: Message):
    await message.answer(f"Спасибо большое за донат!\n\nВот команда, если захочешь их вернуть, просто скопируй и отправь сообщением:")
    await message.answer(f"/refund {message.successful_payment.telegram_payment_charge_id}")