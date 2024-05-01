from setuptools import setup, find_packages

setup(
    name='SystemPromptConverter',
    version='0.1',
    description='A tool for converting system prompts to different formats.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here. For example:
        # 'pandas',
        # 'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'prompt=main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
