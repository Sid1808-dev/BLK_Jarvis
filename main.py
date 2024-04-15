import sys

from script_dummy import generate_widget
from stt import recognize_from_microphone
from tts import convert_text_to_speech


def run_ai_assistant():
    while True:
        spoken_phrase = recognize_from_microphone().lower()

        if 'hey, jarvis.' == spoken_phrase:
            generate_widget()
            jarvis_response_phrase = 'Hey, How Can I help you!'
        elif 'bye' in spoken_phrase:
            jarvis_response_phrase = 'Bye! see you later'
            convert_text_to_speech(jarvis_response_phrase)
            sys.exit()
        else:
            generate_widget()
            jarvis_response_phrase = spoken_phrase

        convert_text_to_speech(jarvis_response_phrase)


# if __name__ == '__main__':
#
#     while True:
#         jarvis_response_phrase = ''
#         spoken_phrase = recognize_from_microphone().lower()
#
#         if 'hey, jarvis.' == spoken_phrase:
#             generate_widget()
#             jarvis_response_phrase = 'Hey, How Can I help you!'
#         elif 'bye' in spoken_phrase:
#             jarvis_response_phrase = 'Bye! see you later'
#             convert_text_to_speech(jarvis_response_phrase)
#             sys.exit()
#         else:
#             generate_widget()
#             jarvis_response_phrase = spoken_phrase
#
#         convert_text_to_speech(jarvis_response_phrase)
