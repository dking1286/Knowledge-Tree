try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Knowledge Tree',
    'version': '0.1',
    'author': 'Daniel Oliver King',
    'author_email': 'daniel.oliver.king@gmail.com',
    'packages': ['knowledge_tree'],
    'install_requires': ['nose', 'peewee'],
    'scripts': [],
    'description': 'Interactive program that shows how long it will take to pay off a loan'
}

setup(**config)
