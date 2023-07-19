#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Lệnh quản trị:</u>**

**c** là viết tắt của phát kênh.

/pause hoặc /cpause - Tạm dừng nhạc đang phát.
/resume hoặc /cresume- Tiếp tục nhạc bị tạm dừng.
/mute hoặc /cmute- Tắt tiếng nhạc đang phát.
/bật tiếng hoặc /cunmute- Bật tiếng nhạc bị tắt tiếng.
/skip hoặc /cskip- Bỏ qua nhạc đang phát.
/stop hoặc /cstop- Dừng phát nhạc.
/shuffle hoặc /cshuffle- Xáo trộn ngẫu nhiên danh sách phát đã xếp hàng đợi.
/seek hoặc /cseek - Chuyển tiếp Tìm kiếm nhạc theo thời lượng của bạn
/seekback hoặc /cseekback - Lùi Tìm nhạc theo thời lượng của bạn
/restart - Khởi động lại bot cho cuộc trò chuyện của bạn.


✅<u>**Bỏ qua cụ thể:**</u>
/skip hoặc /cskip [Số (ví dụ: 3)]
    - Bỏ qua âm nhạc đến một số hàng đợi được chỉ định. Ví dụ: /skip 3 sẽ bỏ qua nhạc đến nhạc xếp hàng thứ ba và sẽ bỏ qua nhạc 1 và 2 trong hàng đợi.

✅<u>**Chơi vòng lặp:**</u>
/loop hoặc /cloop [bật/tắt] hoặc [Các số từ 1-10]
    - Khi được kích hoạt, bot sẽ lặp lại đoạn nhạc đang phát từ 1-10 lần khi trò chuyện bằng giọng nói. Mặc định là 10 lần.

✅<u>**Người dùng xác thực:**</u>
Người dùng xác thực có thể sử dụng các lệnh quản trị mà không có quyền quản trị trong cuộc trò chuyện của bạn.

/auth [Tên người dùng] - Thêm người dùng vào DANH SÁCH AUTH của nhóm.
/unauth [Tên người dùng] - Xóa người dùng khỏi DANH SÁCH AUTH của nhóm.
/authusers - Kiểm tra DANH SÁCH AUTH của nhóm."""


HELP_2 = """✅<u>**Lệnh chơi:**</u>

Các lệnh có sẵn = play , vplay , cplay

Lệnh ForcePlay = playforce , vplayforce , cplayforce

**c** là viết tắt của phát kênh.
**v** là viết tắt của phát video.
**force** là viết tắt của chơi ép buộc.

/play hoặc /vplay hoặc /cplay - Bot sẽ bắt đầu phát truy vấn đã cho của bạn trong trò chuyện thoại hoặc Phát liên kết trực tiếp trên các cuộc trò chuyện thoại.

/playforce hoặc /vplayforce hoặc /cplayforce - **Force Play** dừng bản nhạc đang phát trên trò chuyện thoại và bắt đầu phát bản nhạc đã tìm kiếm ngay lập tức mà không làm phiền/xóa hàng đợi.

/channelplay [Tên người dùng hoặc id trò chuyện] hoặc [Tắt] - Kết nối kênh với một nhóm và truyền phát nhạc trên cuộc trò chuyện thoại của kênh từ nhóm của bạn.

✅**<u>Danh sách phát trên máy chủ của Bot:</u>**
/playlist - Kiểm tra danh sách phát đã lưu của bạn trên máy chủ.
/deleteplaylist - Xóa mọi bản nhạc đã lưu trong danh sách phát của bạn
/play - Bắt đầu phát Danh sách phát đã lưu của bạn từ Máy chủ."""


HELP_3 = """✅<u>**Lệnh của bot:**</u>

/stats - Nhận số liệu thống kê toàn cầu về 10 bản nhạc hàng đầu, 10 người dùng bot hàng đầu, 10 cuộc trò chuyện hàng đầu trên bot, 10 người chơi hàng đầu trong một cuộc trò chuyện, v.v.

/sudolist - Kiểm tra Người dùng Sudo của Yukki Music Bot

/lyrics [Tên nhạc] - Tìm kiếm lời bài hát cho Nhạc cụ thể trên web.

/song [Tên bản nhạc] hoặc [YT Link] - Tải xuống bất kỳ bản nhạc nào từ youtube ở định dạng mp3 hoặc mp4.

/player - Nhận Bảng chơi tương tác.

**c** là viết tắt của phát kênh.

/queue hoặc /cqueue- Kiểm tra danh sách nhạc trong hàng đợi."""

HELP_4 = """✅<u>**Lệnh bổ sung:**</u>
/start - Bắt đầu Music Bot.
/help - Nhận Menu Trình trợ giúp Lệnh với giải thích chi tiết về các lệnh.
/ping- Ping Bot và kiểm tra chỉ số Ram, Cpu, v.v. của Bot.

✅<u>**Cài đặt nhóm:**</u>
/settings - Nhận cài đặt của nhóm hoàn chỉnh bằng các nút nội tuyến

🔗 **Tùy chọn trong Cài đặt:**

1️⃣ Bạn có thể đặt **Chất lượng âm thanh** mà bạn muốn phát trên trò chuyện thoại.

2️⃣ Bạn có thể đặt **Chất lượng video** mà bạn muốn phát trên trò chuyện thoại.

3️⃣ **Người dùng xác thực**: - Bạn có thể thay đổi chế độ lệnh của quản trị viên từ đây thành mọi người hoặc chỉ quản trị viên. Nếu mọi người, bất kỳ ai có mặt trong nhóm của bạn đều có thể sử dụng các lệnh của quản trị viên (như /skip, /stop, v.v.)

4️⃣ **Chế độ sạch:** Khi được bật, bot sẽ xóa các tin nhắn khỏi nhóm của bạn sau 5 phút để đảm bảo cuộc trò chuyện của bạn vẫn sạch sẽ và tốt.

5️⃣ **Command Clean** : Khi được kích hoạt, Bot sẽ xóa các lệnh đã thực thi của nó (/play, /pause, /shuffle, /stop, v.v.) ngay lập tức.

6️⃣ **Cài đặt chơi:**

/playmode - Nhận bảng cài đặt phát hoàn chỉnh với các nút nơi bạn có thể đặt cài đặt phát cho nhóm của mình.

<u>Các tùy chọn trong chế độ phát:</u>

1️⃣ **Chế độ tìm kiếm** [Trực tiếp hoặc Nội tuyến] - Thay đổi chế độ tìm kiếm của bạn trong khi bạn cung cấp /chế độ phát.

2️⃣ **Lệnh quản trị viên** [Mọi người hoặc Quản trị viên] - Nếu mọi người, bất kỳ ai có mặt trong nhóm của bạn sẽ có thể sử dụng các lệnh quản trị viên (như /skip, /stop, v.v.)

3️⃣ **Loại phát** [Mọi người hoặc Quản trị viên] - Nếu là quản trị viên, chỉ quản trị viên có mặt trong nhóm mới có thể phát nhạc trong trò chuyện thoại."""

HELP_5 = """🔰**<u>THÊM VÀ XÓA NGƯỜI DÙNG SUDO :</u>**
/addsudo [Tên người dùng hoặc Trả lời người dùng]
/delsudo [Tên người dùng hoặc Trả lời người dùng]

🛃**<u>HEROKU:</u>**
/ cách sử dụng - Cách sử dụng Dyno.

🌐**<u>CẤU HÌNH VARS:</u>**
/get_var - Nhận một var cấu hình từ Heroku hoặc .env.
/del_var - Xóa bất kỳ var nào trên Heroku hoặc .env.
/set_var [Tên biến] [Giá trị] - Đặt biến hoặc cập nhật biến trên heroku hoặc .env. Tách Var và Giá trị của nó bằng một khoảng trắng.

🤖**<u>LỆNH BOT:</u>**
/reboot - Khởi động lại Bot của bạn.
/update - Cập nhật Bot.
/speedtest - Kiểm tra tốc độ máy chủ
/bảo trì [bật/tắt]
/logger [bật/tắt] - Bot ghi lại các truy vấn đã tìm kiếm trong nhóm nhật ký.
/get_log [Số dòng] - Nhận nhật ký bot của bạn từ heroku hoặc vps. Hoạt động cho cả hai.
/autoend [bật|tắt] - Bật Tự động kết thúc luồng sau 3 phút nếu không có ai nghe.

📈**<u>LỆNH THỐNG KÊ:</u>**
/activevoice - Kiểm tra các cuộc trò chuyện bằng giọng nói đang hoạt động trên bot.
/activevideo - Kiểm tra các cuộc gọi video đang hoạt động trên bot.
/stats - Kiểm tra số liệu thống kê bot

⚠️**<u>CHỨC NĂNG TRÒ CHUYỆN TRONG DANH SÁCH ĐEN:</u>**
/blacklistchat [CHAT_ID] - Đưa vào danh sách đen mọi cuộc trò chuyện sử dụng Music Bot
/whitelistchat [CHAT_ID] - Đưa bất kỳ cuộc trò chuyện nào vào danh sách đen vào danh sách cấm sử dụng Music Bot
/blacklistedchat - Kiểm tra tất cả các cuộc trò chuyện trong danh sách đen.

👤**<u>CHỨC NĂNG BỊ CHẶN:</u>**
/block [Tên người dùng hoặc Trả lời người dùng] - Ngăn người dùng sử dụng lệnh bot.
/unblock [Tên người dùng hoặc Trả lời người dùng] - Xóa người dùng khỏi Danh sách chặn của Bot.
/blockedusers - Kiểm tra danh sách người dùng bị chặn

👤**<u>CHỨC NĂNG GBAN:</u>**
/gban [Tên người dùng hoặc Trả lời người dùng] - Gban người dùng khỏi cuộc trò chuyện do bot cung cấp và ngăn anh ta sử dụng bot của bạn.
/ungban [Tên người dùng hoặc Trả lời người dùng] - Xóa người dùng khỏi Danh sách bị cấm của Bot và cho phép anh ta sử dụng bot của bạn
/gbannedusers - Kiểm tra danh sách người dùng bị Gbanned

🎥**<u>CHỨC NĂNG CUỘC GỌI VIDEO:</u>**
/set_video_limit [Số lượng Trò chuyện] - Đặt Số lượng Trò chuyện tối đa được phép cho Cuộc gọi video tại một thời điểm. Mặc định là 3 cuộc trò chuyện.
/videomode [download|m3u8] - Nếu bật chế độ tải xuống, Bot sẽ tải xuống video thay vì phát chúng ở dạng M3u8. Theo Mặc định cho M3u8. Bạn có thể sử dụng chế độ tải xuống khi bất kỳ truy vấn nào không phát ở chế độ m3u8.

⚡️**<u>CHỨC NĂNG BOT RIÊNG TƯ:</u>**
/ủy quyền [CHAT_ID] - Cho phép trò chuyện để sử dụng bot của bạn.
/unauthorize [CHAT_ID] - Không cho phép trò chuyện sử dụng bot của bạn.
/ ủy quyền - Kiểm tra tất cả các cuộc trò chuyện được phép của bot của bạn.

🌐**<u>CHỨC NĂNG PHÁT SÓNG:</u>**
/broadcast [Tin nhắn hoặc Trả lời tin nhắn] - Phát bất kỳ tin nhắn nào tới các cuộc trò chuyện được phân phát của Bot.

<u>các tùy chọn phát sóng:</u>
**-pin** : Thao tác này sẽ ghim tin nhắn của bạn
**-pinloud** : Điều này sẽ ghim tin nhắn của bạn với thông báo lớn
**-user** : Thao tác này sẽ phát tin nhắn của bạn tới những người dùng đã khởi động bot của bạn.
**-assistant** : Thao tác này sẽ phát tin nhắn của bạn từ tài khoản trợ lý của bot.
**-nobot** : Điều này sẽ buộc bot của bạn không phát tin nhắn

**Ví dụ:** `/broadcast -user -assistant -pin Thử nghiệm xin chào`

"""
