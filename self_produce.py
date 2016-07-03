import os
import sys

"""
I can produce myself!
"""

filename = sys.path[0]+'/'+__file__
with open(filename) as ff:
	content = ff.read()
print content
