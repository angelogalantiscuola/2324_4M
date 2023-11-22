#creation book base class
class Book:
    #creation attributes 
    def __init__(self, title, author, bookmark=0):
        self.title = title
        self.author = author
        self.bookmark = bookmark
    #creation methods bookmark_page
    def bookmark_page(self):
        print("Bookmarking page", self.bookmark)
    #creation method that represents the string format
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

#creation novel class
class Novel(Book):
    #creation new attributes
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    #creation methods get_genre
    def get_genre(self):
        return self.genre
    #creation method that represents the string format
    def __str__(self):
        return f"{super().__str__()}\nGenre: {self.genre}"

#creation scienze fiction class
class ScienceFiction(Novel):
    #creation new attributes
    def __init__(self, title, author, genre, futuristic_tech):
        super().__init__(title, author, genre)
        self.futuristic_tech = futuristic_tech
    #creation methods get_futuristic_tech
    def get_futuristic_tech(self):
        return self.futuristic_tech
    #creation method that represents the string format
    def __str__(self):
        return f"{super().__str__()}\nFuturistic Technology: {self.futuristic_tech}"

#creation fantasy class
class Fantasy(Novel):
    #creation new attributes
    def __init__(self, title, author, genre, magic_system):
        super().__init__(title, author, genre)
        self.magic_system = magic_system
    #creation methods get_magic_system
    def get_magic_system(self):
        return self.magic_system
    #creation method that represents the string format
    def __str__(self):
        return f"{super().__str__()}\nMagic System: {self.magic_system}"
