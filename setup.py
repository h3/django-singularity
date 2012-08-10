"""
django-singularity

"""

from setuptools import setup, find_packages

setup(
    name = "django-singularity",
    version = "0.0.1",
    url = "https://github.com/h3/django-singularity",
    license = "BSD",
    description = "Web application framework that mixes Twitter Bootstrap & AngularJS",
    author = 'Maxime Haineault',
    packages = find_packages(),
    package_dir = {'': '.'},
    install_requires = [
        # https://github.com/dyve/django-bootstrap-toolkit
        # https://github.com/addyosmani/jquery-ui-bootstrap
        # https://raw.github.com/michaelhelmick/django-bootstrap-admin/
    ],
)
