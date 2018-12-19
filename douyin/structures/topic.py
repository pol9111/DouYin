from douyin.structures import Base
from douyin.utils.fetch import fetch
from douyin.config import topic2video_url, common_headers


class Topic(Base):
    
    def __init__(self, **kwargs):
        """
        init topic object
        :param kwargs:
        """
        super().__init__()
        self.id = kwargs.get('id')
        self.view_count = kwargs.get('view_count')
        self.user_count = kwargs.get('user_count')
        self.name = kwargs.get('name')
        self.desc = kwargs.get('desc')
    
    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Topic: <%s, %s>>' % (self.id, self.name)
    
    def videos(self, max=None, **kwargs):
        """
        get videos of topic
        :return:
        """
        from douyin.utils.transform import data_to_video
        if max and not isinstance(max, int): # 如果max存在, 但不是int的话
            raise RuntimeError('`max` param must be int')
        # query = {
        #     'device_id': '33333333',
        #     'ch_id': self.id,
        #     'count': '18',
        #     'aid': '1129'
        # }
        offset, count = 0, 0
        kwargs.update({'params': {
            'ch_id': self.id,
            'count': '20',
            # 'aid': '1128',
            # 'query_type': '0',
            # 'retry_type': 'no_retry',
            # 'click_reason': '0',
            # 'channel': 'tianzhuo_dy_wifi1',
            # 'dpi': '640',
            # 'os_api': '26',
            # 'openudid': 'f5cb4100b4812e13',
            # 'manifest_version_code': '310',
            # 'iid': '49186176872',
            # 'cp': '04c2ce573f86014ee1]qKu',
            # 'as': 'a155b0d0236cfc14782322',

        }})
        # while True:
        # define cursor
        kwargs['params'].update({
            'cursor': str(offset),
        })
        # query['cursor'] = str(offset)
        result = fetch(topic2video_url, **kwargs)
        print(result)
        print(result.get('aweme_list', None))
        aweme_list = result.get('aweme_list', []) # result是排行榜的json格式
        for item in aweme_list:
            video = data_to_video(item) # 把数据转换成视频对象
            count += 1
            yield video
            if max and count >= max: # 超过即返回
                return
            # next page
            # if result.get('has_more'):
            #     offset += 20
            # else:
            #     break
