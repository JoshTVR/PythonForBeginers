# Lists Summary

You just added a super helpful tool to your coding toolbox: lists!

Here's a recap of the chapter:

- Lists are used to store different items in a single variable.
- An index is an item's position in a list. Python lists are \* 0-indexed.
- Slicing can access certain parts of a list with `name[start:end]`.
- Python has built-in functions like `len()`, `max()`, `min()`.
- Lists have built-in methods like `.append()`, `.insert()`, `.remove()`, `.pop().`
- We can iterate over a list using `for-in`.

Now let's pull everything together one last time and build your bucket list!

## Instructions

A bucket list is a number of experiences or achievements that a person hopes to have or accomplish during their lifetime. 🪣

Create a bucket_list.py program with your own unique bucket list.

First, create a `things_to_do` list, and add things you want to do in your lifetime.

For example:

```py
things_to_do = [
'🚀 Create the dopest learn to code platform ever.',
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

Now, iterate over the list and print everything out.

Lastly, to keep yourself accountable, take a screenshot of your program and post your bucket list to Twitter by clicking the icon below.

The days are long but the years are short; from the whole Codédex team, we hope you accomplish all of your wildest dreams!

ଘ(੭ˊᵕˋ)੭\* ੈ✩‧˚

## Solved Exercise:

```py
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
    '🎓 Finish my engineering degree with a project I’m proud to showcase.',
    '📊 Launch a SaaS product that automates business intelligence for small businesses.',
    '🏅 Get certified in a hot tech area—AI, cloud computing, or advanced data analytics.',
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
