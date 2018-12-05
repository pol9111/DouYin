import douyin

# # HotMusic 获取音乐榜榜视频列表
# result = douyin.hot.music()
# # music objects
# musics = result.data
# # print every music
# for music in musics:
#     print(music)
#
# # define handler and specify folder
# handler = douyin.handlers.MusicFileHandler(folder='./musics')
# # define downloader
# downloader = douyin.downloaders.MusicDownloader([handler])
# # download musics
# downloader.download(musics)

# get hot video result 获取视频榜视频列表
result = douyin.hot.video()
# video objects拿到视频列表
videos = result.data
# print every video迭代视频列表
for video in videos:
    print(video)

# define handler and specify folder定义为文件处理
handler = douyin.handlers.VideoFileHandler(folder='./videos')
# define downloader异步下载视频
downloader = douyin.downloaders.VideoDownloader([handler])
# download videos更新进度条
downloader.download(videos)
