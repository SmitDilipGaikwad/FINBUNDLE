from setuptools import setup, find_packages

setup(
    name='FINBUNDLE',
    version='0.1.0',  # Update the version number with each release
    author='Your Name',
    author_email='your.email@example.com',
    description='A collection of financial tools',
    long_description='''Add a detailed description of your package here.
    You can use the content from your README.md file for this section.''',
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/FINBUNDLE',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your package here
        'numpy',  # Example: 'numpy>=1.18.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Choose appropriate development status
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
