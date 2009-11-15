from setuptools import setup, find_packages

version = '0.0.1'
classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Haskell",
        "Topic :: Software Development :: "
        "Libraries :: Haskell Modules"]

setup(
        name='skelhs.basicmodule',
        version=version,
        description=("PasteScript templates for a simple Haskell "
            "module, including HUnit and Quickcheck tests."),
        classifiers=classifiers,
        keywords='paste templates Haskell HUnit QuickCheck',
        author='Bas Bossink',
        author_email='bas.bossink@gmail.com',
        url='http://github.com/basbossink/skelhs',
        license='GPL',
        packages=find_packages(exclude=['ez_setup']),
        namespace_packages=['basicmodule'],
        include_package_data=True,
        install_requires=['setuptools','PasteScript'],
        entry_points="""
        # -*- Entry points -*-
        [paste.paster_create_template]
        skelhs_basic_module = basicmodule.skels.module:Module
        """)

        
