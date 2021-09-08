"""Translator docstring - module for using translator
 service and contiaing f2e and e2f functions."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()
APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION ='2018-05-01'

def create_translator_instance():
    '''Creates translation service instance.'''
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version=VERSION,
        authenticator=authenticator)
    language_translator.set_service_url(URL)
    return language_translator

def english_to_french(english_text):
    '''Translates from english to french with translator instance.'''
    if english_text == "":
        return ""
    translation = create_translator_instance().translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    '''Translates from french to english with translator instance.'''
    if french_text == "":
        return ""
    translation = create_translator_instance().translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
