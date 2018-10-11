from setuptools import setup
setup(
    name='crontab_check',
    version = '1.0',
    packages=['crontab_check'],
    entry_points = {
        'console_scripts': [
            'crontab-check = crontab_check.process:run'
        ]
    })