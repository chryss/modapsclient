from setuptools import setup

setup(
    name='modapsclient',
    version='0.1',
    description='A client for the NASA MODAPS web service',
    author='Chris Waigl',
    author_email='chris.waigl@gmail.com',
    url='https://github.com/chryss/modapsclient',
    license='MIT',
    packages=['modapsclient'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
