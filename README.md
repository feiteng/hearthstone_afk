# Hearthstone_AFK #
Raw python files for hanging out during ranked match to earn 400 xp on your journey book

Works best on Hunter (and other face deck)

Basic logic:
- Reads pixel color on your primary monitor and get status of current game
- play hand cards, play board cards, play hero, end turn (tweak order for your desired hero / deck)
- if attacking enemy hero is not available, tries to hit all 7 enemy board positions for taunt minions
- surprise.. 19% win rate (depending on your deck ofc)


Usage:
- make a deck
- run playGame.py

Lookouts:
- my computer is 1920 x 1080 resolution, current positions are hard coded, so adjust them accordingly
- can only cast spell on enemies
- animation could lead to problems
- will try to play cards with similar color to green / yellow

