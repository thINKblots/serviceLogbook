NO_START_TREE = {
    'question': 'Does the engine crank?',
    'yes': {
        'question': 'Does it start and then die?',
        'yes': 'Diagnosis: Possible fuel supply issues (e.g. fuel filters, air in fuel, etc.)',
        'no': {
            'question': 'Is this a gas engine?',
            'yes': {
                'question': 'Does the spark plug have spark?',
                'yes': 'Check fuel system.',
                'no': 'Check ignition system.'
            },
            'no': {
                'question': 'Is this a diesel engine?',
                'yes': {
                    'question': ''
                }
            }
        }
    }
}