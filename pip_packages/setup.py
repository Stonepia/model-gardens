## Modified from https://github.com/tensorflow/models/blob/master/official/pip_package/setup.py

"""Sets up TensorFlow Official Models."""
import datetime
import os
import sys

from setuptools import find_packages
from setuptools import setup

version = '2.5.0'

project_name = 'tf-models-official'

long_description = """The TensorFlow official models are a collection of
models that use TensorFlow's high-level APIs.
They are intended to be well-maintained, tested, and kept up to date with the
latest TensorFlow API. They should also be reasonably optimized for fast
performance while still being easy to read."""

if '--project_name' in sys.argv:
  project_name_idx = sys.argv.index('--project_name')
  project_name = sys.argv[project_name_idx + 1]
  sys.argv.remove('--project_name')
  sys.argv.pop(project_name_idx)


def _get_requirements():
  """Parses requirements.txt file."""
  install_requires_tmp = []
  dependency_links_tmp = []
  with open(
      os.path.join(os.path.dirname(__file__), '../requirements.txt'), 'r') as f:
    for line in f:
      package_name = line.strip()
      # Skip empty line or comments starting with "#".
      if not package_name or package_name[0] == '#':
        continue
      if package_name.startswith('-e '):
        dependency_links_tmp.append(package_name[3:].strip())
      else:
        install_requires_tmp.append(package_name)
  return install_requires_tmp, dependency_links_tmp

install_requires, dependency_links = _get_requirements()

if project_name == 'tf-models-nightly':
  version += '.dev' + datetime.datetime.now().strftime('%Y%m%d')
  install_requires.append('tf-nightly')
  install_requires.append('tensorflow-text-nightly')
else:
  install_requires.append('tensorflow>=2.4.0')
  install_requires.append('tensorflow-text>=2.4.0')

print('install_requires: ', install_requires)
print('dependency_links: ', dependency_links)

setup(
    name=project_name,
    version=version,
    description='Model Implementation gardens',
    long_description=long_description,
    author='Stonepia',
    author_email='no-reply@google.com',
    url='https://github.com/Stonepia/model-gardens',
    license='Apache 2.0',
    packages=find_packages(exclude=[
        'research*',
        'official.pip_package*',
        'official.benchmark*',
        'official.colab*',
    ]),
    exclude_package_data={
        '': ['*_test.py',],
    },
    install_requires=install_requires,
    dependency_links=dependency_links,
    python_requires='>=3.6',
)
