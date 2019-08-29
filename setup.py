import codecs
import os
from setuptools import setup, find_packages


extras_require = {
    "bam": ["pysam"],
    "miniwdl": ["miniwdl"],
    "progress": ["tqdm"]
}
extras_require["all"] = [
    lib
    for lib_array in extras_require.values()
    for lib in lib_array
]


setup(
    name="pytest-wdl",
    author="The pytest-wdl development team",
    url="https://github.com/EliLillyCo/pytest-wdl",
    project_urls={
        "Documentation": "https://pytest-wdl.readthedocs.io/en/stable/",
        "Source": "https://github.com/EliLillyCo/pytest-wdl",
        "Tracker": "https://github.com/EliLillyCo/pytest-wdl/issues"
    },
    description="Pytest plugin for testing WDL workflows.",
    long_description_content_type="text/markdown",
    long_description=codecs.open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "README.md"
        ),
        "rb",
        "utf-8"
    ).read(),
    license=codecs.open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "LICENSE"
        ),
        "rb",
        "utf-8"
    ).read(),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    entry_points={
        "pytest11": [
            "pytest_wdl = pytest_wdl"
        ],
        "pytest_wdl.data_types": [
            "bam = pytest_wdl.data_types.bam:BamDataFile",
            "vcf = pytest_wdl.data_types.vcf:VcfDataFile",
        ],
        "pytest_wdl.executors": [
            "cromwell = pytest_wdl.executors.cromwell:CromwellExecutor",
            "miniwdl = pytest_wdl.executors.miniwdl:MiniwdlExecutor"
        ]
    },
    py_modules=["pytest_wdl"],
    packages=find_packages(),
    install_requires=[
        "pytest",
        "delegator.py"
    ],
    extras_require=extras_require,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
