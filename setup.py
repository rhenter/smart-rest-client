import codecs
import os
import re

from setuptools import setup, find_packages, Command
from smart_rest_client.utils import get_version_from_changes

here = os.path.abspath(os.path.dirname(__file__))
version = get_version_from_changes(here)


# Save last Version
def save_version():
    version_path = os.path.join(here, "smart_rest_client/version.py")

    with open(version_path) as version_file_read:
        content_file = version_file_read.read()

    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, content_file, re.M)
    current_version = mo.group(1)

    content_file = content_file.replace(current_version, "{}".format(version))

    with open(version_path, 'w') as version_file_write:
        version_file_write.write(content_file)


save_version()


# Get the long description
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get changelog
with codecs.open(os.path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changelog = f.read()

with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requires = [line for line in f.readlines() if not line.startswith('#')]


class VersionCommand(Command):
    description = 'print library version'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


setup(
    author='Rafael Henter',
    author_email='rafael@henter.com.br',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
    cmdclass={'version': VersionCommand},
    description='Python wrapper to perform requests to Rest APIs using objects to request endpoints and their methods',
    install_requires=install_requires,
    keywords='rest api client python',
    long_description=long_description,
    name='smart-rest-client',
    packages=find_packages(exclude=['docs_src', 'doc', 'tests*']),
    url='https://github.com/rhenter/smart-rest-client',
    version=version,
)
