from typing import Dict

from TTS.tts.utils.text.kazakh.phonemizer import kazakh_text_to_phonemes
from TTS.tts.utils.text.phonemizers import BasePhonemizer
_DEF_KK_PUNCS = ",!." 

class KazakhPhonemizer(BasePhonemizer):
    language = "kk"

    def __init__(self, punctuations=_DEF_KK_PUNCS, keep_puncs=True, **kwargs):
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)

    @staticmethod
    def name():
        return "kazakh_phonemizer"

    @staticmethod
    def phonemize_kk(text: str, separator: str = "|") -> str:  # pylint: disable=unused-argument
        return kazakh_text_to_phonemes(text)

    def _phonemize(self, text, separator):
        return self.phonemize_kk(text, separator)

    @staticmethod
    def supported_languages() -> Dict:
        return {"kk": "Kazakh"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True


if __name__ == "__main__":
    txt = "тест"
    e = KazakhPhonemizer()
    print(e.supported_languages())
    print(e.version())
    print(e.language)
    print(e.name())
    print(e.is_available())
    print("`" + e.phonemize(txt) + "`")