from setuptools import setup

setup(
    name='armstrong.base',
    version='0.1.1',
    description='Base functionality that needs to be shared widely',
    author='Texas Tribune',
    author_email='tech@texastribune.org',
    url='http://github.com/texastribune/armstrong.base/',
    packages=[
        'armstrong',
        'armstrong.base',
    ],
    namespace_packages=[
        "armstrong",
    ],
    install_requires=[
        'setuptools',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
