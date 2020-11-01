from skbuild import setup

setup(
    name="libta_lib",
    version="0.4.0.rc1",
    description='TA-lib C++ builder',
    long_description="TA-lib C++ builder from source",
    long_description_content_type='text/markdown',
    url='https://github.com/timkpaine/ta-lib',
    author='Tim Paine',
    author_email='t.paine154@gmail.com',
    license='BSD 3-clause',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    packages=["libta_lib"],
    cmake_args=['-DBUILD_TESTS:BOOL=OFF']
)


