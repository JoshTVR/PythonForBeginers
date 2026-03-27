# Lists — Summary

You just added a super helpful tool to your coding toolbox: lists! 🎉

Here's a full recap of everything from this chapter:

- Lists store multiple items in a single variable: `my_list = ['a', 'b', 'c']`
- Lists are 0-indexed: the first item is at index `0`, not `1`.
- Negative indices count from the end: `list[-1]` is the last item.
- Slicing accesses a range: `list[start:end]` (end is non-inclusive).
- Lists can hold mixed data types: strings, ints, floats, booleans — all in one.
- The `in` operator checks membership: `'x' in my_list` returns `True` or `False`.
- You can update items by index: `list[0] = 'new value'`
- Built-in functions: `len()`, `max()`, `min()`, `sum()`, `sorted()`
- All 11 list methods: `.append()`, `.clear()`, `.copy()`, `.count()`, `.extend()`, `.index()`, `.insert()`, `.pop()`, `.remove()`, `.reverse()`, `.sort()`
- Two iteration patterns:
  - `for item in list` — loop by value
  - `for i in range(len(list))` — loop by index

---

# Quick Cheat Sheet

| What you want | Syntax | Example |
|---|---|---|
| Create a list | `name = [a, b, c]` | `scores = [90, 85, 72]` |
| Access by index | `list[i]` | `scores[0]` → `90` |
| Access last item | `list[-1]` | `scores[-1]` → `72` |
| Slice | `list[start:end]` | `scores[0:2]` → `[90, 85]` |
| Modify item | `list[i] = x` | `scores[0] = 95` |
| Add to end | `list.append(x)` | `scores.append(100)` |
| Remove by value | `list.remove(x)` | `scores.remove(85)` |
| Remove by index | `list.pop(i)` | `scores.pop(0)` |
| Get length | `len(list)` | `len(scores)` → `3` |
| Iterate | `for x in list` | `for s in scores: print(s)` |

---

## Instructions

A bucket list is a collection of experiences or achievements you hope to accomplish in your lifetime. 🪣

Create a `bucket_list.py` program that:

1. Creates a `things_to_do` list with at least 10 goals — make them real, make them yours
2. Iterates over the list and prints everything out

For example:

```py
things_to_do = [
    '🚀 Create the dopest learn-to-code platform ever.',
    '⛰️ Hike the Pacific Crest Trail.',
    '🏡 Build an A-frame house and raise some goats.',
    '🌏 Live somewhere in Asia for a year.',
    '🎸 Release an album.',
    '📝 Write a book.',
    '🏆 Reach 100k subscribers on YouTube.',
    '🚐 Road trip with the fam.',
    '🍳 Open a cozy diner upstate.',
    '👴🏻 Grow old with no regrets.'
]
```

The days are long but the years are short — write the things you actually want to do.

ଘ(੭ˊᵕˋ)੭* ੈ✩‧˚

## Solved Exercise:

```py
# bucket_list.py

things_to_do = [
    '🌐 Launch my own tech startup focused on immersive digital experiences.',
    '🎮 Develop a viral indie video game and see streamers play it.',
    '🕶️ Create a VR/AR educational platform that changes how people learn.',
    '✈️ Travel to Tokyo and experience the intersection of tech and tradition.',
    '🎤 Speak at an international tech or gaming conference.',
    '📱 Build a mobile app that gets 1M downloads.',
    '🏡 Design and 3D-print my own smart home (with secret rooms).',
    '📚 Publish a practical book about digital business for creators.',
    '💡 Mentor students in coding, 3D modeling, or entrepreneurship.',
    '🚀 Intern or collaborate with a top tech company like Google or Unity.',
    '🌍 Take a year to travel and work remotely from different countries.',
    '🎥 Start a YouTube channel sharing tutorials on Unity, AR/VR, and digital biz.',
    '🖼️ Exhibit a digital art/VR piece in a physical gallery.',
    '💪 Build a high-performing, creative team for a passion project.',
    '🧘‍♂️ Take a digital detox retreat in the mountains.',
    '🤝 Negotiate my first big international business deal.',
    '🎓 Finish my engineering degree with a project I\'m proud to showcase.',
    '📊 Launch a SaaS product that automates business intelligence for small businesses.',
    '🏅 Get certified in a hot tech area — AI, cloud computing, or advanced data analytics.',
    '🎵 Compose and release an original soundtrack for a game or film.',
    '🚗 Road trip across Mexico, visiting every major archaeological site.',
    '🔗 Build an online community for young digital creators.',
    '🍣 Try every Michelin-star restaurant in a new country.',
    '📈 Grow my LinkedIn following and inspire students from Latin America.',
    '👴🏻 Look back and know I built something that lasts longer than me.'
]

for i in range(len(things_to_do)):
    print(things_to_do[i])
```

---

Chapter 6 — done! 🏆 Next up: **Chapter 7 — Functions**. Time to stop repeating yourself. 🚀
