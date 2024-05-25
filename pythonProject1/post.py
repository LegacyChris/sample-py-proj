class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author
        
    def get_details_of_author(self):
        print(f"Post: {self.message} was written by {self.author}!")