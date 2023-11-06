import setuptools


with open("requirements.txt", "r") as f:
    reqs = f.read().split("\n")

with open("requirements_test.txt", "r") as f:
    test_reqs = f.read().split("\n")

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    name='sac3',
    version='0.0.1',    
    description='A package to detect hallucination',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/test',
    author='Jiaxin Zhang',
    author_email='jiaxin_zhang@intuit.com',
    license='Apache License 2.0',
    packages=['sac3'],
    install_requires=reqs,
    python_requires=">=3.8",
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