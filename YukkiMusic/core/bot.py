#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Bot bắt đầu")
        super().__init__(
            "Coihaycoc",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bot bắt đầu"
            )
        except:
            LOGGER(__name__).error(
                "Bot không truy cập được vào Nhóm nhật ký. Đảm bảo rằng bạn đã thêm bot vào kênh nhật ký của mình và được thăng cấp làm quản trị viên!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Kiểm tra xem bot còn sống hay đã chết"),
                        BotCommand("play", "Bắt đầu phát bài hát được yêu cầu"),
                        BotCommand("skip", "Di chuyển đến bản nhạc tiếp theo trong hàng đợi"),
                        BotCommand("pause", "Tạm dừng bài hát đang phát"),
                        BotCommand("resume", "Tiếp tục bài hát bị tạm dừng"),
                        BotCommand("end", "Xóa hàng đợi và rời khỏi trò chuyện thoại"),
                        BotCommand("shuffle", "Xáo trộn ngẫu nhiên danh sách phát đã xếp hàng."),
                        BotCommand("playmode", "Cho phép bạn thay đổi chế độ phát mặc định cho cuộc trò chuyện của mình"),
                        BotCommand("settings", "Mở cài đặt của bot âm nhạc cho cuộc trò chuyện của bạn.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Vui lòng thăng cấp Bot làm Quản trị viên trong Logger Group"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot bắt đầu với tư cách là {self.name}")
