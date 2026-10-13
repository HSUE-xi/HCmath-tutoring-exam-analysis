"""Validate an exam's per-subquestion score map from a JSON file.
Usage: python validate_exam.py exam.json
JSON shape: {"full_score":100,"questions":[{"id":"一-1","points":3},...]}
"""
import json
import sys
from decimal import Decimal


def validate(payload):
    questions = payload['questions']
    if not questions:
        raise ValueError('題目清單為空')
    names = [str(q['id']).strip() for q in questions]
    if any(not n for n in names) or len(names) != len(set(names)):
        raise ValueError('題號不可空白或重複')
    points = [Decimal(str(q['points'])) for q in questions]
    if any(p <= 0 for p in points):
        raise ValueError('小題配分必須大於 0')
    full = Decimal(str(payload['full_score']))
    total = sum(points)
    if total != full:
        raise ValueError(f'配分總和 {total} 不等於滿分 {full}')
    return len(questions), total


if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf-8') as f:
        data = json.load(f)
    count, total = validate(data)
    print(f'驗證通過：{count} 小題，總分 {total}')
