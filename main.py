import asyncio
import datetime
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from settings import TOKEN

dp = Dispatcher()


class Schedule:
    schedule_list = []


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply("Hey, welcome!")


@dp.message()
async def upload_chesdule(message: Message):
    match message.text:
        case "/today":
            try:
                await message.answer(s.schedule_list[datetime.datetime.now().day - 1])
            except:
                await message.answer("Update your schedule")
        case "/tomorrow":
            try:
                await message.answer(s.schedule_list[datetime.datetime.now().day])
            except:
                await message.answer("Update your schedule")
        case "/weekend":
            today = datetime.datetime.now().day
            rest_of_the_month = Schedule.schedule_list[today:]
            for i, day in enumerate(rest_of_the_month):
                if day == "L":
                    await message.answer(f"Your weekend is in {i + 1} days")
        case _:
            schedule = message.text.split()
            Schedule.schedule_list = schedule
            await message.answer("Your schedule is list now!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    s = Schedule()
    asyncio.run(main())
