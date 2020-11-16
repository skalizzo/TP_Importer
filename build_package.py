import os


def build_package():
    """
    builds the distributable package and the wheel and uploads the package to PyPl using the
    account data from .pypirc
    :return:
    """
    print(os.system('python setup.py sdist'))  # build python package
    print(os.system('python setup.py bdist_wheel --universal'))  # build python wheel
    print(os.system('twine upload dist/* --config-file ".pypirc"'))  # upload to PyPl


if __name__ == '__main__':
    build_package()
