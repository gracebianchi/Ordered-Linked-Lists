# Movie.py

class Movie:

    def __init__(self, movieName, director, year, rating = None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = int(year)
        self.rating = rating

    def getMovieName(self):
        return self.movieName

    def getDirector(self):
        return self.director

    def getYear(self):
        return self.year

    def getRating(self):
        return self.rating

    def formatDirector(self):
        last, first = self.director.split(", ")
        return f"{first.upper()} {last.upper()}"

    def getMovieDetails(self):
        format_director = self.formatDirector()
        return f"{self.movieName} directed by {format_director} ({self.year}), Rating: {self.rating}"

    def __gt__(self, other):
        if self.director == other.director:
            if self.year == other.year:
                return self.movieName > other.movieName
            return self.year > other.year
        return self.director > other.director


