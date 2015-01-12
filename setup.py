from setuptools import setup, find_packages


setup(
    name='readthedocs',
    version="1.0",
    description='A documentation hosting website',
    #long_description=readme,
    author='Eric Holscher, Charles Leifer, Bobby Grace',
    author_email='eric@ericholscher.com',
    url='http://readthedocs.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    ],
)
