# testFile.py

from Movie import Movie
from MovieCollection import MovieCollection
from MovieCollectionNode import MovieCollectionNode


def test_Movie():
    m1 = Movie("Twilight", "Hardwicke, Catherine", 2008, 5.3)
    m2 = Movie("Harry Potter and the Goblet of Fire", "Newell, Mike", 2005, 7.7)
    assert m1.getMovieName() == "TWILIGHT"
    assert m1.getDirector() == "HARDWICKE, CATHERINE"
    assert m1.getYear() == 2008
    assert m1.getRating() == 5.3
    assert m1.getMovieDetails() == "TWILIGHT directed by CATHERINE HARDWICKE (2008), Rating: 5.3"
    assert m2 > m1
def test_MovieCollectionNode():
    m3 = Movie("Maleficent", "Stromberg, Robert", 2014, 6.9)
    node = MovieCollectionNode(m3)
    assert node.getData() == m3
    assert node.getNext() is None
def test_MovieCollection():
    m4 = Movie("Home Alone", "Columbus, Chris", 1990, 7.7)
    m5 = Movie("Percy Jackson", "Columbus, Chris", 2010, 5.9)
    m6 = Movie("Grease", "Kleiser, Randal", 1978, 7.2)
    mc = MovieCollection()
    mc.insertMovie(m4)
    mc.insertMovie(m5)
    mc.insertMovie(m6)
    assert mc.getNumberOfMovies() == 3
    expectedoutput = "HOME ALONE directed by CHRIS COLUMBUS (1990), Rating: 7.7\nPERCY JACKSON directed by CHRIS COLUMBUS (2010), Rating: 5.9\nGREASE directed by RANDAL KLEISER (1978), Rating: 7.2\n"
    assert mc.getAllMoviesInCollection() == expectedoutput
    directoroutput = "HOME ALONE directed by CHRIS COLUMBUS (1990), Rating: 7.7\nPERCY JACKSON directed by CHRIS COLUMBUS (2010), Rating: 5.9\n"
    assert mc.getMoviesByDirector("Columbus, Chris") == directoroutput
    assert mc.avgDirectorRating("Columbus, Chris") == 6.80
    mc.removeDirector("Columbus, Chris")
    assert mc.getNumberOfMovies() == 1
    assert mc.recursiveSearchMovie("Grease", mc.head) == True

