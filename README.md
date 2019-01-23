# Tool for creating vocabulary cards in Anki from a Google Sheet

### What is EasyFlashcard?

Recently I have found myself reading more and more texts in foreign languages.
At first, I was writing unfamiliar words down on paper, and later looking up
translations. Although writing certainly has benefits when it comes to
language acquisition, I wanted to find a more efficient way to learn vocabulary.

This brought me to Google Sheets, where I created a simple spreadsheet that I
inserted unfamiliar words into, and the neighboring column produced the English
translation. A great first step.

Finally, I wanted to automatically generate flashcards based on the vocabulary
that I inserted into this sheet.

EasyFlashcards does just that.

### Installation

### Setup

The application currently relies on a very specific Google Sheets format.
Download the following sheet to your own drive:
https://docs.google.com/spreadsheets/d/18i2KqK-969L5zePuj8YnVGZhKewFiql2Z7v13UpA1Ck/edit?usp=sharing

Once the sheet is in your drive, navigate to it and copy the URL. Paste this
URL in the SHEET section of the config.properties file.

Feel free to remove the sample vocabulary words from the sheet.

### Usage

The application parses the sheet and creates flashcards for all new words
in a single sweep. During a study session, add words to the foreign language
column. After the study session, a few steps must be taken to create the
flashcards:
1. Open the Anki Application
2. Navigate to the EasyFlashcards directory and run the following:`
  `
  python3 EasyFlashcards.py
  `
3. Study your new flashcards in Anki
### How to contribute
