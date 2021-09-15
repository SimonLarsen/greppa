import click
import pandas as pd
from typing import Optional
from .files import guess_file_type, read_file, write_file
from .grep import grep


@click.command()
@click.argument("pattern", type=str)
@click.argument("infile", type=click.Path(exists=True, readable=True))
@click.argument(
    "outfile", type=click.Path(exists=False, writable=True), required=False
)
@click.option("-n", "--max-rows", type=int, default=25)
@click.option(
    "--intype",
    type=click.Choice(["parquet"], case_sensitive=False),
    required=False,
)
@click.option(
    "--outtype",
    type=click.Choice(["parquet"], case_sensitive=False),
    required=False,
)
def cli(
    pattern: str,
    infile: click.Path,
    outfile: Optional[click.Path],
    max_rows: int,
    intype: Optional[click.Choice],
    outtype: Optional[click.Choice],
) -> None:
    if intype is None:
        in_type_str = guess_file_type(str(infile))
    else:
        in_type_str = str(intype)

    if outfile is not None:
        if outtype is None:
            out_type_str = guess_file_type(str(outfile))
        else:
            out_type_str = str(outtype)

    df = read_file(str(infile), in_type_str)
    df = grep(df, pattern)

    if outfile:
        write_file(df, str(outfile), out_type_str)
    else:
        with pd.option_context("display.max_rows", max_rows):
            click.echo(df)
