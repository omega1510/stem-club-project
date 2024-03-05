from distutils.core import setup
import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/requirements.txt"
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()
setup(
    name="Dave's: The Game",
    version="0.1.0",
    author="Hayaan Imam Rizvi",
    author_email="hayaanrizvi@gmail.com",
    description="A text-adventure game",
    long_description="A text-adventure game where you play as Br. Waqas, a PE teacher who is trying to get Dave's hot chicken for the boys.",
    packages=["DavesTheGame",],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=install_requires,
)
