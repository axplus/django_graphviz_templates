import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django_graphviz_templates',
    version="0.0.1",
    author="yijie zeng",
    author_email="axplus@163.com",
    description="a quick render for django from graphviz formatted file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/axplus/django_graphviz_templates",
    packages=['django_graphviz_templates'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6',
    install_requires=[
        'Django>=1.6',
        'graphviz>=0.13',
    ]
)