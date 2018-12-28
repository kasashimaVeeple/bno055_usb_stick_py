import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bno055_usb_stick_py",
    version="0.1.0",
    author="Dr. Konstantin Selyunin",
    author_email="selyunin.k.v@gmail.com",
    description="BNO055 USB Stick Linux Python Driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/selyunin/bno055_usb_stick_py",
    packages=setuptools.find_packages(),
    requires=["pyudev", "pyserial", "dataclasses"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
)