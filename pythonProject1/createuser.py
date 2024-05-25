from user import User
from post import Post

user_one = User("legacy", "pwd1", "chris@coils.com", "DevOps Engineer")
#user_one.user_info()
user_one.update_job_title("Senior DevOps Engineer")
user_one.user_info()

new_post = Post("Living intentionally is the best living", user_one.username)
new_post.get_details_of_author()