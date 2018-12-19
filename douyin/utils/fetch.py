import time
import requests
from retrying import retry
import random
from douyin.config import retry_max_number, retry_min_random_wait, retry_max_random_wait, fetch_timeout, common_headers


def need_retry(exception):
    """
    need to retry
    :param exception:
    :return:
    """
    result = isinstance(exception, (requests.ConnectionError, requests.ReadTimeout))
    if result:
        print('Exception', type(exception), 'occurred, retrying...')
    return result


# @retry(stop_max_attempt_number=retry_max_number, wait_random_min=retry_min_random_wait,
#        wait_random_max=retry_max_random_wait, retry_on_exception=need_retry)
def fetch(url, **kwargs):
    """
    warp _fetch method
    :param url: fetch url
    :param kwargs: other requests params
    :return: result of _fetch
    """
    kwargs.update({'verify': False})
    kwargs.update({'timeout': fetch_timeout})
    kwargs.update({'headers': common_headers})
    now = int(time.time())
    num = random.randint(100, 800)
    kwargs['params'].update({
            'ts': now,
            '_rticket': str(now) + str(num),
            'app_type': 'normal',
            'app_name': 'aweme',
            'js_sdk_version': '1.2.2',
            'ac': 'wifi',
            'os_version': '8.0.0',
            'version_code': '310',
            'version_name': '3.1.0',
            'device_brand': 'samsung',
            'device_platform': 'android',
            'device_type': 'SM-G9500',
            'resolution': '1440*2768',
            'language': 'en',
            'update_version_code': '3102'
        })
    response = requests.get(url, **kwargs)
    print(response)
    # print(response.json())
    # if response.status_code != 200:
    #     raise requests.ConnectionError('Expected status code 200, but got {}'.format(response.status_code))
    return response.json()


    # @retry(stop_max_attempt_number=retry_max_number, wait_random_min=retry_min_random_wait,
    #        wait_random_max=retry_max_random_wait, retry_on_exception=need_retry)
    # def _fetch(url, **kwargs):
    #     """
    #     fetch api response
    #     :param url: fetch url
    #     :param kwargs: other requests params
    #     :return: json of response
    #     """
    #     kwargs.update({'verify': False})
    #     kwargs.update({'timeout': fetch_timeout})
    #     kwargs.update({'headers': common_headers})
    #     response = requests.get(url, **kwargs)
    #     if response.status_code != 200:
    #         raise requests.ConnectionError('Expected status code 200, but got {}'.format(response.status_code))
    #     return response.json()
    #
    # try:
    #     result = _fetch(url, **kwargs)
    #     return result
    # # give up retrying
    # except (requests.ConnectionError, requests.ReadTimeout):
    #     return {}
