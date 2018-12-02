from douyin.structures import Video
from douyin.handlers import Handler
from douyin.downloaders import Downloader


class VideoDownloader(Downloader):
    
    async def process_item(self, obj):
        """使用异步开始下载视频
        process item
        :param obj: single obj
        :return:
        """
        if isinstance(obj, Video): # 如果他是视频
            print('Processing', obj, '...')
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    await handler.process(obj) # 开始异步下载
