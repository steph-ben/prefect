#!/usr/bin/env python


import click

import prefect
from prefect.utilities import backend as backend_util

from .agent import agent as _agent
from .auth import auth as _auth
from .create import create as _create
from .delete import delete as _delete
from .describe import describe as _describe
from .execute import execute as _execute
from .get import get as _get
from .run import run as _run
from .server import server as _server
from .heartbeat import heartbeat as _heartbeat
from .register import register as _register
from ..utilities.configuration import set_permanent_user_config

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    The Prefect CLI for creating, managing, and inspecting your flows.

    \b
    Note: a Prefect Cloud API token is required for all Cloud related commands. If a token
    is not set then run `prefect auth login` to set it.

    \b
    Query Commands:
        get         List high-level object information
        describe    Retrieve detailed object descriptions

    \b
    Action Commands:
        agent       Manage agents
        create      Create objects
        delete      Delete objects
        execute     Execute a flow's environment
        run         Run a flow
        register    Register flows with an API
        heartbeat   Send heartbeats for a run

    \b
    Setup Commands:
        auth        Handle Prefect Cloud authorization
        backend     Switch between `server` and `cloud` backends
        server      Interact with the Prefect Server

    \b
    Miscellaneous Commands:
        version     Print the current Prefect version
        config      Output Prefect config
        diagnostics Output Prefect diagnostic information
    """
    pass


cli.add_command(_agent)
cli.add_command(_auth)
cli.add_command(_create)
cli.add_command(_delete)
cli.add_command(_describe)
cli.add_command(_execute)
cli.add_command(_get)
cli.add_command(_run)
cli.add_command(_server)
cli.add_command(_heartbeat)
cli.add_command(_register)


# Miscellaneous Commands


@cli.command(hidden=True)
def version():
    """
    Get the current Prefect version
    """
    click.echo(prefect.__version__)


@cli.command(hidden=True)
def config():
    """
    Output Prefect config
    """
    click.echo(prefect.config.to_json())


@cli.command(hidden=True)
@click.option(
    "--include-secret-names",
    help="Output Prefect diagnostic information",
    hidden=True,
    is_flag=True,
)
def diagnostics(include_secret_names):
    """
    Output Prefect diagnostic information

    \b
    Options:
        --include-secret-names    Enable output of potential Secret names
    """
    click.echo(
        prefect.utilities.diagnostics.diagnostic_info(
            include_secret_names=bool(include_secret_names)
        )
    )


@cli.command(hidden=True)
@click.argument("api")
def backend(api):
    """
    \b
    Switch Prefect API backend :
        - `cloud` for using prefect cloud
        - `server` for using a localhost server
        - any other string for specifying a custom server host, eg. http://my-prefect-server.com
            (~/.prefect/config.toml will be updated)

    """
    if api == "cloud":
        backend_util.save_backend(api)
        click.secho("Backend switched to {}".format(api), fg="green")

    if api == "server":
        backend_util.save_backend(api)
        click.secho("Backend switched to {}".format(api), fg="green")

        # Set back to default localhost
        set_permanent_user_config({'server': {'host': "http://localhost"}})

    if api not in ["server", "cloud"]:
        # Switch backend to server
        backend_util.save_backend("server")

        # Expect a server hostname
        fp = set_permanent_user_config({'server': {'host': api}})
        click.secho(f"User config {fp} updated with server.host = {api}", fg="green")
