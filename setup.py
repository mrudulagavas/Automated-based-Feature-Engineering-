from setuptools import setup

setup(
    description = ("Automated feature engineering "),
    name = "bigfeat",
    version = "0.1",
    keywords = ["feature engineering", "machine learning", "automl", "feature extraction", "feature selection"],
    url = "https://github.com/mrudulagavas/Automated-based-Feature-Engineering-.git",
    packages=['bigfeat'],
    long_description=("Automated feature engineering "),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'lightgbm',
    ],
)
