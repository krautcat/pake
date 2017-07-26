from distutils.core import setup

setup(
    name='Pake',
    version='0.0.0.dev1',
    packages=['pake'],
    url='',
    license='MIT',
    author='Georgiy Odisharia',
    author_email='math.kraut.cat@gmail.com',
    description='',
    entry_points={
        'console_scripts': [
            "pake = pake:main",
        ],
    }
)
