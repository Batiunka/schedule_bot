import asyncio
import datetime
from os import getenv
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv("TOKEN")
ADMIN_ID = getenv("ADMIN_ID")
dp = Dispatcher()


class Schedule:
    schedule_list = []


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    print(f"new user {message.from_user.username} id {message.from_user.id}")
    await message.reply("Hey, welcome!")


def generate_reply(schedule, shift=0):
    try:
        shift_letter = schedule.schedule_list[datetime.datetime.now().day - shift]
    except Exception as e:
        print(f"Error generating the reply {e}")
        return "Update your schedule"
    match shift_letter:
        case "L":
            return "You can fly😎😎😎😎😎😎😎"
        case "M":
            return "You should go to bed (morning)"
        case "E":
            return "music for night ride turns on"
        case _:
            return "there is object unidentified"


@dp.message()
async def message_handler(message: Message):
    print(
        f"message {message.from_user.id} {message.from_user.username}: {message.text}"
    )
    try:
        match message.text:
            case "/today":
                await message.answer(generate_reply(s, 1))
            case "/tomorrow":
                await message.answer(generate_reply(s))
            case "/weekend":
                today = datetime.datetime.now().day
                rest_of_the_month = Schedule.schedule_list[today:]
                for i, day in enumerate(rest_of_the_month):
                    if day == "L":
                        await message.answer(f"Your weekend is in {i + 1} days")
                        break
            case _:
                if str(message.from_user.id) == ADMIN_ID:
                    schedule = message.text.split()
                    Schedule.schedule_list = schedule
                    await message.answer("Your schedule is list now!")
                else:
                    await message.answer("You know nothing, Jon Snow!")
    except Exception as e:
        print(f"Error {e}")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    print("bot created, starting to poll")
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("starting...")
    s = Schedule()
    asyncio.run(main())
