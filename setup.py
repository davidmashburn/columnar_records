from distutils.core import setup

# Read the version number
with open("columnar_records/_version.py") as f:
    exec(f.read())

setup(
    name='columnar_records',
    version=__version__, # use the same version that's in _version.py
    author='David N. Mashburn',
    author_email='david.n.mashburn@gmail.com',
    packages=['columnar_records'],
    scripts=[],
    url='http://pypi.python.org/pypi/columnar_records/',
    license='LICENSE.txt',
    description='<ADD DESCRIPTION>',
    long_description=open('README.txt').read(),
    install_requires=[
                      
                     ],
)