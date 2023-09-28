import datetime

import requests
import gspread
from oauth2client.client import GoogleCredentials


class Person:
    def __init__(self, name, pic_example, long_shift):
        self.name = name
        self.pic_example = pic_example
        self.long_shift = long_shift
        self.shifts = []

