from datetime import date
# from urllib3 import request
from urllib import request

from multiprocessing import Pool

def days_between(start,stop):
  today = date(*start)
  stop = date(*stop)
  while today < stop:
    datestr = today.strftime("%m-%d-%Y")
    yield "http://jtwolohan.com/arch-rival-blog/"+datestr
    today = date.fromordinal(today.toordinal()+1)

def get_url(path):
  return request.urlopen(path).read()


with Pool() as P:
  blog_posts = P.map(get_url,days_between((2000,1,1),(2011,1,1)))



##playground

# blog_posts = map(get_url,days_between((2000,1,1),(2020,1,1)))
# print(list(blog_posts))


#print wrong order because that's processing time
#return right order

def print_and_return(x):
  print(x); return x
with Pool() as P:
  result = P.map(print_and_return, range(50))

print(result)