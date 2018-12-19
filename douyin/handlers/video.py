import base64
from douyin.handlers import FileHandler
from douyin.structures import Video
from douyin.utils.common import mix


class VideoFileHandler(FileHandler):
    
    async def process(self, obj, **kwargs):
        """
        process video obj
        :param obj:
        :param kwargs:
        :return:
        """
        if isinstance(obj, Video):
            patern = '{}i33@)@t@{};3@)u)@g3w)@fhuyq1fshhdf;4@{}_----/ss-o#o#{}../i:b-o#:`-o#pbfrh^+jt:#/.^'.format(mix(13),mix(15),mix(9),mix(13))
            rc = base64.b64encode(patern.encode('utf8')).decode()
            kwargs.update({'params': {'rc': rc}})  # 请求视频的参数
            kwargs.update({'headers': {
                'User-Agent': 'Lavf/57.71.100',
                'Accept-Encoding': 'identity',
                'Vpwp-Flag': '0',
                'Connection': 'Keep-Alive',
            }})
            return await self._process(obj, **kwargs)
