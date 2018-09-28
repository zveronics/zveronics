from setuptools import setup, find_packages


setup(
    name='zveronics',
    description='Python server for zveronics game',
    author='Zveronics developers',
    author_email='grihabor@gmail.com',
    url='https://github.com/zveronics/zveronics',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
        'msgpack',
        'pyyaml',
    ],
    setup_requires=[
        'setuptools_scm',
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    use_scm_version=True,
)
