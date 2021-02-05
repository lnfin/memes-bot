from configuration import *


# Returns True if "likes history" is open for all people, False otherwise.
def check_likes_privacy(username, proxy_obj=None) -> bool:
    res = api.userLikedbyUsername(username, count=1, proxy=proxy_obj, language='en', region='US')
    return len(res) != 0


# Returns count of videos which were liked by @username.
def get_liked_video_count(username, proxy_obj=None) -> int:
    # todo: реализовать нормальный бинарный поиск, если будет серьезная просадка по времени
    for count in range(1, max_video_liked, 5):
        status = api.userLikedbyUsername(username, count=count, proxy=proxy_obj, language='en', region='US')
        if len(status) == 0:
            return count-1
    return max_video_liked


# Returns True if user exists, False otherwise.
def is_valid_username(username, proxy_obj=None) -> bool:
    try:
        # If user not found TikTokApi throws an exception :)
        api.getUserObject(username, language='en', proxy=proxy_obj)
        return True
    except exceptions.TikTokNotFoundError:
        return False