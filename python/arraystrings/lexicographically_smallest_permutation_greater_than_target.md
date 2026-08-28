# Lexicographically Smallest Permutation Greater Than Target

Find the **lexicographically smallest permutation of `s`** that is **strictly greater than `target`**. If none exists, return `""`.

## High-level idea

Build the answer **left → right**, matching `target` as long as possible, then make the **first increase** as early as possible, and fill the rest with the **smallest leftover letters**.

```
target:  a  b  b  a
answer:  a  c  … …     ← same prefix "a", then bump at position 1
```

## Walkthrough with `s = "aabb"`, `target = "abba"`

**Available letters (counts):**

```
a: 2
b: 2
c..z: 0
```

### Position 0 — try to keep `'a'` (same as target)

```
target:  a  b  b  a
         ^
try:     a  ?  ?  ?
```

Spend one `a` → remaining `{a:1, b:2}`.

Ask: *can the leftover still form something > `"bba"`?*

Largest leftover string = `"bba"` → `"bba" > "bba"`? **No.**

So matching `'a'` here is a dead end → put the `a` back.

### Position 0 — bump to something larger than `'a'`

Next available letter > `'a'` is `'b'`:

```
answer so far:  b
remaining:      {a:2, b:1}
```

Fill the rest with the **smallest** leftover order: `a, a, b`

```
answer:  b a a b   →  "baab"
```

`"baab" > "abba"` ✓ and it’s the smallest such permutation.

That’s exactly this block in the code:

```python
for c in range(t + 1, 26):
    if cnt[c] > 0:
        cnt[c] -= 1
        res.append(chr(c + ord("a")))
        # Lexicographically smallest permutation of remaining characters
        res.append(
            "".join(chr(j + ord("a")) * cnt[j] for j in range(26))
        )
        return "".join(res)
```

## The two choices at each index `i`

```
                target[i]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
   1) keep same char     2) pick first larger char
      (if available)        then append sorted leftovers
         │                   → DONE (return)
         ▼
   check: can remaining
   still beat target[i+1:]?
         │
    yes ─┴─ no
     │      │
  commit   undo & try option 2
  & move on
```

### Option 1 — stay equal so far (greedy “match prefix”)

```python
if cnt[t] > 0:
    cnt[t] -= 1
    # Check for success
    if self.can_greater(cnt, target[i + 1 :]):
        res.append(target[i])
        continue
    cnt[t] += 1
```

`can_greater` asks: with what’s left, is the **largest** possible suffix still > `target[i+1:]`?

```python
def can_greater(self, cnt: list[int], suffix: str) -> bool:
    # Construct the largest string from largest to smallest
    max_str = "".join(
        chr(i + ord("a")) * cnt[i] for i in range(25, -1, -1) if cnt[i] > 0
    )
    return max_str > suffix
```

If even the best leftover can’t beat the rest of `target`, matching here locks you into something ≤ `target` later → backtrack that letter.

### Option 2 — first increase, then smallest tail

Pick the smallest letter `> target[i]` you still have, then dump leftovers in ascending order. That guarantees:

1. Strictly greater than `target` (first differing position is larger)
2. Lexicographically smallest among such answers (increase as early/small as possible; rest minimized)

## Another example: `s = "bac"`, `target = "abc"` → `"acb"`

```
counts: a:1 b:1 c:1

i=0, target='a'
  keep 'a'? remaining {b:1,c:1}
  max leftover = "cb" > "bc"? YES
  → commit 'a'   res = "a"

i=1, target='b'
  keep 'b'? remaining {c:1}
  max leftover = "c" > "c"? NO
  → undo
  bump: next > 'b' is 'c'
  → res = "a" + "c" + leftover("b") = "acb"
```

```
target:  a  b  c
answer:  a  c  b
         │  └─ first bump
         └─ matched prefix
```

## Impossible case: `s = "abc"`, `target = "cba"`

`"cba"` is already the largest permutation of `s`. At every position, you can’t bump higher, so the loop returns `""`.

Also, if you somehow matched the whole string, the final `return ""` after the loop means “equal to `target` isn’t allowed” (need **strictly** greater).

## Mental model (one sentence)

> Match `target` from the left while a greater future is still possible; as soon as you must diverge, take the smallest larger letter and append the sorted leftovers.

That’s next-permutation thinking, but constrained to the multiset of letters in `s`.
