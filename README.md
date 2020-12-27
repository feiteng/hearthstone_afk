# Hearthstone_AFK #
Raw python files for hanging out during ranked match

Current support Hunter only (technically works for other heros, if you modify the code to  wait for 60 seconds and burn the rope)

Basically:
- Reads pixel color on your primary monitor and get status of current game
- play hand cards, play board cards, play hero, end turn
- if attacking enemy hero is not available, tries to hit all 7 enemy board positions
- surprise.. 19% win rate 

Usage:
- make a deck
- run Game.py 

Lookouts:
- my computer is 1920 x 1080 resolution, current positions are hard coded, so adjust them accordingly
- can only cast spell on enemies
- animation could lead to problems
- will try to play cards with similar color to green / yellow

