from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='knockoffspy',
      version='0.0.1',
      description='Variable Selection with Knockoffs in Python',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Statistics',
      ],
      url='https://github.com/biona001/knockoffspy',
      keywords='knockoff filter knockoffs variable selection feature selection conditional independence group fdr lasso',
      author='Benjamin Chu',
      author_email='bbchu@stanford.edu',
      license='MIT',
      packages=['knockoffspy',''],
      install_requires=['julia>=0.2', 'jill'],
      include_package_data=True,
      zip_safe=False)