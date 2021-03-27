"""
Here we are collecting alf functions for cleaning xml records from whitespaces and /
abbreviations, splitting tag.texts and converting strings with date info to datetimes
"""
import binascii
import datetime
import os
import re

# changing to lowercase, deleting 'р.', 'м.', 'с.', 'смт.', 'смт', 'сщ.', 'с/рада.', 'сщ/рада.', /
# 'вул.' from a string
from django.utils import translation
from num2words import num2words


def clean_name(name):
    return re.sub(r'р\.|м\.|с\.|смт\.|сщ\.|с/рада\.|сщ/рада\.|вул\.', "", name.lower()).strip()


# a dictionary for storing all abbreviations and full forms
SHORT_TO_FULL_DICT = {
    'вул.': 'вулиця ',
    'бульв.': 'бульвар ',
    'просп.': 'проспект ',
    'пров.': 'провулок ',
    'пл.': 'площа ',
    'р-н': 'район',
    'р-ну': 'району',
    'обл.': 'область',
    'области': 'області'
}


# changing to lowercase and abbreviations to full forms like 'р-н' to 'район' /
# (see all cases in short_to_full_dict)
def change_to_full_name(name):
    name = name.lower()
    for abbr, full_form in SHORT_TO_FULL_DICT.items():
        name = name.replace(abbr, full_form)
    return name


# extracting the first word
def get_first_word(string):
    return string.split()[0]


# getting all words before slash and changing string to lowercase
def get_lowercase_substring_before_slash(string):
    return string.split('/')[0].lower()


# extracting all words except first
def cut_first_word(string):
    words_after_first = string.split()[1:]
    return " ".join(words_after_first)


# deleting ';' from a string, then converting it to the datetime format 'Y-m-d'
def format_date_to_yymmdd(str_ddmmyy):
    if str_ddmmyy:
        if ';' in str_ddmmyy:
            str_ddmmyy = str_ddmmyy.replace(";", "")
        if '/' in str_ddmmyy:
            str_ddmmyy = str_ddmmyy.replace("/", ".")
        try:
            date = datetime.datetime.strptime(str_ddmmyy, "%d.%m.%Y").strftime("%4Y-%m-%d")
        except ValueError:
            return None
        return date


# checking if exists, then converting to string
def to_lower_string_if_exists(value):
    if value:
        return str(value).lower()
    return None


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


def uah2words(value):
    lang = translation.get_language()
    if lang == 'uk':
        amount_words = num2words(
            float(value), lang=lang, to='currency',
            currency='UAH', separator=' ', cents=False,
        )
    else:
        uah, kop = divmod(value, 1)
        kop = round(kop * 100)
        amount_words = f'{num2words(uah, lang=lang, to="cardinal")} hryvnias {kop:02} kopiyok'
    return amount_words


def print_recursion(record, root_tab):
    for elem in record:
        print(root_tab, elem.tag, ':', elem.text or '')
        child_tab = root_tab + '\t'
        print_recursion(elem, child_tab)


def get_source_records(search_text, search_tag='EDRPOU', converter_module=
                        'business_register.converter.company_converters.ukr_company_full.UkrCompanyFullConverter'):
    from lxml import etree
    from django.utils.module_loading import import_string
    converter = import_string(converter_module)()
    elements = etree.iterparse(
        source=converter.LOCAL_FOLDER + converter.LOCAL_FILE_NAME,
        tag=converter.RECORD_TAG,
        recover=False,
    )
    index = 0
    for _, record in elements:
        index += 1
        text_from_record = record.xpath(search_tag)[0].text
        if text_from_record == search_text:
            print('Record #', index, 'from:', converter.LOCAL_FILE_NAME)
            print('-------------------------------------------------------------------------')
            print_recursion(record, '')
        record.clear()
        for ancestor in record.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
