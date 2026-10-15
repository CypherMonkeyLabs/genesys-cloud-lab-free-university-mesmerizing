import hashlib


def _rotate_quiz(lesson_id, quiz):
    rotated = []
    for question, choices, answer, why in quiz:
        if answer != 0 or len(choices) != 4:
            raise SystemExit(f"{lesson_id} quiz shape: {question[:40]}")
        shift = int(hashlib.sha256(f"{lesson_id}|{question}".encode()).hexdigest(), 16) % 4
        ordered = choices[shift:] + choices[:shift]
        rotated.append((question, ordered, (4 - shift) % 4, why))
    return rotated


_ERRORS = []


def lesson(id, title, level, minutes, summary, paras, cite_list, figure, flow_title, steps, quiz, cards, lab_title, lab_steps, lab_success, fault, uncertainty=""):
    quiz = _rotate_quiz(id, quiz)
    if len(quiz) != 6:
        _ERRORS.append(f"{id} quiz {len(quiz)}")
    if len(cards) != 4:
        _ERRORS.append(f"{id} cards {len(cards)}")
    if len(steps) < 4:
        _ERRORS.append(f"{id} steps {len(steps)}")
    if len(lab_steps) < 3:
        _ERRORS.append(f"{id} lab {len(lab_steps)}")
    if len(paras) < 2:
        _ERRORS.append(f"{id} paras {len(paras)}")
    if len(fault) != 5:
        _ERRORS.append(f"{id} fault {len(fault)}")
    ft, sy, lg, ca, fx = fault
    return {
        "id": id,
        "title": title,
        "level": level,
        "minutes": minutes,
        "summary": summary,
        "paras": paras,
        "cites": cite_list,
        "uncertainty": uncertainty,
        "figure": figure,
        "flow": {
            "title": flow_title,
            "steps": [
                {"from": a, "to": b, "title": t, "detail": d, "inspect": i}
                for a, b, t, d, i in steps
            ],
        },
        "quiz": [{"q": q, "choices": ch, "answer": ans, "why": why} for q, ch, ans, why in quiz],
        "cards": [{"front": f, "back": b} for f, b in cards],
        "lab": {"title": lab_title, "steps": lab_steps, "success": lab_success},
        "fault": {"title": ft, "symptom": sy, "log": lg, "cause": ca, "fix": fx},
    }


def fig(caption, nodes, edges):
    return {
        "caption": caption,
        "nodes": [{"id": i, "label": label, "kind": kind, "x": x, "y": y} for i, label, kind, x, y in nodes],
        "edges": [{"a": a, "b": b} for a, b in edges],
    }


def q(question, correct, wrongs, why):
    choices = [correct, *wrongs]
    return (question, choices, 0, why)
