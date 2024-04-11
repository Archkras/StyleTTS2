import os

root_path = "StyleTTS2/"


def install_styleTTS2_original():
    try:
        os.system("")
        os.system(
            f"git clone https://github.com/yl4579/StyleTTS2.git && \
            cd StyleTTS2 && \
            git-lfs clone https://huggingface.co/yl4579/StyleTTS2-LibriTTS && \
            mv StyleTTS2-LibriTTS/Models . && \
            mv StyleTTS2-LibriTTS/reference_audio.zip . && \
            unzip reference_audio.zip && \
            mv reference_audio voices && \
            cd .. && \
            mv -t . StyleTTS2/Configs StyleTTS2/Data StyleTTS2/Models StyleTTS2/Modules StyleTTS2/Utils StyleTTS2/voices && \
            mv StyleTTS2/*.py . && \
            rm -rf StyleTTS2"
        )
    except Exception as error:
        print("An error occurred:", error)


def install_styleTTS2_fix():
    try:
        os.system("")
        os.system(
            f"cd {root_path} && \
            git-lfs clone https://huggingface.co/yl4579/StyleTTS2-LibriTTS && \
            mv StyleTTS2-LibriTTS/Models . && \
            mv StyleTTS2-LibriTTS/reference_audio.zip . && \
            unzip reference_audio.zip && \
            mv reference_audio voices  && \
            rm -rf StyleTTS2-LibriTTS && \
            rm reference_audio.zip"
        )
        print("StyleTTS2 data load ok!")
    except Exception as error:
        print("An error occurred:", error)


def uninstall_styleTTS2_fix():
    try:
        os.system("")
        os.system(
            f"cd {root_path} && \
            rm -rf StyleTTS2-LibriTTS/ Models/ Demo/reference_audio/ reference_audio voices"
        )
        print("StyleTTS2 data removed!")
    except Exception as error:
        print("An error occurred:", error)
