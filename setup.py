import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Deep_Learning_Classifer_Project"
AUTHOR_USER_NAME = "shrey-0407"
SRC_REPO = "Deep_Classifer"
AUTHOR_EMAIL = "shreyash966977@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/shrey-0407/Deep_Learning_Classifer_Project",
    project_urls={
        "Bug Tracker": f"https://github.com/shrey-0407/Deep_Learning_Classifer_Project/issues",
    },
    package_dir={"": "src"},
)
    