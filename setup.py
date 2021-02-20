from setuptools import setup

setup(
    name="c3-toolset",
    version="1.2.1",
    description="Toolset for control, calibration and characterization of physical systems",
    url="http://www.q-optimize.org",
    author="q-optimize",
    author_email="c3@q-optimize.org",
    include_package_data=True,
    packages=[
        "c3",
        "c3/generator",
        "c3/libraries",
        "c3/optimizers",
        "c3/qiskit",
        "c3/schemas",
        "c3/signal",
        "c3/system",
        "c3/utils",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "adaptive==0.11.1",
        "cma==3.0.3",
        "hjson==3.0.2",
        "rich==9.2.0",
        "numpy==1.19.5",
        "scipy==1.5.2",
        "tensorflow==2.4.0",
        "tensorflow-estimator==2.4.0",
        "tensorflow-probability==0.12.1",
    ],
    python_requires="~=3.6",    
)
