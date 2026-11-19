"""Deliver the bundled news atlas without rendering or network access."""
import os
import shutil
import sys


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entry.png')
    source_size = os.path.getsize(source)
    if not 0 < source_size <= 1024 * 1024:
        raise OSError('The bundled image is empty or exceeds 1 MiB')
    destination_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(destination_dir, exist_ok=True)
    destination = os.path.join(destination_dir, 'entry.png')
    if os.path.realpath(source) != os.path.realpath(destination):
        shutil.copyfile(source, destination)
    if source_size != os.path.getsize(destination):
        raise OSError('The copied image has an unexpected size')
    print('Image written to ' + destination + ' (' + str(source_size) + ' bytes)')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except OSError as error:
        print('Image delivery failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
