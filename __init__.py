import os

from .install import install_styleTTS2_fix, uninstall_styleTTS2_fix

root_path = "StyleTTS2/"
if os.path.isdir(f"{root_path}Models") and os.path.isdir(f"{root_path}voices"):
    print("StyleTTS2 data exist")
else:
    print("StyleTTS2 data not exist\n remove previous data")
    uninstall_styleTTS2_fix()
    print("\nInstall...")
    install_styleTTS2_fix()


from .styleTTS2 import TTS2, compute_style, inference
