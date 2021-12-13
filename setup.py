import os.path

from skbuild import setup

requires = []
requires_dev = requires + [
    "black>=20.",
    "bump2version>=1.0.0",
    "flake8>=3.7.8",
    "flake8-black>=0.2.1",
    "mock",
    "pytest>=4.3.0",
    "pytest-cov>=2.6.1",
    "pytest-rerunfailures>=10.1",
    "recommonmark",
    "Sphinx>=1.8.4",
    "sphinx-markdown-builder>=0.5.2",
    "sphinx-rtd-theme",
]

cmake_args = ["-DBUILD_TESTS:BOOL=OFF"]

vcpkg_toolchain_file = os.path.abspath(
    os.path.join("vcpkg\\scripts\\buildsystems\\vcpkg.cmake")
)

if os.path.exists(vcpkg_toolchain_file):
    cmake_args.append("-DCMAKE_TOOLCHAIN_FILE={}".format(vcpkg_toolchain_file))

setup(
    name="libta_lib",
    version="0.4.0.rc2",
    description="TA-lib C++ builder",
    long_description="TA-lib C++ builder from source",
    long_description_content_type="text/markdown",
    url="https://github.com/timkpaine/ta-lib",
    author="Tim Paine",
    author_email="t.paine154@gmail.com",
    license="BSD 3-clause",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
    ],
    zip_safe=False,
    packages=["libta_lib"],
    install_requires=requires,
    extras_require={
        "dev": requires_dev,
    },
    cmake_args=cmake_args,
)
