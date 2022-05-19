class Movie
{
    private String title;
    private int year;
    private double rating;

    public Movie(String t, int y, double r)
    {
        title = t;
        year = y;
        rating = r;
    }

    public Movie(String t)
    {
        title = t;
        year = 0;
        rating = 0.0;
    }
    { r1 = random.randint(1, 5)
	print("Random rating between 1 and 5 is % s" % (r1))}
	
}

Movie m = new Movie("Lion King", "1994", 8.0);
Movie m = new Movie("the incredibles", "2004", 8.0);
Movie m = new Movie("charlie and the choclate factory", "2005", 8.0);