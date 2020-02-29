from setuptools import setup

# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='exemplo-crud',
      version="0.0.1",
      description="exemplo de uma CRUD API ",
      url="",
      author="Yuri Mussi",
      author_email="ymussi@gmail.com",
      license="BSD",
      keywords="Yuri Mussi",
      packages=["crud"],
      zip_safe=False
      ),
