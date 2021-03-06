import datetime
from copy import deepcopy


class Base(object):
    
    def json(self):
        """
        object to json
        :return:
        """
        from douyin.structures import Video, Music, User, Topic, Address
        # transfer object to dict
        d = deepcopy(self.__dict__)
        # iterate every attribute
        for k, v in d.items():
            if not v:
                continue # 如果数据的值为空, 则跳过
            # recurrent call json method
            if isinstance(v, (Video, Music, User, Topic, Address)):
                d[k] = v.json() # 如果数据的值是对象的话, 再次json
            # to string
            if isinstance(v, datetime.datetime):
                d[k] = str(v)
        return d # 最后返回格式化好的数据, 存入mongoDB
