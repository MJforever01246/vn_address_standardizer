import setuptools
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name='vn_address_standardizer',
    version='1.0.0',
    author="MJforever01246",
    author_email="MJforever01246@gmail.com",
    description="A package for parsing Vietnamese address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MJforever01246/vn_address_standardizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'nltk', 'joblib', 'sklearn_crfsuite', 'fuzzywuzzy', 'python-Levenshtein', 'sentence-transformers', 'torch', 'pandas', "numpy" , "sentence-transformers", "transformers", "tqdm" , "flake8", "gradio"
    ],
    include_package_data=True,
    package_data={
        '': ['resource/*',"embedding-model/*"], 
    },
)