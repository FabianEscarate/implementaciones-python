
from setuptools import setup, find_packages
from digimondata.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='digimondata',
    version=VERSION,
    description='obtencion, mantencion, ideas, etc. con informacion de digimon',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Fabian Escarate',
    author_email='john.doe@example.com',
    url='https://github.com/FabianEscarate',
    license='GNU',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'digimondata': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        digimondata = digimondata.main:main
    """,
)
