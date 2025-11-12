#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    try:
        from django.core.management import execute_from_command_line
    except Exception:
        # Django may not be installed in this environment; this file is provided for exercise tooling.
        print('Django not available. This manage.py is present for repository completeness.')
        return
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
