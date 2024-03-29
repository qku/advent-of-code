from datetime import datetime
from pathlib import Path
import shutil

import click
import requests

from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.option('--year', default=-1, help='Year in YYYY format.')
@click.option('--day', default=-1, help='Day in DD format.')
def main(year, day):
    """Advent of Code download script."""

    today = datetime.today()
    today_year = int(today.strftime('%Y'))
    today_day = int(today.strftime('%d'))

    if year < 0:
        year = today_year
    if day < 0:
        day = today_day

    if day > 25:
        click.echo('Christmas is over :(')
        return

    # session cookie
    with open('session') as f:
        session = f.read()
        session.strip()
    cookies = {'session': session}

    # post request
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    r = requests.post(url, cookies=cookies)

    # create directory if it doesn't exist yet
    root = 'src/advent_of_code'
    folder = f'{root}/{year}/{day:02}'
    Path(folder).mkdir(parents=True, exist_ok=True)

    # write input.txt file
    with open(folder + '/input.txt', 'w') as f:
        f.write(r.text)

    # copy over templates
    shutil.copy(f'{root}/template/day00.py', f'{folder}/day{day:02}.py')
    shutil.copy(f'{root}/template/test_day00.py', f'{folder}/test_day{day:02}.py')

    # create empty test input file
    open(folder + '/test_input.txt', 'a').close()
