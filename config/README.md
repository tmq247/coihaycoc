# Yukki Music Bot Configs

Các vars cấu hình về cơ bản là các biến định cấu hình hoặc sửa đổi bot để hoạt động, là những điều cơ bản cần thiết để plugin hoặc mã hoạt động. Bạn phải đặt các lọ bắt buộc phù hợp để làm cho nó hoạt động và bắt đầu tính năng cơ bản của bot.

### Tìm hiểu sâu về tất cả các lọ này từ Tài liệu của chúng tôi. [Read Now from Here](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/available-vars)

## Mandatory Vars

- Đây là những lọ tối thiểu bắt buộc phải thiết lập để Yukki Music Bot hoạt động.

1. `API_ID` : Lấy từ my.telegram.org
2. `API_HASH` : Lấy từ my.telegram.org
3. `BOT_TOKEN` : Nhận từ [@Botfather](http://t.me/BotFather) trong Telegram
4. `MONGO_DB_URI` : Nhận mongo db [từ đây.](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb)
5. `LOG_GROUP_ID` ​​: Bạn sẽ cần ID nhóm riêng cho việc này. Cần có siêu nhóm với id bắt đầu từ -100
6. `MUSIC_BOT_NAME` : Tên cho bot Âm nhạc của bạn.
7. `OWNER_ID` : ID chủ sở hữu để quản lý bot của bạn.
8. `STRING_SESSION` : Cần phiên Pyrogram, tạo chuỗi từ [@YukkiStringBot](http://t.me/YukkiStringBot) trong Telegram.

## Non-Mandatory Vars

- Đây là các lọ bổ sung cho các tính năng bổ sung bên trong Music Bot. Bạn có thể để lại các lọ không bắt buộc ngay bây giờ và có thể thêm chúng sau.

1. `DURATION_LIMIT` : Thời lượng âm thanh (nhạc) tối đa tùy chỉnh cho trò chuyện thoại. Mặc định là 60 phút.
2. `SONG_DOWNLOAD_DURATION_LIMIT` : Giới hạn thời lượng tải Bài hát ở định dạng MP3 hoặc MP4 từ bot. Mặc định là 180 phút.
3. `VIDEO_STREAM_LIMIT` : Số cuộc gọi video tối đa được phép trên bot. Sau đó, bạn có thể đặt nó qua /set_video_limit trên telegram. Mặc định là 3 cuộc trò chuyện.
4. `SERVER_PLAYLIST_LIMIT` : Giới hạn tối đa Cho phép người dùng lưu danh sách phát trên máy chủ của bot. Mặc định là 30
5. `PLAYLIST_FETCH_LIMIT` : Giới hạn tối đa cho việc tìm nạp bản nhạc của danh sách phát từ liên kết youtube, spotify, apple. Mặc định là 25
6. `CLEANMODE_MINS` : Thời gian Cleanmode sau đó bot sẽ xóa các tin nhắn cũ của nó khỏi các cuộc trò chuyện. Mặc định là 5 phút.
7. `SUPPORT_CHANNEL` : Nếu bạn có bất kỳ kênh nào cho bot âm nhạc của mình, hãy điền vào kênh đó bằng liên kết kênh của bạn
8. `SUPPORT_GROUP` : Nếu bạn có bất kỳ nhóm hỗ trợ nào cho bot âm nhạc của mình, hãy điền vào đó bằng liên kết nhóm của bạn

## Play FileSize Limit Vars

- Giới hạn kích thước tệp tối đa cho âm thanh và video mà người dùng có thể phát từ bot của bạn. [Chỉ chấp nhận kích thước byte]
> Bạn có thể chuyển đổi mb thành byte từ https://www.gbmb.org/mb-to-bytes và sử dụng tại đây

1. `TG_AUDIO_FILESIZE_LIMIT` : Giới hạn kích thước tệp tối đa cho các tệp âm thanh có thể được phát trực tuyến qua vc. Mặc định là 104857600 byte, tức là 100MB
2. `TG_VIDEO_FILESIZE_LIMIT` : Giới hạn kích thước tệp tối đa cho tệp video có thể phát. Mặc định là 1073741824 byte, tức là 1024MB hoặc 1GB

## Bot Vars

- Tất cả các lọ này được sử dụng để thiết lập bot. Bạn có thể chỉnh sửa các lọ này nếu muốn, nếu không thì hãy để nguyên tất cả chúng.

1. `PRIVATE_BOT_MODE` : Đặt là `True` nếu bạn muốn bot của mình chỉ ở chế độ riêng tư hoặc Sai cho tất cả các nhóm. Mặc định là Sai
2. `YOUTUBE_EDIT_SLEEP` : Thời lượng ngủ cho Trình tải xuống Youtube. Mặc định là 3 giây
3. `TELEGRAM_EDIT_SLEEP` : Thời lượng ngủ cho Telegram Downloader. Mặc định là 5 giây
4. `AUTO_LEAVING_ASSISTANT` : Đặt thành `True` nếu bạn muốn rời khỏi trợ lý của mình sau một khoảng thời gian nhất định.
5. `ASSISTANT_LEAVE_TIME` : Khoảng thời gian mà sau đó tài khoản trợ lý của bạn sẽ tự động rời khỏi các cuộc trò chuyện được cung cấp. Mặc định là 5400 giây, tức là 90 phút
6. `AUTO_DOWNLOADS_CLEAR` : Đặt là `True` nếu bạn muốn xóa các bản tải xuống sau khi phát nhạc kết thúc.
7. `AUTO_SUGGESTION_MODE` : Đặt nó là `True` nếu bạn muốn bot đề xuất các lệnh bot cho các cuộc trò chuyện ngẫu nhiên của các bot của bạn.
9. `AUTO_SUGGESTION_TIME` : Thời gian sau đó bot của bạn sẽ đề xuất ngẫu nhiên 1/10 cuộc trò chuyện trong số các cuộc trò chuyện được phục vụ của bạn về các lệnh bot. Mặc định là 5400 giây, tức là 90 phút
10. `SET_CMDS` : Đặt thành `True` nếu bạn muốn bot của mình tự động đặt các lệnh cho menu trò chuyện. [Tham khảo](https://i.postimg.cc/Bbg3LQTG/image.png)

## Spotify Vars

- Bạn có thể phát các bản nhạc hoặc danh sách phát từ spotify từ bot Yukki Music
- Bạn sẽ cần hai lọ này để làm cho spotify play hoạt động. Điều này không cần thiết, bạn có thể để trống nếu muốn.
  
### How to get these? [Read from here](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/spotify)


1. `SPOTIFY_CLIENT_ID` : Lấy từ https://developer.spotify.com/dashboard
2. `SPOTIFY_CLIENT_SECRET` : Lấy từ https://developer.spotify.com/dashboard


## Heroku Vars

- Để làm việc với một số mô-đun tương thích với Heroku, cần có giá trị var này để Truy cập tài khoản của bạn để sử dụng các lệnh `get_log`, `usage`, `update`, v.v.
- Bạn có thể điền vào biến này bằng cách sử dụng khóa API hoặc Mã thông báo ủy quyền của mình.

### How to get these? [Read from here](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/heroku-vars)

1. `HEROKU_API_KEY` : Lấy từ http://dashboard.heroku.com/account
2. `HEROKU_APP_NAME` : Bạn phải Nhập tên ứng dụng mà bạn đã cung cấp để xác định Music Bot của bạn trong Heroku.

## Custom Repo Vars

- Nếu bạn định sử dụng Yukki Music Bot với mã tùy chỉnh hoặc sửa đổi của riêng bạn.

1. `UPSTREAM_REPO` : URL Repo ngược dòng hoặc Repo rẽ nhánh của bạn.
2. `UPSTREAM_BRANCH` : Nhánh mặc định của URL Repo ngược dòng hoặc Repo rẽ nhánh của bạn.
3. `GIT_TOKEN` : GIT TOKEN của bạn nếu repo ngược dòng của bạn ở chế độ riêng tư
4. `GITHUB_REPO` : Url Github Repo của bạn, sẽ được hiển thị trên lệnh /start



## Images/Thumbnail Vars

- Bạn có thể thay đổi hình ảnh được sử dụng trong Yukki Music Bot.
- Bạn có thể tạo liên kết điện báo từ [@YukkiTelegraphBot](http://t.me/YukkiTelegraphBot) và sử dụng tại đây.

1. `START_IMG_URL` : Hình ảnh xuất hiện trên lệnh /start trong tin nhắn riêng tư của bot.
2. `PING_IMG_URL` : Hình ảnh xuất hiện trên lệnh /ping của bot.
3. `PLAYLIST_IMG_URL` : Hình ảnh xuất hiện trên lệnh /play của bot.
4. `GLOBAL_IMG_URL` : Hình ảnh xuất hiện trên lệnh /stats của bot.
5. `STATS_IMG_URL` : Hình ảnh xuất hiện trên lệnh /stats của bot.
6. `TELEGRAM_AUDIO_URL` : Hình ảnh này xuất hiện khi ai đó phát âm thanh từ telegram.
7. `TELEGRAM_VIDEO_URL` : Hình ảnh này xuất hiện khi ai đó phát video từ telegram.
8. `STREAM_IMG_URL` : hình ảnh của anh ấy xuất hiện khi ai đó chơi m3u8 hoặc liên kết chỉ mục.
9. `SOUNCLOUD_IMG_URL` : Hình ảnh này xuất hiện khi ai đó phát nhạc từ soundcloud.
10. `YOUTUBE_IMG_URL` : Hình ảnh này xuất hiện nếu trình tạo hình thu nhỏ không thành công.
11. `SPOTIFY_ARTIST_IMG_URL` : Hình ảnh này xuất hiện khi ai đó phát nghệ sĩ Spotify qua liên kết ở chế độ nội tuyến.
12. `SPOTIFY_ALBUM_IMG_URL` : Hình ảnh này xuất hiện khi ai đó phát album Spotify qua liên kết ở chế độ nội tuyến.
13. `SPOTIFY_PLAYLIST_IMG_URL` : Hình ảnh này xuất hiện khi ai đó phát album Spotify qua liên kết ở chế độ nội tuyến.

## Multi Assistant Mode

- Bạn có thể sử dụng tối đa 5 Trợ lý Khách hàng (cho phép bot của bạn hoạt động ít nhất trong 2000-2500 cuộc trò chuyện cùng một lúc)

1. `STRING_SESSION2` : Cần phiên Pyrogram, tạo chuỗi từ [@YukkiStringBot](http://t.me/YukkiStringBot) trong Telegram.
2. `STRING_SESSION3` : Cần phiên Pyrogram, tạo chuỗi từ [@YukkiStringBot](http://t.me/YukkiStringBot) trong Telegram.
3. `STRING_SESSION4` : Cần phiên Pyrogram, tạo chuỗi từ [@YukkiStringBot](http://t.me/YukkiStringBot) trong Telegram.
4. `STRING_SESSION5` : Cần phiên Pyrogram, tạo chuỗi từ [@YukkiStringBot](http://t.me/YukkiStringBot) trong Telegram.
