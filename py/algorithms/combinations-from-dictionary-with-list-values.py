#coding:utf8

# 从字典里组合列表的值

# I have the following incoming value:
variants = {
    "debug" : ["on", "off"],
    "locale" : ["de_DE", "en_US", "fr_FR"],
}

# I want to process them so I get the following result:
combinations = [
    [{"debug":"on"},{"locale":"de_DE"}],
    [{"debug":"on"},{"locale":"en_US"}],
    [{"debug":"on"},{"locale":"fr_FR"}],
    [{"debug":"off"},{"locale":"de_DE"}],
    [{"debug":"off"},{"locale":"en_US"}],
    [{"debug":"off"},{"locale":"fr_FR"}]
]

# This should work with arbitrary length of keys in the dictionary.
# Played with itertools in Python, but did not found anything matching these requirements.

############

import itertools

varNames = sorted(variants) # 返回字典的keys列表 ['debug', 'locale']
combinations = [dict(zip(varNames, prod)) for prod in itertools.product(*(variants[varName] for varName in varNames))]
print combinations
# [
#     {'debug': 'on', 'locale': 'de_DE'},
#     {'debug': 'on', 'locale': 'en_US'},
#     {'debug': 'on', 'locale': 'fr_FR'},
#     {'debug': 'off', 'locale': 'de_DE'},
#     {'debug': 'off', 'locale': 'en_US'},
#     {'debug': 'off', 'locale': 'fr_FR'}
# ]

combinations2 = [ [ {varName: val} for varName, val in zip(varNames, prod) ] \
                    for prod in itertools.product(*(variants[varName] \
                    for varName in varNames))]
print combinations2
# [
#     [{'debug': 'on'}, {'locale': 'de_DE'}],
#     [{'debug': 'on'}, {'locale': 'en_US'}],
#     [{'debug': 'on'}, {'locale': 'fr_FR'}],
#     [{'debug': 'off'}, {'locale': 'de_DE'}],
#     [{'debug': 'off'}, {'locale': 'en_US'}],
#     [{'debug': 'off'}, {'locale': 'fr_FR'}]
# ]
