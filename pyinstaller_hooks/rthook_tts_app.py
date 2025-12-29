"""PyInstaller runtime hook for tts_app.

This runtime hook runs at application startup before any imports,
ensuring the Python path is correctly set up for the bundled environment.

It also patches pkg_resources to correctly locate bundled data files
for packages like perth that use resource_filename().
"""

import sys
import os

def setup_tts_app_path():
    """Ensure tts_app package can be imported in PyInstaller bundle."""
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller bundle
        # sys._MEIPASS is the path where PyInstaller extracts bundled files
        base_path = sys._MEIPASS

        # Ensure base_path is in sys.path at the beginning
        if base_path not in sys.path:
            sys.path.insert(0, base_path)

        # Also add the tts_app package path explicitly
        tts_app_path = os.path.join(base_path, 'tts_app')
        if os.path.exists(tts_app_path) and tts_app_path not in sys.path:
            sys.path.insert(0, tts_app_path)


def setup_pkg_resources_path():
    """Patch pkg_resources to find bundled data files in PyInstaller.

    The perth package uses pkg_resources.resource_filename() to locate
    its pretrained models. In a PyInstaller bundle, we need to ensure
    that pkg_resources can find files extracted to sys._MEIPASS.
    """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS

        # Add _MEIPASS to working set for pkg_resources
        try:
            import pkg_resources
            # Add the base path as a location for finding package data
            if base_path not in pkg_resources.working_set.entries:
                pkg_resources.working_set.add_entry(base_path)
        except ImportError:
            # pkg_resources not available, skip
            pass


# Execute the path setups
setup_tts_app_path()
setup_pkg_resources_path()
