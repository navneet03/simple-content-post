from django.utils import timezone
from post_app.models import *


class PostDbService(object):

    def get_all_post_details(self, user):
        """
        :param user: user object
        :return: all the post_content data as list
        """
        post_obj_list = ContentPost.objects.all()
        post_det_list = []
        for post_obj in post_obj_list:
            temp_dict = {"post_id": post_obj.post_id, "author": post_obj.author.get_full_name(),
                         "title": post_obj.title, "content":post_obj.content,
                         "publish_time": post_obj.publish, "likes": post_obj.total_likes()}
            likes_user_list = []
            your_like = self.get_user_list_of_likes_post(post_obj, user, likes_user_list)
            temp_dict["likes_name"] = likes_user_list
            temp_dict["your_like"] = your_like
            post_det_list.append(temp_dict)
        return post_det_list

    def save_post_data(self, user, data):
        """
        save the new post details and returns
        :param user: user object
        :param data: new post data
        :return: new post_content details
        """
        post_obj = ContentPost(author=user)
        post_obj.title = data["title"]
        post_obj.content = data["content"]
        post_obj.publish = timezone.now()
        post_obj.save()
        post_details = {"post_id": post_obj.post_id, "author": post_obj.author.get_full_name(),
                        "publish_time": post_obj.publish, "likes": post_obj.total_likes()}

        likes_user_list = []
        your_like = self.get_user_list_of_likes_post(post_obj, user, likes_user_list)
        post_details["likes_name"] = likes_user_list
        return post_details

    def update_post_like(self, user, post_id):
        """
        update the like of post
        :param user: user object
        :param post_id:
        :return: current like post data
        """
        post_obj = ContentPost.objects.get(pk=post_id)
        if post_obj.likes.filter(user_id=user.user_id).exists():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like_details = {"likes": post_obj.total_likes()}
        likes_user_list = []
        your_like = self.get_user_list_of_likes_post(post_obj, user, likes_user_list)
        like_details["likes_name"] = likes_user_list
        return like_details

    @staticmethod
    def get_user_list_of_likes_post(post_obj, user, likes_user_list):
        """
        update the likes_user_list and your like
        :param post_obj:
        :param user: user object
        :param likes_user_list: list
        :return: your like status of post
        """
        your_like = None
        like_user_objs = post_obj.likes.all()
        for user_obj in like_user_objs:
            likes_user_list.append(user_obj.get_full_name())
            if user_obj == user:
                your_like = True
        return your_like