class Movie:
    def __init__(self, name, genre,watched):
        self.name = name 
        self.genre = genre
        self.watched = watched   
    
    def __repr__(self) -> str:
        return f"<Movie {self.name}>"
    
    def json(self):
        return {
            'name': self.name, 
            'genre': self.genre,
            'watched':self.watched
        }
    
    @classmethod
    def from_json(cls, json_data):
        return Movie(**json_data)