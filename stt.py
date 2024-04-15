import os
import azure.cognitiveservices.speech as speechsdk


def recognize_from_microphone():
    final_spoken_phrase = ''

    speech_config = speechsdk.SpeechConfig(subscription='2a7f633b7e96439383b955417a0121aa', region='eastus')
    speech_config.speech_recognition_language = "en-US"
    speech_config.set_property(speechsdk.PropertyId.Speech_SegmentationSilenceTimeoutMs, "3000")

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True, )
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        final_spoken_phrase = speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        final_spoken_phrase = 'Did not understand what was said. Please retry!!'
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        final_spoken_phrase = 'Did not understand what was said. Please retry!!'
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
            final_spoken_phrase = 'Did not understand what was said. Please retry!!'

    return final_spoken_phrase


recognize_from_microphone()
