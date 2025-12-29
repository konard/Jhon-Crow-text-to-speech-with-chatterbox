"""PyInstaller hook for perth package (resemble-perth).

This hook ensures the perth watermarking library's pretrained models
are properly collected and included in the PyInstaller bundle.

The perth package uses pkg_resources.resource_filename() to locate its
pretrained model files, which requires special handling for PyInstaller.
"""

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all submodules of perth
hiddenimports = collect_submodules('perth')

# Collect the pretrained model data files
# These are located in perth/perth_net/pretrained/
datas = collect_data_files('perth')
