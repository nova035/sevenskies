import os
import sys
import json
import pkg_resources
import click
import env_variables

from subprocess import call
from sarge import run

BACKEND_VERSION = pkg_resources.require("kehia")[0].version
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SSH_USER = os.environ.get('USER', '')
PRIVATE_KEY = os.environ.get('ANSIBLE_SSH_PRIVATE_KEY_FILE', '~/.ssh/google_compute_engine')  # noqa


def call_ansible(server, playbook, extra_vars):
    call([
        "ansible-playbook", "-i{},".format(server.strip()),
        "{}".format(playbook),
        "--extra-vars={}".format(extra_vars),
        "--ssh-extra-args=-o ServerAliveInterval=30",
    ])


def call_ansible_tag(server, playbook, extra_vars, tag):
    call([
        "ansible-playbook", "-i{},".format(server.strip()),
        "{}".format(playbook),
        "--extra-vars={}".format(extra_vars),
        "--ssh-extra-args=-o ServerAliveInterval=30",
        "--tags={}".format(tag)
    ])


def create_archive():
    """
    Create a tarball of the project
    """
    p = run("run archive")
    if p.returncode:
        sys.exit(1)


@click.group()
def deploy():
    """Deploys the KEHIA application"""
    pass


@deploy.command()
@click.option('--domain', default="staging.kehia.org",
              prompt="Server domain",
              help="The domain name of the server you're deploying to.")
@click.option('--force',
              help="Ignore the lock file that prevents parallel deploys",
              is_flag=True,
              prompt="Forcefully override any existing deploy? [N]",
              default=False)
@click.option('--setup-new-certs',
              help="Copy SSL certificates to the server's tls directory",
              is_flag=True,
              prompt="Setup new SSL certificates? [N]",
              default=False)
@click.option('--setup-new-db',
              help="Drop the database and rebuild the site; irreversible.",
              is_flag=True,
              prompt="To deploy to a new server or rebuild from default data, respond [y] ( default )",  # noqa
              default=True)
@click.option('--ssl-on', help="Turn on ssl.",
              is_flag=True,
              prompt="This only changes nginx SSL settings; certificates needed [Y]",  # noqa
              default=True)
@click.option('--version', prompt="Version",
              help="The version that you'd like to deploy.",
              default=BACKEND_VERSION)
def backend(domain, version, force, setup_new_db, ssl_on, setup_new_certs):
    ignore_lock = 'true' if force else 'false'
    setup_ssl_certs = 'true' if setup_new_certs else 'false'
    deploy_https = 'true' if ssl_on else 'false'
    setup_new_database = 'true' if setup_new_db else 'false'
    extra_vars = {
        'version': version,
        'ansible_ssh_user': SSH_USER,
        'ansible_ssh_private_key_file': PRIVATE_KEY,
        'pg_login_user': env_variables.login_user,
        'pg_login_password': env_variables.login_password,
        'db_user': env_variables.db_user,
        'db_pass': env_variables.db_pass,
        'db_name': env_variables.db_name,
        'setup_new_db': setup_new_database,
        'ansible_host': domain,
        'api_server_domain': domain,
        'server_domain': domain,
        'secret_key': env_variables.secret_key,
        'libcloud_user': env_variables.libcloud_user,
        'libcloud_key': env_variables.libcloud_key,
        'sudo_magick_needed': 'true',
        'force_ignore_lock': ignore_lock,
        'setup_new_ssl_certs': setup_ssl_certs,
        'ssl_on': deploy_https,
        'aws_key_id': env_variables.aws_key_id,
        'aws_secret': env_variables.aws_secret,
        'front_end_url': env_variables.front_end_url,
        'libcloud_storage': env_variables.libcloud_storage,
        'libcloud_provider': env_variables.libcloud_provider,
        'libcloud_type': env_variables.libcloud_type,
        'libcloud_bucket': env_variables.libcloud_bucket
    }
    click.echo(extra_vars)
    click.echo("Deploying version {} to domain {}!".format(version, domain))
    call_ansible(domain, 'kehia.yml', json.dumps(extra_vars))


if __name__ == '__main__':
    create_archive()
    deploy()
