import collections

HotSearch = collections.namedtuple('HotSearch', ['datetime', 'data']) # 热搜(榜)类 30
HotVideo = collections.namedtuple('HotVideo', ['datetime', 'data']) # 视频(榜)类 20
HotEnergy = collections.namedtuple('HotVideo', ['datetime', 'data']) # 正能量(榜)类 20
HotMusic = collections.namedtuple('HotMusic', ['datetime', 'data']) # 音乐(榜)类 30
HotTrend = collections.namedtuple('HotTrend', ['datetime', 'data', 'count', 'offset']) # 热门话题+热门音乐