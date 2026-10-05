#!/usr/bin/env python3
"""Offline catalog, generated-content and local-link validation."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import collections
import datetime
import json
import re
import sys

from build_catalog import ROOT, load_data, rendered_outputs

def strip_fences(text):
    # Examples may legitimately contain not-yet-inserted figure paths.
    return re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', text, flags=re.M | re.S)

def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen = collections.Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', strip_fences(text), flags=re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading).lower()
        # GitHub keeps Unicode letters, digits and hyphens while removing punctuation.
        slug = ''.join(c for c in heading if c.isalnum() or c in ' _-')
        slug = slug.replace(' ', '-')
        count = seen[slug]
        seen[slug] += 1
        result.add(slug + (f'-{count}' if count else ''))
    return result

def validate():
    errors = []
    papers, taxonomy = load_data()
    topics = {t['id']: t for t in taxonomy}
    required = {'id','title','authors','year','venue','url','origin','survey_sections',
                'stage','topic','annotation','verification'}
    ids, urls = set(), set()
    for p in papers:
        label = p.get('id', '<missing id>')
        if not required <= p.keys():
            errors.append(f'{label}: missing fields {sorted(required-p.keys())}'); continue
        if not re.fullmatch(r'[a-z][a-z0-9-]*', label) or label in ids:
            errors.append(f'{label}: invalid or duplicate ID')
        ids.add(label)
        if p['url'] in urls: errors.append(f'{label}: duplicate paper URL')
        urls.add(p['url'])
        if p['topic'] not in topics or p['stage'] != topics[p['topic']]['stage']:
            errors.append(f'{label}: taxonomy/stage mismatch')
        if p['origin'] not in {'survey','addition'}:
            errors.append(f'{label}: invalid origin')
        if bool(p['survey_sections']) != (p['origin'] == 'survey'):
            errors.append(f'{label}: inconsistent manuscript provenance')
        if not p['authors'] or not all(isinstance(a,str) and a for a in p['authors']):
            errors.append(f'{label}: missing authors')
        if not isinstance(p['year'],int) or not 1900 <= p['year'] <= datetime.date.today().year+1:
            errors.append(f'{label}: invalid year')
        for key in ('url','code_url'):
            if p.get(key):
                u=urlsplit(p[key])
                if u.scheme!='https' or not u.netloc or re.search(r'\s',p[key]):
                    errors.append(f'{label}: invalid {key}')
        try: datetime.date.fromisoformat(p['verification']['checked_on'])
        except (ValueError,KeyError,TypeError): errors.append(f'{label}: invalid verification date')
        if p['verification'].get('source_url') != p['url']:
            errors.append(f'{label}: source check is for a different URL')
        if any(token in p['title']+p['url'] for token in ('TODO','TBD','XXXXXXXX','turn0search')):
            errors.append(f'{label}: placeholder in bibliographic record')
    for path, expected in rendered_outputs().items():
        if not path.exists() or path.read_text(encoding='utf-8') != expected:
            errors.append(f'{path.relative_to(ROOT)}: generated file is stale')
    bib=(ROOT/'references.bib').read_text(encoding='utf-8')
    keys=re.findall(r'^@\w+\{([^,]+),',bib,flags=re.M)
    if len(keys)!=len(set(keys)) or set(keys)!=ids:
        errors.append('BibTeX keys do not match the catalog exactly')
    files=list(ROOT.rglob('*.md'))
    contents={p.resolve():p.read_text(encoding='utf-8') for p in files}
    checked=0
    for path, text in contents.items():
        clean=strip_fences(text)
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',clean):
            u=urlsplit(target)
            if u.scheme or u.netloc: continue
            checked+=1
            destination=(path.parent/unquote(u.path)).resolve() if u.path else path
            if not destination.is_relative_to(ROOT.resolve()):
                errors.append(f'{path.name}: local link escapes repository: {target}'); continue
            if not destination.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing local target {target}'); continue
            if u.fragment and destination.suffix=='.md':
                found=anchors(contents.get(destination,destination.read_text(encoding='utf-8')))
                if unquote(u.fragment) not in found:
                    errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')
    report=dict(catalog_entries=len(papers),manuscript_entries=sum(p['origin']=='survey' for p in papers),
                added_entries=sum(p['origin']=='addition' for p in papers),
                code_links=sum(bool(p.get('code_url')) for p in papers),
                topics=len(topics),markdown_files=len(files),local_links_checked=checked,
                bibliography_entries=len(keys),errors=errors)
    return report

if __name__ == '__main__':
    try:
        result=validate()
        print(json.dumps(result,indent=2))
        sys.exit(bool(result['errors']))
    except (ValueError,KeyError,FileNotFoundError,TypeError) as exc:
        print(f'Validation failed: {exc}',file=sys.stderr)
        sys.exit(1)
