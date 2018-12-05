import douyin
from douyin.structures import Topic, Music

# define handler
mongo_handler = douyin.handlers.MongoHandler(conn_uri='mongodb://Bridi:anNBU7MD@localhost:27017/') # 实例化一个保存数据到mongo的处理对象
# define downloader and specify handler
downloader = douyin.downloaders.VideoDownloader([mongo_handler]) # 把该处理加入下载器todo列表中

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 100 max per
        if isinstance(item, Topic):
            print('Get topic', item)
            downloader.download(item.videos(max=10)) # 只保存前一百个视频数据到mongo
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=0))
