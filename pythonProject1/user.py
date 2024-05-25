class User:
    def __init__(self, username, password, email, cuurent_job_title):
        self.username = username
        self.password = password
        self.email = email
        self.current_job_title = cuurent_job_title

    def change_password(self, new_password):
        self.password = new_password

    # def update_email(self, new_email):
    #     self.email = new_email
    
    def update_job_title(self, new_job_title):
        self.current_job_title = new_job_title
        
    #create a function to display a user info
    def user_info(self):
        print(f"The user {self.username} is a {self.current_job_title} and can be reached via email {self.email}")
        