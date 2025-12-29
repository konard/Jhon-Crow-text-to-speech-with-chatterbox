"""PyInstaller hook for chatterbox-tts package.

This hook ensures all chatterbox submodules and their dependencies
are properly collected and included in the PyInstaller bundle.
"""

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all submodules of chatterbox
hiddenimports = collect_submodules('chatterbox')

# Collect any data files (e.g., model configs, tokenizers)
datas = collect_data_files('chatterbox')
