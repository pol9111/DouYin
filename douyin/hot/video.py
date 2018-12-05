from douyin.config import hot_video_url
from douyin.structures import HotVideo
from douyin.utils import fetch
from douyin.utils.transform import data_to_video, parse_datetime


def video(**kwargs):
    """
    get hot video result
    :return: HotVideo object
    """
    kwargs.setdefault('params', {})
    result = fetch(hot_video_url, **kwargs)
    # process json data
    datetime = parse_datetime(result.get('active_time'))
    video_list = result.get('aweme_list', []) # 如果没有默认返回空列表
    videos = []
    for item in video_list:
        video = data_to_video(item.get('aweme_info')) # 通过util/transfer 转化成video对象
        video.hot_count = item.get('hot_value') # 直接传入video对象中
        videos.append(video)
    # construct HotVideo object and return
    return HotVideo(datetime=datetime, data=videos)
