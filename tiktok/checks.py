from gevent import monkey
monkey.patch_all()

import os
import sys
import queue
from threading import Thread
from configuration import *


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


# Returns True if "likes history" is open for all people, False otherwise.
def check_likes_privacy(username, proxy_obj=None, q=None) -> bool:
    res = api.userLikedbyUsername(username, count=1, proxy=proxy_obj, language='en', region='US')
    is_ok = len(res) != 0
    if q is None:
        return is_ok
    q.put(is_ok)



# Returns count of videos which were liked by @username.
def get_liked_video_count(username, proxy_obj=None) -> int:
    # todo: реализовать нормальный бинарный поиск, если будет серьезная просадка по времени
    for count in range(1, max_video_liked, 5):
        status = api.userLikedbyUsername(username, count=count, proxy=proxy_obj, language='en', region='US')
        if len(status) == 0:
            return count - 1
    return max_video_liked


# Returns True if user exists, False otherwise.
def is_valid_username(username, proxy_obj=None) -> bool:
    try:
        # If user not found TikTokApi throws an exception :)
        api.getUserObject(username, language='en', proxy=proxy_obj)
        return True
    except exceptions.TikTokNotFoundError:
        return False

# multithreading analogs


def m_check_likes_privacy(username, proxy_obj=None) -> bool:
    temp_q = queue.Queue()
    th1 = Thread(
        target=check_likes_privacy,
        args=(username, proxy_obj, temp_q)
    )
    th1.setName("searcher")
    th1.start()
    return temp_q.get()