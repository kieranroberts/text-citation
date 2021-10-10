import re

def sectionize_wiki_str(content):
    return content.split('\n\n\n==')

def exclude_sections(sections, section_names=['See also', 'Footnotes', 'References', 'External links']):
    desired_sections = list()
    exc_pattern = re.compile(r"^ ({})".format('|'.join(section_names)))
    for sec in sections:
        if not(re.match(exc_pattern, sec)):
            desired_sections.append(sec)
    return desired_sections

def remove_section_title(sections):
    content_only = list()
    pattern = re.compile(r"[ \S]+(.*)", re.DOTALL)
    for sec in sections:
        m = re.match(pattern, sec)
        content_only.append(m.group(1)[1:])
    return content_only

def desectionize_wiki_str(sections):
    return "\n\n\n".join(sections)

def exclude_substring_sections(content, section_names=['See also', 'Footnotes', 'References', 'External links']):
    sections = sectionize_wiki_str(content)
    sections = exclude_sections(sections,section_names=section_names)
    sections = remove_section_title(sections)
    return desectionize_wiki_str(sections)