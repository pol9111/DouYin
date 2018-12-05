import douyin
from douyin.structures import Topic, Music

# define file handler and specify folder
video_file_handler = douyin.handlers.VideoFileHandler(folder='./videos')
music_file_handler = douyin.handlers.MusicFileHandler(folder='./musics')
# define mongodb handler
mongo_handler = douyin.handlers.MongoHandler(conn_uri='mongodb://Bridi:anNBU7MD@localhost:27017/')
# define downloader 下载热门音乐和话题, 并保存相关数据到mongo
downloader = douyin.downloaders.VideoDownloader([mongo_handler, video_file_handler, music_file_handler])

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 30 max per
        if isinstance(item, Topic):
            print('Item', item)
            downloader.download(item.videos(max=5))
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=2))
