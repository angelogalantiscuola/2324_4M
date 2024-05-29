class User:
    def __init__(self, user_id, username, email, password):
        self.UserID = user_id
        self.Username = username
        self.Email = email
        self.Password = password
        self.FriendsList = []

    def add_friend(self, friend):
        self.FriendsList.append(friend)

    def remove_friend(self, friend):
        if friend in self.FriendsList:
            self.FriendsList.remove(friend)

    def post_content(self, content):
        pass
class RegularUser(User):
    def __init__(self, user_id, username, email, password, interests=[]):
        super().__init__(user_id, username, email, password)
        self.Interests = interests
        self.ActivityLog = []

    def like_post(self, post):
        pass  

    def comment_on_post(self, post, comment):
        pass  
class BusinessUser(User):
    def __init__(self, user_id, username, email, password, business_id, products=[]):
        super().__init__(user_id, username, email, password)
        self.BusinessID = business_id
        self.Products = products
        self.CustomerReviews = []

    def advertise(self):
        pass  

    def respond_to_reviews(self, review):
        self.CustomerReviews.append(review)

class Post:
    post_counter = 1

    def __init__(self, content):
        self.PostID = Post.post_counter
        Post.post_counter += 1
        self.Content = content
        self.LikesCount = 0
        self.Comments = []

    def like(self):
        self.LikesCount += 1

    def comment(self, comment):
        self.Comments.append(comment)
    def __str__(self):
        canzoni=""
        for i in self.post:
            canzoni+=i.__str__()+"\n"
        return f"Nome: {self.name} -Canzoni:\n{canzoni}"

class TextPost(Post):
    def __init__(self, content, word_count, language):
        super().__init__(content)
        self.WordCount = word_count
        self.Language = language

    def analyze_sentiment(self):
        pass  

class ImagePost(Post):
    def __init__(self, content, image_url, resolution):
        super().__init__(content)
        self.ImageURL = image_url
        self.Resolution = resolution

    def apply_filter(self, filter_type):
        pass 

user1 = RegularUser(1, "user1", "user1@email.com", "password123", interests=["Technology"])
user2 = BusinessUser(2, "business1", "business1@email.com", "businesspassword", business_id="B001", products=["ProductA"])

user1.add_friend(user2)
user2.advertise()

text_post = TextPost("This is a text post.", 50, "English")
image_post = ImagePost("Check out this image!", "image_url.jpg", "1080x720")

user1.post_content(text_post)
user1.post_content(image_post)

user1.like_post(text_post)
user1.comment_on_post(image_post, "Nice picture!")

print(user1.FriendsList)
print(user2.CustomerReviews)
print(text_post.LikesCount)
print(image_post.Comments)
