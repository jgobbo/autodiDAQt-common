from pathlib import Path
from setuptools import setup, find_packages

ROOT = Path(__file__).parent

VERSION = "2.0.0"
PACKAGE_NAME = "autodidaqt-common"
AUTHOR = "Conrad Stansbury, Jacob Gobbo"
AUTHOR_EMAIL = "jgobbo@berkeley.edu"
URL = ""

LICENSE = "MIT License"
DESCRIPTION = "Common code for autodidaqt core and receiver"
LONG_DESCRIPTION = (ROOT / "README.md").read_text()
LONG_DESC_TYPE = "markdown"

with open(ROOT / "requirements.txt") as f:
    INSTALL_REQUIRES = f.read().splitlines()

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESC_TYPE,
        author=AUTHOR,
        license=LICENSE,
        author_email=AUTHOR_EMAIL,
        url=URL,
        install_requires=INSTALL_REQUIRES,
        packages=find_packages(),
    )
