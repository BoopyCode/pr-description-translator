#!/usr/bin/env python3
"""PR Description Translator - Because 'it works on my machine' isn't a PR description"""

import sys
import re

# The magic translation matrix - because developers speak in tongues
TECH_TO_NORMAL = {
    r'\bLGTM\b': 'Looks good to me (probably didn't read it)',
    r'\bWIP\b': 'Work in progress (aka: I'm committing crimes)',
    r'\brefactor\b': 'I touched everything but nothing changed (trust me)',
    r'\boptimize\b': 'Made it faster (or at least different)',
    r'\bfix\b': 'Broke it yesterday, less broken today',
    r'\benhancement\b': 'Added a button that does nothing',
    r'\btech debt\b': 'My past self was an idiot',
    r'\bedge case\b': 'Something that will break in production',
    r'\bscalability\b': 'Works for our 3 users',
    r'\bsecurity\b': 'Changed "password" to "p@ssw0rd"',
    r'\b\d+\s?ms\b': 'Blazing fast (on my gaming PC)',
    r'\b\d+%\s+faster\b': 'Probably measured wrong',
    r'\bNFR\b': 'Non-functional requirement (aka: magic)',
}

NORMAL_TO_TECH = {
    r'\bbug\b': 'Unexpected feature',
    r'\bworks\b': 'Passes one test case',
    r'\bquick fix\b': 'Technical debt delivery',
    r'\bsimple\b': 'Only 47 files changed',
    r'\beasy\b': 'Will take 3 weeks',
    r'\buser friendly\b': 'Added 14 configuration options',
    r'\bintuitive\b': 'Documentation required',
    r'\brobust\b': 'Handles one error case',
}


def translate_pr(description, mode='normal'):
    """Translates PR descriptions between technical and normal human speak.
    
    Args:
        description: The PR description (probably written during coffee shortage)
        mode: 'normal' for tech→human, 'tech' for human→tech
    
    Returns:
        Translated description with 20% more clarity (results may vary)
    """
    if mode == 'normal':
        translations = TECH_TO_NORMAL
        prefix = 'For normal humans:\n\n'
    else:
        translations = NORMAL_TO_TECH
        prefix = 'For technical reviewers:\n\n'
    
    result = description
    for pattern, replacement in translations.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    return prefix + result


def main():
    """Main function - handles arguments and disappointment"""
    if len(sys.argv) < 2:
        print('Usage: python pr_translator.py "PR description here" [mode]')
        print('Modes: normal (tech→human), tech (human→tech)')
        return
    
    description = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'normal'
    
    if mode not in ['normal', 'tech']:
        print('Error: Mode must be "normal" or "tech" (like your PR quality)')
        return
    
    translated = translate_pr(description, mode)
    print(translated)


if __name__ == '__main__':
    main()
