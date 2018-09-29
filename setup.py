from setuptools import setup, find_packages

tests_require = [
    'coverage',
    'pytest',
    'pylint',
    'isort',
    'flake8',
    'coveralls',
]
extras_require = {
    'test': tests_require,
}

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
    tests_require=tests_require,
    extras_require=extras_require,
    use_scm_version=True,
    include_package_data=True,
    package_data={
        'zveronics': ['etc/*.yaml'],
    },
)
