import urllib.request
import unittest

def getFiles():
    urllib.request.urlretrieve("http://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD", "./mm.csv")
    urllib.request.urlretrieve("http://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD", "./pb.csv")

class unit(unittest.TestCase):
    def setUp(self):
        return self

if __name__ == "__main__":
    unittest.main()
