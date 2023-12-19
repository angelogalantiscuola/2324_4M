Design a class diagram UML and a Python program for a social media platform. Focus on representing users, posts, and their relationships. Utilize inheritance to model different types of posts and users.

1. **User:**
   - Attributes: UserID, Username, Email, Password, FriendsList, etc.
   - Methods: AddFriend, RemoveFriend, PostContent, etc.

2. **RegularUser (Derived from User):**
   - Additional attributes: Interests, ActivityLog, etc.
   - Methods: LikePost, CommentOnPost, etc.

3. **BusinessUser (Derived from User):**
   - Additional attributes: BusinessID, Products/Services, CustomerReviews, etc.
   - Methods: Advertise, RespondToReviews, etc.

4. **Post:**
   - Attributes: PostID, Content, Timestamp, LikesCount, Comments, etc.
   - Methods: Like, Comment, Share, etc.

5. **TextPost (Derived from Post):**
   - Additional attributes: WordCount, Language, etc.
   - Methods: AnalyzeSentiment, etc.

6. **ImagePost (Derived from Post):**
   - Additional attributes: ImageURL, Resolution, FiltersApplied, etc.
   - Methods: ApplyFilter, TagPeople, etc.

Establish associations such as:
- Users having a friends list and posting content.
- Regular users interacting with posts through likes and comments.
- Business users advertising and responding to customer reviews.
- Differentiating between TextPosts and ImagePosts.

Consider how inheritance allows for a more organized representation of user and post types. Explain your design choices and any assumptions made.
