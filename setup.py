from setuptools import setup
setup(
    name = 'wordle',
    version = '0.1.0',
    description='You like Wordle? You like CLI? You love Wordle CLI!',
    author='Guy Torbet',
    license='MIT',
    packages = ['wordle'],
    entry_points = {
        'console_scripts': [
            'wordle = wordle.__main__:main'
        ]
    })
