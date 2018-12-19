# urls
hot_search_url = 'https://api.amemv.com/aweme/v1/hot/search/list/'
hot_video_url = 'https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/'
hot_energy_url = 'https://api.amemv.com/aweme/v1/hotsearch/positive_energy/billboard/'
hot_music_url = 'https://api.amemv.com/aweme/v1/hotsearch/music/billboard/'
hot_trend_url = 'https://api.amemv.com/aweme/v1/category/list/'
# 跟换接口
topic2video_url = 'https://aweme.snssdk.com/aweme/v1/challenge/aweme/'
music2video_url = 'https://aweme.snssdk.com/aweme/v1/music/aweme/'
# topic2video_url = 'https://api.amemv.com/aweme/v1/challenge/aweme/'
# music2video_url = 'https://api.amemv.com/aweme/v1/music/aweme/'

# http
fetch_timeout = 5
common_headers = {
    # 'User-Agent': 'Aweme 2.9.1 rv:29101 (iPhone; iOS 12.0; zh_CN) Cronet',
    'User-Agent': 'com.ss.android.ugc.aweme/310 (Linux; U; Android 8.0.0; en_US; SM-G9500; Build/R16NW; Cronet/58.0.2991.0)',
    # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1',
}

# retrying
retry_max_number = 10
retry_min_random_wait = 1000  # ms
retry_max_random_wait = 5000  # ms


# hot_video_url = 'https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/?ts=1543926781&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=310&_rticket=1543926781219&ac=wifi&device_id=58851176365&iid=49186176872&os_version=8.0.0&channel=tianzhuo_dy_wifi1&version_code=310&device_type=SM-G9500&language=en&uuid=354765085131977&resolution=1440*2768&openudid=f5cb4100b4812e13&update_version_code=3102&app_name=aweme&version_name=3.1.0&os_api=26&device_brand=samsung&ssmix=a&device_platform=android&dpi=640&aid=1128&as=a195c7907d0ffc63466277&cp=70fdc654dd630637e1Sc%5Bg&mas=01a728ae4bed8313a043e1b9c60edacfc5ecec4c6c6c2ccc6cc666'
# hot_music_url = 'https://api.amemv.com/aweme/v1/hotsearch/music/billboard/?ts=1543926781&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=310&_rticket=1543926781222&ac=wifi&device_id=58851176365&iid=49186176872&os_version=8.0.0&channel=tianzhuo_dy_wifi1&version_code=310&device_type=SM-G9500&language=en&uuid=354765085131977&resolution=1440*2768&openudid=f5cb4100b4812e13&update_version_code=3102&app_name=aweme&version_name=3.1.0&os_api=26&device_brand=samsung&ssmix=a&device_platform=android&dpi=640&aid=1128&as=a175e750adafbc13d66600&cp=74f0cf5ad3680631e1Uc%5Dg&mas=01c2d18c8119440aafe7ade636784d53950c0c6c6c6c26cc8cc646'