from douyin.handlers import FileHandler
from douyin.structures import Music


class MusicFileHandler(FileHandler):
    
    async def process(self, obj, **kwargs):
        """
        process music
        :param obj:
        :param kwargs:
        :return:
        """
        if isinstance(obj, Music):
            kwargs.update({'headers': {
                'User-Agent': 'stagefright/1.2 (Linux;Android 8.0.0)',
            }})
            return await self._process(obj, **kwargs)
