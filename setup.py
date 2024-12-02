import os
import setuptools

version_file = 'pytoolsJS/_version.py'
exec(compile(open(version_file, 'rb').read(), version_file, 'exec'), globals(), locals())

with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='pytoolsJS',
    version=__version__,
    author='Jeremy Schroeter',
    author_email='jeremyschroeter@gmail.com',
    description='misc personal Python tools',
    long_description=long_description,
    url='https://github.com/jeremyschroeter/pytoolsJS',
    pavkage=['pytoolsJS'],
    package_dir={'pytoolsJS' : 'pytoolsJS'},
    install_requires=[
        'allensdk',
        'numpy',
        'scikit-image',
        'setuptools',
        'scikit-learn',
        'matplotlib'
    ],
    include_package_data=True
)