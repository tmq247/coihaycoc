#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\nNhập API_ID của bạn:\n > ")
API_HASH = input("\nNhập API_HASH của bạn:\n > ")

print("\n\n Nhập số điện thoại khi được hỏi.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    xx = f"ĐÂY LÀ PHIÊN CHUỖI CỦA BẠN, SAO CHÉP NÓ, ĐỪNG CHIA SẺ!!\n\n`{ss}`\n:)\n"
    ok = await i.send_message("me", xx)
    print("\nĐÂY LÀ PHIÊN CHUỖI CỦA BẠN, SAO CHÉP NÓ, KHÔNG CHIA SẺ!!\n")
    print(f"\n{ss}\n") 
    print("\n:)\n")


asyncio.run(main())
