from flask import Flask, jsonify
from collections import deque

app = Flask(__name__)

W = 10
q = deque(maxlen=W)

def p(n=5):  # Prime
    r, x = [], 2
    while len(r) < n:
        if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)):
            r.append(x)
        x += 1
    return r

def f(n=5):  # Fibonacci
    r = [0, 1]
    for _ in range(n - 2):
        r.append(r[-1] + r[-2])
    return r

def e(n=5):  # Even
    return [i for i in range(2, 2 * n + 1, 2)]

def r(n=5):  # Random (placeholder)
    return [i for i in range(1, n + 1)]

@app.route('/numbers/<t>', methods=['GET'])
def get_n(t):
    p_s = list(q)

    if t == 'p':
        n = p(5)
    elif t == 'f':
        n = f(5)
    elif t == 'e':
        n = e(5)
    elif t == 'r':
        n = r(5)
    else:
        return jsonify({"err": "Invalid"}), 400

    for i in n:
        if i not in q:
            q.append(i)

    c_s = list(q)
    a = round(sum(c_s) / len(c_s), 2) if c_s else 0.0

    return jsonify({
        "windowPrevState": p_s,
        "windowCurrState": c_s,
        "numbers": n,
        "avg": a
    })

if __name__ == '__main__':
    app.run(port=9876, debug=True)
