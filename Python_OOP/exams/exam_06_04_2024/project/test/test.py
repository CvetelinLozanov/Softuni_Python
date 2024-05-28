import unittest
from exams.exam_06_04_2024.project.social_media import SocialMedia


class SocialMediaTest(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia("test_name", "Instagram", 5, "some_content")

    def test_initializer_with_correct_data(self):
        self.assertEqual("test_name", self.social_media._username)
        self.assertEqual("Instagram", self.social_media.platform)
        self.assertEqual(5, self.social_media.followers)
        self.assertEqual("some_content", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_initializer_with_wrong_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "some_platform"

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_initializer_with_negative_followers(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -5

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post_method(self):
        result = self.social_media.create_post("test_content")
        self.assertIn({'content': "test_content", 'likes': 0, 'comments': []}, self.social_media._posts)
        self.assertEqual(1, len(self.social_media._posts))
        self.assertEqual("New some_content post created by test_name on Instagram.", result)

    def test_like_post_method_with_negative_index(self):
        result = self.social_media.like_post(-1)
        self.assertEqual("Invalid post index.", result)

    def test_like_post_method_with_index_greater_than_length_of_posts(self):
        result = self.social_media.like_post(10)
        self.assertEqual("Invalid post index.", result)

    def test_like_post_method_with_likes_more_than_ten(self):
        self.social_media.create_post("test_content")
        self.social_media._posts[0]["likes"] = 11
        result = self.social_media.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", result)

    def test_like_post_method_with_nine_likes(self):
        self.social_media.create_post("test_content")
        self.social_media._posts[0]["likes"] = 9
        result = self.social_media.like_post(0)
        self.assertEqual("Post liked by test_name.", result)
        self.assertEqual(10, self.social_media._posts[0]["likes"])

    def test_comment_on_post_with_less_characters_than_ten(self):
        self.social_media.create_post("test_content")
        result = self.social_media.comment_on_post(0, "Azis")
        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_comment_on_post_with_correct_characters(self):
        self.social_media.create_post("test_content")
        result = self.social_media.comment_on_post(0, "lorem ipsum test")
        self.assertEqual("Comment added by test_name on the post.", result)
        self.assertIn({'user': 'test_name', 'comment': 'lorem ipsum test'}, self.social_media._posts[0]['comments'])


if __name__ == '__main__':
    unittest.main()