# Regex searches used to pull 206 data from schedule
regex_206_dict = [
    {'key': 'rs_pob', 'value': r'^[1-3]\.[0-9]{1,3} ((\$\s?\d+[,\.\d]+)?) (.+?) (p.?o.? box.+?\d+)(.+?[0-9]{5}).+basis for the claim:? (\w+\s\w+)'},
    {'key': 'rs_w_claim', 'value': r'^[1-3]\.[0-9]{1,3} ((\$\s?\d+[,\.\d]+)?) (.+?) ([0-9].+?[0-9]{5}).+basis for the claim:? (\w+\s?\w+)'},
    {'key': 'rs_unk', 'value': r'^[1-3]\.[0-9]{1,3} (unknown) (.+?) ([0-9].+?[0-9]{5}).+basis for the claim:? (\w+\s?\w+)'},
    {'key': 'rs_n2_claim', 'value': r'^[1-3]\.[0-9]{1,3} ((\$\s?\d+[,\.\d]+)?) \$\s?\d+[,\.\d]+(.+?) ([0-9].+?[0-9]{5})'},
    {'key': 'rs_n_claim', 'value': r'^[1-3]\.[0-9]{1,3} ((\$\s?\d+[,\.\d]+)?) (.+?) ([0-9].+?[0-9]{5})'},
    {'key': 'rs_rest', 'value': r'^[1-3]\.[0-9]{1,3} ((\$\s?\d+[,\.\d]+)?) (.+)'},
    {'key': 'rs_rest_unk', 'value': r'^[1-3]\.[0-9]{1,3} (unknown) (.+)'},
    {'key': 'rs_search_itv1', 'value': r'[1-3]\.[0-9]{1,3} as of the.+?apply (\$\s?\d+[,\.\d]+)(.+\w\w,? [0-9]{5})'},
    {'key': 'rs_search_itv2', 'value': r'[1-3]\.[0-9]{1,3}(.+)(\$\s?\d+[,\.\d]+)(.+\w\w,? [0-9]{5})'},
    {'key': 'rs_search_it', 'value': r'[1-3]\.[0-9]{1,3}.+(\$\s?\d+[,\.\d]+)(.+\w\w,? [0-9]{5})'},
    {'key': 'rs_search_it_unk', 'value': r'[1-3]\.[0-9]{1,3}.+(unknown)\s(.+)(.+\w\w,? [0-9]{5})'}
]

# List of words we know to remove to improve parsing
rem_word = [
    'as of the petition filing date, the claim is: check all that apply.',
    'nonpriority creditor\'s name and mailing address',
    'contingent',
    'unliquidated',
    'disputed',
    'date(s) debt was incurred',
    'check all that apply.',
    'last 4 digits of account number',
    'is the claim subject to offset?',
    'no',
    'yes',
    'basis for the claim',
    'as of the petition filing date, the claim is:',
    'priority creditor\'s name and mailing address',
    'basis for the claim:',
    'date or dates debt was incurred',
    'last 4 digits of account',
    'number specify code subsection of priority unsecured claim:',
    'debtor',
    'case number (if known)',
    'name',
    'part 1:',
    'additional page',
    'unpaid salary prior to 12/31/19',
    'last 4 digits of account',
    'specify code subsection of priority unsecured',
    'claim: 11 u.s.c. § 507(a) (4)',
    'official form 206e/f',
    'schedule e/f: creditors who have unsecured claims',
    'as of the petition filing date, the claim is: check all that',
    'as of the petition filing date the claim is check all that apply.',
    'apply.',
    'as of the petition filing date, the claim is: check all that apply',
    'as of the petition filling date, the claim is: check all that apply.'
]