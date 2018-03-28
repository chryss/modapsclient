from setuptools import setup, find_packages

version = '0.1.1'

with open('README.rst', 'rU') as f:
    long_description = f.read()

setup(
    name='modapsclient',
    version=version,
    description='A client for the NASA MODAPS web service',
    long_description=long_description,
    author='Chris Waigl',
    author_email='chris.waigl@gmail.com',
    url='https://github.com/chryss/modapsclient',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'future',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
