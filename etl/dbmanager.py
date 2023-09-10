""" A file for managing the upload of dataframes into postgres database """

import psycopg2


class DBmanager:
    """ a class for uploading dataframes into postgres """
    
    def __init__(self):
