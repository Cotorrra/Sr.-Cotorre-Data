# Sr.-Cotorre-Data
Repo for the main data for Sr. Cotorre.

Its divided in 4 folders:
Each folder should contain one file per language (es, en, etc.) with the following information:

### Errata
It contains the Erratas: 

- `code`: Its card code in ArkhamDB (i.e 01016 for the .45 Automatic)
- `text`: Its errata text in its frontal side
- `text_back`: Its errata text for the back side (useful for Deckbuilding Options erratas)

### Lang
It contains all the strings that the bot uses to create it's Discord information. (Slash commands descriptions, tags, etc.).

### Taboo
It contains the current (and former) taboo data. Currently, it's based on the ArkhamDB Taboos API response.

### Tarot
It contains the information for the RTCU Tarot Cards.

- `name`: The name of the tarot card
- `up`: Positive Effect
- `down`: Inverted Effect
- `illustrator`: The Illustrator that made this cool art.
- `set`: Set name.
- `number`: The number of the card.
