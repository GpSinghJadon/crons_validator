from setuptools import setup
setup(
    name = 'crontab-check',
    version = '1.0',
    packages = ['crontab-check'],
    entry_points = {
        'console_scripts': [
            'crontab-check = crontab-check.__main__:main'
        ]
    })