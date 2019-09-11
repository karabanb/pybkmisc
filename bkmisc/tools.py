
import os


def start_project():
    for folder in ['data', 'doc', 'results', 'scripts', 'tmp']:
        os.mkdir(os.path.join(os.getcwd(), folder))

