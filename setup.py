from setuptools import setup, find_packages
import subprocess

name = 'kehia'


def get_version():
    with open('VERSION') as f:
        version = f.read().strip()

    # Append the Git commit id if this is a development version.
    if version.endswith('+'):
        tag = 'v' + version[:-1]
        try:
            desc = subprocess.check_output([
                'git', 'describe', '--match', tag,
            ])[:-1].decode()
        except Exception:
            version += 'unknown'
        else:
            assert str(desc).startswith(tag)
            import re
            match = re.match(r'v([^-]*)-([0-9]+)-(.*)$', desc)
            if match is None:       # paranoia
                version += 'unknown'
            else:
                ver, rev, local = match.groups()
                version = '%s.post%s+%s' % (ver, rev, local.replace('-', '.'))
                assert '-' not in version

    return version

version = get_version()

setup(
    name=name,
    version=version,
    packages=find_packages(),
    description="KEHIA Website",
    long_description=open('README.rst').read(),
    url="http://pip.slade360.co.ke/docs/{}/".format(name),
    author="SIL",
    author_email="developers@savannahinformatics.com",
    license="Proprietary",
    classifiers=[
        'Development Status :: 1 - Alpha',
    ],
    install_requires=[
        'wagtail',
        'gunicorn',
        'psycopg2',
        'python-memcached',
        'django-debug-toolbar',
    ],
    scripts=[
        'bin/kehia_manage',
        'bin/run',
    ],
    include_package_data=True
)
