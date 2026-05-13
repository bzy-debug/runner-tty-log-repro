#!/usr/bin/env python3
import sys
import time


def main() -> None:
    is_tty = sys.stdout.isatty()
    print(f"python_stdout_isatty={str(is_tty).lower()}")

    if not is_tty:
        for frame in range(1, 6):
            print(f"plain progress frame {frame}/5")
            time.sleep(0.05)
        return

    for frame in range(1, 26):
        sys.stdout.write(f"\rtty redraw frame {frame:02d}/25")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
