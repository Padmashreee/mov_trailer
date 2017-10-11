import media
import fresh_tomatoes


avatar = media.Movie("Avatar",
                           "Avatar is written and directed by james cameron.",
                           "https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/07/28/16/avatar.jpg",
                           "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

rio_2 = media.Movie("Rio 2",
                        "rio 2 is a american comedy movie",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnjOGZchXEgjBNbvFsZIRFvynyGOMFXgD4RX7FoV_8J52ZPHPq", 
                        "https://www.youtube.com/watch?v=81ll2B4zl1g")

frozen = media.Movie("Frozen",
                          "Frozen plays on the level of ice and snow but also the frozen relationship, the frozen heart that has to be thawed.",
                          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW4L4jnHfsXNsSTknk-Gvruim-yd3C-lClzy8BjojY_WY7fr8Y",  
                          "https://www.youtube.com/watch?v=TbQm5doF_Uc")


it = media.Movie("It",
                        "A horror movie.",
                        "https://i.pinimg.com/736x/6d/3e/7b/6d3e7b5dd5f5243c1dd2eb9b3d79f34f--stephen-kings-it-it-movie-stephen-king.jpg", 
                        "https://www.youtube.com/watch?v=FnCdOQsX5kc")

tangled = media.Movie("Tangled",
                        "A story of Rapunzel, an innocent, young girl, is locked up by her overly protective mother.",
                        "http://stuffpoint.com/soundtracks/image/421465-soundtracks-tangled-soundtrack-cover.jpg", 
                        "https://www.youtube.com/watch?v=ip_0CFKTO9E")

movies = [avatar, rio_2, frozen, it, tangled]

fresh_tomatoes.open_movies_page(movies)
