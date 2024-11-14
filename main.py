from pathlib import Path

project_dir = Path(__file__).parent

source_file = project_dir / '.venv' / 'Lib' / 'site-packages' / 'six.py'
destination_file = project_dir / '.venv' / 'Lib' / 'site-packages' / 'kafka' / 'vendor' / 'six.py'

if source_file.exists() and destination_file.exists():
    with open(source_file, 'r') as source:
        content = source.read()

    with open(destination_file, 'w') as destination:
        destination.write(content)

    print("Successfully.")  # noqa
else:
    print("Failed. (One of the) files was not found.")  # noqa
