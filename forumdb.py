# "Database code" for the DB Forum.

import datetime
import psycopg2

dbname = 'forum'



POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=dbname)
  c = db.cursor()
  c.execute('SELECT content FROM {} ORDER BY time'.format(dbname))

  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))


