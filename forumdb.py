# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach
dbname = 'forum'



POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=dbname)
  c = db.cursor()
  c.execute('SELECT content, time FROM posts ORDER BY time')

  data = c.fetchall()
  db.close()
  return data

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))
  dt = datetime.datetime.now()
  d_truncated = datetime.date(dt.year, dt.month, dt.day)
  db = psycopg2.connect(database=dbname)
  content = bleach.clean(content)
  c = db.cursor()
  c.execute("INSERT INTO posts (content, time) VALUES (%s, %s)", (content, dt,))
  db.commit()
  db.close()


