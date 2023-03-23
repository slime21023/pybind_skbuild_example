from skbuild import setup  # This line replaces 'from setuptools import setup'
setup(
    name="example",
    version="0.0.1",
    description="a minimal example package",
    packages=['example'],
    python_requires=">=3.8",
)
