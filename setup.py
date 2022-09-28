from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme_text = readme_file.read()


setup_args = dict(
    name='tekleo-common-utils',
    version='0.0.2.1',
    description="",
    keywords=[],
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License',
    packages=find_packages(),
    author="Leo Ertuna",
    author_email="leo.ertuna@gmail.com",
    url="https://github.com/jpleorx/tekleo-common-utils",
    download_url='https://pypi.org/project/tekleo-common-utils/'
)


install_requires = [
    'pytz',
    'tzlocal',
    'injectable',
    'requests',
    'user-agent',
    'Faker',
    'namesgenerator',
    'Pillow',
    'numpy',
    'opencv-python',
    'pillow-heif',
    'tekleo-common-message-protocol'
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
