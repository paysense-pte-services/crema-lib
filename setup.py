from setuptools import setup, find_packages

setup(
    name='crema',
    version='2.26',
    description='Kafka Library',
    url='https://github.com/paysense/crema',
    author='Rohit Laddha',
    author_email='rohit.laddha@paysense.in',
    packages=['crema'],
    zip_safe=False,
    install_requires=['kafka-python==2.0.0', 'uhashring==1.1']
)
