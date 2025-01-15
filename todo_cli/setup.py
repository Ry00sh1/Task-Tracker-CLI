# setup.py
from setuptools import setup, find_packages

setup(
    name="todo-cli",
    version="0.1",
    packages=find_packages(),
    install_requires=["tabulate"],
    entry_points={
        "console_scripts": [
            "todo-cli = todo_cli.main:main",
        ],
    },
)
