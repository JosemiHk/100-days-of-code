"""Validate evidence-backed learning entries without changing repository state."""
import argparse
import json
from datetime import date
from pathlib import Path


def validate(entries, root, today=None):
    today = today or date.today()
    root = Path(root).resolve()
    if not isinstance(entries, list):
        raise ValueError('Log must be a JSON array')
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError('Each entry must be an object')
        day = entry.get('day')
        if type(day) is not int or not 1 <= day <= 100 or day in seen:
            raise ValueError('Days must be unique integers from 1 to 100')
        seen.add(day)
        try:
            recorded = date.fromisoformat(entry['date'])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError('Each entry needs an ISO date') from exc
        if recorded > today:
            raise ValueError('Future completion dates are not allowed')
        for field in ('summary', 'learned', 'verification', 'assistance'):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ValueError(f'Missing substantive field: {field}')
        evidence = entry.get('evidence')
        if not isinstance(evidence, list) or not evidence:
            raise ValueError('At least one evidence file is required')
        for name in evidence:
            if not isinstance(name, str) or not name.strip():
                raise ValueError('Evidence paths must be nonempty strings')
            path = (root / name).resolve()
            if Path(name).is_absolute() or not path.is_relative_to(root):
                raise ValueError('Evidence must stay inside the repository')
            if not path.is_file() or path.stat().st_size == 0:
                raise ValueError(f'Evidence file missing or empty: {name}')
    return len(seen)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        entries = json.loads((args.root / 'log/entries.json').read_text(encoding='utf-8'))
        count = validate(entries, args.root)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Invalid progress log: {exc}\n')
    print(f'{count}/100 evidence-backed entries. Validation does not prove learning or authorship.')


if __name__ == '__main__':
    main()
