from setuptools import setup, find_packages

setup(
    name='openwavelab',
    version='0.1.0',
    author='Arya K J',
    author_email='your_email@example.com',  # replace with your actual email
    description='A beginner-friendly DSP visualization toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aryakj123/openwavelab',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'ipywidgets',
        'sounddevice',
        'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Signal Processing'
    ],
    python_requires='>=3.6',
)
