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
**This is only tested on Ubuntu systems**


##### Python
Python3.6 comes with Ubuntu 17.10 and later. Check that you have it by typing

`
python3 --version
`

into a terminal window.

If it does not exist, run the following commands to install it

`
sudo apt-get update

sudo apt-get install python3
`
##### Repository
Clone this repository by typing the following command into your terminal

`
git clone git@github.com:gcooper120/EasyFlashcards.git
`

This creates a new EasyFlashcards directory. Switch to this directory by typing

`
cd EasyFlashcards
`

##### Anki
Download the [Anki Flashcards](https://apps.ankiweb.net/) app.

Next you will be installing this [Anki Add-on](https://ankiweb.net/shared/info/2055492159)
that allows code to modify the app.

Click on the tools heading, and then Add-ons.

Click Get Add-ons on the right hand side and enter the code found at the
above link: 2055492159

Restart Anki

##### Google Credentials

In order for the application to interact with Google Sheets, the Sheets API
must be enabled. Follow Step 1 and 2 [here](https://developers.google.com/sheets/api/quickstart/python)

##### Google Sheets
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
Coming soon.
