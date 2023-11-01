import setuptools


with open("requirements.txt", "r") as f:
    reqs = f.read().split("\n")

with open("requirements_test.txt", "r") as f:
    test_reqs = f.read().split("\n")

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    name='dcr_consistency',
    version='0.0.1',    
    description='A package to detect and mitigate inconsistency',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/test',
    author='Wendi Cui, Jiaxin Zhang',
    author_email='wendi_cui@intuit.com',
    license='Apache License 2.0',
    packages=['dcr'],
    install_requires=reqs,
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
