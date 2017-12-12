[Like network file format]

* For more information, please check http://instagram.com/developer/
* All fields are divided by |  (w/o quotes)

1. instagram_data_media_XX
user_id | media_id | type | effect | media_url | timestamp | # likes | # comments | depth

2. instagram_data_media_caption_XX
user_id | media_id | caption | depth

3. instagram_data_media_comments_XX
user_id | media_id | timestamp | commented_user | depth

4. instagram_data_media_comments_text_XX
user_id | media_id | commented_user | comment

5. instagram_data_media_location_XX (note: many of data do not contain location info)
user_id | media_id | latitude | longitude | location_text | depth

6. instagram_data_media_tags_XX
user_id | media_id | list of tags separated by ????| depth 

7. instagram_users
user_id
