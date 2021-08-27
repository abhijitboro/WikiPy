#!/usr/bin/python3
###################
import cgi, cgitb
# import imdb
import wikipedia

form = cgi.FieldStorage()

search = form.getvalue('search')

# moviesDB = imdb.IMDb()
# movies = moviesDB.search_movie(''+search)

# id = movies[0].getID()
# movie = moviesDB.get_movie(id)
# title = movie['title']
# rating = movie['rating']
# year = movie['year']

result = wikipedia.summary(""+search)

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>biography</title>")
print("</head>")
print("<body>")
print("<center>")
print("<div style='width: 100%; height: 100%; color: grey; font-family: arial black; font-size: 20px; background-color: whitesmoke;'>")
print("<h3>you searching.. %s</h3>" % (search))
# print(f'<h3>title: {title}</h3></br>')
# print(f'<h3>rating: {rating}</h3></br>')
# print(f'<h3>year: {year}</h3></br>')
print(result)
print("</div>")
print("</center>")
print("</body>")
print("</html>")