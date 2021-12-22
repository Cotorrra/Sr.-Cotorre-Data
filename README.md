# Sr.-Cotorre-Data
Repo for the main data for Sr. "CoTorre". and all other versions of it.

It's divided in 4 files:
Each folder language (es, en, etc.) should have 4 files with the following information:

### errata.json
It contains the cards erratas: 

- `code`: Its card code in ArkhamDB (example 01016 is the .45 Automatic)
- `text`: Its errata text in its frontal side
- `text_back`: Its errata text for the back side (useful for Deckbuilding Options erratas)

### framework.json
It contains the "Phase" and "Skill Test" framework with each step of them as they come from the game's manual.

### lang.json
It contains all the strings that the bot uses to create its Discord information. (Slash commands descriptions, tags, etc.).

### taboo.json
It contains the current (and former) taboo data. Currently, it's based on the ArkhamDB Taboos API response.

### tarot.json
It contains the information for the RTCU Tarot Cards.

- `name`: The name of the tarot card
- `up`: Positive Effect
- `down`: Inverted Effect
- `illustrator`: The Illustrator that made this cool art.
- `set`: Set name.
- `number`: The number of the card.
