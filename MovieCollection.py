# MovieCollection.py

from Movie import Movie
from MovieCollectionNode import MovieCollectionNode

class MovieCollection:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfMovies(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def insertMovie(self, movie):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > movie:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = MovieCollectionNode(movie)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        

    def getAllMoviesInCollection(self):
        movie_current = self.head
        result = ''
        while movie_current is not None:
            movie = movie_current.getData()
            result += movie.getMovieDetails() + "\n"
            movie_current = movie_current.getNext()

        return result

    def getMoviesByDirector(self, director):
        movie_current = self.head
        result = ''
        director = director.upper()
        while movie_current is not None:
            movie = movie_current.getData()
            if movie.getDirector().upper() == director:
                result += movie.getMovieDetails() + "\n"
            movie_current = movie_current.getNext()

        return result

    def removeDirector(self, director):
        director = director.upper()
        current = self.head
        previous = None

        while current is not None:
            if current.getData().getDirector() == director:
                if previous == None:
                    self.head = current.getNext()
                else: 
                    previous.setNext(current.getNext())
            else:
                previous = current
            current = current.getNext()

    def avgDirectorRating(self, director):
        director = director.upper()
        movie_current = self.head
        sumrating = 0
        totalmovies = 0
        while movie_current is not None:
            movie = movie_current.getData()
            if movie.getDirector() == director and movie.getRating() is not None:
                sumrating += movie.getRating()
                totalmovies += 1
            movie_current = movie_current.getNext()

        if totalmovies > 0:
            return round(sumrating/totalmovies, 2)

    def recursiveSearchMovie(self, movieName, movieNode):
        if movieNode == None:
            return False
        if movieNode.getData().getMovieName().upper() == movieName.upper():
            return True
        return self.recursiveSearchMovie(movieName, movieNode.getNext())
        

