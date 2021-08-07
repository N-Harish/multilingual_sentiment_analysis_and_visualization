from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = <your ibm API key>
url = <your ibm translation url>

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)


def lan_det(text1):
    ln = lt.identify(text=text1).get_result()
    model_id1 = ln['languages'][0]['language'] + "-en"
    if model_id1 == "en-en":
        return text1
    else:
        translation = lt.translate(text=text1, model_id=model_id1).get_result()
        return translation['translations'][0]['translation']
