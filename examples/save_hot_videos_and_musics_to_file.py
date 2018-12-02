import douyin

# HotMusic
result = douyin.hot.music()
# music objects
musics = result.data
# print every music
for music in musics:
    print(music)

# define handler and specify folder
handler = douyin.handlers.FileHandler(folder='./musics')
# define downloader
downloader = douyin.downloaders.MusicDownloader([handler])
# download musics
downloader.download(musics)

# get hot video result获取视频列表
result = douyin.hot.video()
# video objects拿到视频列表
videos = result.data
# print every video迭代视频列表
for video in videos:
    print(video)

# define handler and specify folder定义为文件处理
handler = douyin.handlers.FileHandler(folder='./videos')
# define downloader异步下载视频
downloader = douyin.downloaders.VideoDownloader([handler])
# download videos更新进度条
downloader.download(videos)
