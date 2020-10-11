from setuptools import setup

setup(name="ConnectSQl",
      packages=['ConnectSQl'],
      download_url="https://github.com/kailash1011/ConnectSQl/releases/tag/1.0",
      version='1.0',
      description="Connect Access & retrieve MYSQl databases.",
      url="https://github.com/kailash1011/ConnectSQl",
      author="Kailash Sharma",
      author_email="kailashps.1011@gmail.com",
      license="MIT",
      classifiers=['Programming Language :: Python :: 3.6'],
      REQUIREMENTS=['mysql-connector-python~=8.0.21']

      )
