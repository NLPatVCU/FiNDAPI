from setuptools import setup

setup(
    name='PaperScraper',
    version='1.0',
    install_requires=[
        'Flask==0.12.2',
        'flask-restplus==0.10.1',
    ],
    license='MIT',
    author='Brandon Watts',
    author_email='wattsbc2@mymail.vcu.edu',
    description='Application for the efficient extraction of scientific articles.'
)