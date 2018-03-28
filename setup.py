try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='modapsclient',
    version='0.1',
    description='A client for the NASA MODAPS web service',
    author='Chris Waigl',
    author_email='chris.waigl@gmail.com',
    url='https://github.com/chryss/modapsclient',
    license='MIT',
    packages=['modapsclient'],
    install_requires=[
        'future',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
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
