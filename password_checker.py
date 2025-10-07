
### Starter kod (`password_checker.py`) — nusxa ko‘chiring
```python
import re

def score_password(pw: str) -> int:
    score = 0
    if len(pw) >= 8:
        score += 1
    if re.search(r"[a-z]", pw) and re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        score += 1
    return score

def strength_label(score: int) -> str:
    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    pw = input("Enter password to check: ")
    s = score_password(pw)
    print(f"Score: {s} — {strength_label(s)}")
