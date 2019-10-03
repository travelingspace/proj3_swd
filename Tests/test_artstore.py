from peewee import *
import unittest
from unittest import TestCase
from SQL_db import config as db
import Model.model as model

class TestArtStoreDB(TestCase):

    test_db = 'test_artstore.db'

    def setUp(self):

        with sqlite3.connect(self.test_db) as conn:
            conn.execute('drop table if exists artist')
        conn.close()

        with sqlite3.connect(self.test_db) as conn:
            conn.execute('create table artist (name text unique not null, email text not null)')
        conn.close()

        self.db = db

    def test_add_new_artist(self):
        a1 = model.Artist('Van Gogh','oneEar@pernod.com')
        a1.save()