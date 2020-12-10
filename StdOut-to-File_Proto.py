#   Testing HTTP GET's from a response, trying to understand more
#   to be able to pump the response codes from stdout into a file.
#   Prototype for my PlaylistPopulator program - see here: 
#   https://github.com/ramrow17/PythonPractice//blob/master/YouTubePlaylist_Populator.py
#
#   Also using example code from DigitalOcean:
#       https://www.digitalocean.com/community/tutorials/getting-started-with-python-requests-get-requests
#
#   Example code for re-directing stdout into a file:
#       https://www.blog.pythonlibrary.org/2016/06/16/python-101-redirecting-stdout/
#
#  

import requests
import sys 

orgn = sys.stdout

res = requests.get('https://www.google.com/')


if res:
    print('Response OK')
else:
    print('Response Failed')

sys.stdout = open('TestFile.txt', 'w')

print(res.headers)
sys.stdout = orgn
print(res.headers)
