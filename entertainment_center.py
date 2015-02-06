import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A boy and his toys", "http://upload.wikimedia.org/wikipedia/en/thumb/6/69/Toy_Story_3_poster.jpg/220px-Toy_Story_3_poster.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar", "Marine on an alian planet", "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ");
fresh_tomatoes.open_movies_page([toy_story, avatar])


