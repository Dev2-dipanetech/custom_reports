from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_reports/__init__.py
from custom_reports import __version__ as version

setup(
	name="custom_reports",
	version=version,
	description="creating personalised reports",
	author="DT team",
	author_email="dev2@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
