from setuptools import setup

setup(
    name='CDJobs',
    version='0.1',
    description='continues deployment kubernetes job api',
    author='Yuval Bar',
    author_email='yuvalb098@gmail.com',
    packages=['cdjobs'],
    package_dir={"": "src"},
    install_requires=[
        'fastapi',
        'uvicorn[standard]',
        'requests',
        'kubernetes'],
)
