from setuptools import setup, find_packages
 
setup(
    name='todo',
    version='0.1.0',
    description='A simple command-line tool to manage daily tasks',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=todo:main'
        ]
    },
    install_requires=[
        'argparse>=1.4.0',
        'datetime>=4.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
