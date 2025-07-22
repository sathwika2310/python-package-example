from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/sathwika2310/python-package-example',
    author='Sai Sathwika Palle',
    author_email='sathwika2310@gmail.com'
)

