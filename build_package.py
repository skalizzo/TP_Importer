import os


def build_package():
    """
    builds the distributable package and the wheel and uploads the package to PyPl using the
    account data from .pypirc
    :return:
    """
    DISTRIBUTION_DIR = "./dist/"
    # removing old packages
    for f in os.listdir(DISTRIBUTION_DIR):
        os.remove(os.path.join(DISTRIBUTION_DIR, f))
    print(os.system('python setup.py sdist'))  # build python package
    print(os.system('python setup.py bdist_wheel --universal'))  # build python wheel
    print(os.system('twine upload dist/* --config-file ".pypirc"'))  # upload to PyPl


if __name__ == '__main__':
    build_package()
