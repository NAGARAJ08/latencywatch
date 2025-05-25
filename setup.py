from setuptools import setup, find_packages

setup(
    name='latencywatch',
    version='0.1.0',
    description='A lightweight Python profiler using sys.setprofile for latency tracing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nagaraj K   ',
    author_email='kbnagaraj18@gmail.com',
    url='https://github.com/NAGARAJ08/latencywatch',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
