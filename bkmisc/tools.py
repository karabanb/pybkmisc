
import os


def start_project():
    for folder in ['data', 'doc', 'results', 'scripts', 'tmp']:
        os.mkdir('./' + folder)
