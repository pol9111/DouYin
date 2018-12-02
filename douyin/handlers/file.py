from os.path import join, exists
from os import makedirs
from douyin.handlers import Handler
from douyin.utils.type import mime_to_ext
import aiohttp


class FileHandler(Handler):
    
    def __init__(self, folder):
        """
        init save folder
        :param folder:
        """
        super().__init__()
        self.folder = folder
        if not exists(self.folder):
            makedirs(self.folder)
    
    async def _process(self, obj, **kwargs):
        """
        download to file
        :param url: resource url
        :param name: save name
        :param kwargs:
        :return:
        """
        print('Downloading', obj, '...')
        kwargs.update({'ssl': False}) # 设置不做证书认证
        kwargs.update({'timeout': 10}) # 设置超时为10秒
        async with aiohttp.ClientSession() as session:
            async with session.get(obj.play_url, **kwargs) as response:
                if response.status == 200:
                    extension = mime_to_ext(response.headers.get('Content-Type')) # 获取文件格式
                    full_path = join(self.folder, '%s.%s' % (obj.id, extension)) # 路径+文件名+格式
                    with open(full_path, 'wb') as f:
                        f.write(await response.content.read())
                    print('Downloaded file to', full_path)
                else:
                    print('Cannot download %s, response status %s' % (obj.id, response.status))
    
    async def process(self, obj, **kwargs):
        """
        process obj
        :param obj:
        :param kwargs:
        :return:
        """
        return await self._process(obj, **kwargs)
