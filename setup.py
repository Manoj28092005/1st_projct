from setuptools import setup, find_packages 
from typing import Listist
def get_requirements(file_path):
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path, 'r') as file:
        req=[]
        with open(file_path)as file_obj:
            reqq= file_obj.readlines()
            reqq=[req.repalce('\n',"")for req in reqq ]
            HYPHEN_E_DOT = '-e .'
            if HYPHEN_E_DOT in reqq:
                reqq.remove(HYPHEN_E_DOT)
        return reqq
setup(
    name='mlprojct',
    version='0.1.0',
    description='An example Python package',
    author='manoj',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),)

