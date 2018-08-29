from setuptools import setup

setup(
    name='name_anagramer',
    version='1.0',
    author='Tom Watson',
    description='Make pseudonym that\'s an anagram!',
    packages=['name_anagramer'],
    install_requires=[
        'names>=0.3.0',
        'progressbar2>=3.30.2'
    ],
    entry_points = {
        'console_scripts': [
            'name_anagramer=name_anagramer:cli'
        ]
    }
)
