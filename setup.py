from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="i3-clipboard-history",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Clipboard history manager for i3wm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/i3-clipboard-history",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["clipman"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: X11 Applications",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "clipman=clipman:main",
        ],
    },
    install_requires=[
        # No external Python dependencies required
        # All dependencies are system packages (xclip, rofi)
    ],
)
