"""Emit the pre-rendered make.fun entry using only the standard library."""
import os
import shutil
import sys


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    size = os.path.getsize(source)
    if not 0 < size <= 1024 * 1024:
        raise ValueError("Source image must be nonempty and at most 1 MiB")
    with open(source, "rb") as image:
        if image.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError("Source image is not a PNG")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    if not (os.path.exists(destination) and os.path.samefile(source, destination)):
        shutil.copyfile(source, destination)
    if size != os.path.getsize(destination):
        raise OSError("Output size does not match source size")
    print("Wrote " + destination + " (" + str(size) + " bytes)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print("Entry output failed: " + str(error), file=sys.stderr)
        sys.exit(1)
