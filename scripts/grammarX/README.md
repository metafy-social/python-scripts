# GrammarX

GrammarX is a python tool which is check grammar mistakes from input file (i.e. whatever written in `demo.txt` ) as well as it will suggest possible fix to it.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [language-tool-python](https://pypi.org/project/language-tool-python/).

```bash
pip install language-tool-python
```

## Usage
- Any input text you want to check you can put in `demo.txt` file
- In terminal run this command
```python
python3 tool.py
```

## Output
- Step 1 : Run This command in terminal
```
python3 tool.py
```
- Step 2 : You will see this output, this is the original text
```
******************************************************************************************
Original Text
******************************************************************************************
another big problem in the speech analytics space.
When customers first bring the software on,
is that they they are blown away by the fact that an engine can monitor hundreds of Kpis.
Right? Everything from my new compliance issues to, you know,
human human interaction, empathy measurements to upsell aptitude to closing aptitude.
They're hundreds literally of Kpis that one could look at. And the speech analytics
companies have typically gone to the customer and really bang that trump. We'll get all
of these things that we're gonna help you keep an eye on. The reality, however, is that
a company even a contact center manager, they can't keep track in their brain even if
they have a report in front of. Of that many Kpis. Mh. And frankly, it's overwhelming.
So what successful companies do is they bite off no more than they can chew at any given time.
The reality is is you can only train a call center agent on a maximum of three skills at any given day. Right?
And by focusing on focusing on problem areas, for a week for a month depending on how bad things are.
And then once you've mastered that skill to take a baseline of of your performance and move on to the next worst skill.
Right, is the way that companies succeed using this product?
```
- Step 3: Grammar mistakes & Imporvements
```
******************************************************************************************
Grammar mistakes & Improvements
******************************************************************************************
This sentence does not start with an uppercase letter. => another big problem in the speech analytics space.
Suggestion : Another
Possible typo: you repeated a word => When customers first bring the software on,
is that they they are blown away by the fact that an engine can monitor hundreds of Kpis.
Suggestion : they
Possible spelling mistake found. => When customers first bring the software on,
is that they they are blown away by the fact that an engine can monitor hundreds of Kpis.
Suggestion : KPIs
Possible typo: you repeated a word => Everything from my new compliance issues to, you know,
human human interaction, empathy measurements to upsell aptitude to closing aptitude.
Suggestion : human
Possible spelling mistake found. => They're hundreds literally of Kpis that one could look at.
Suggestion : KPIs
The word ‘gonna’ is informal. => We'll get all
of these things that we're gonna help you keep an eye on.
Suggestion : going to
Possible spelling mistake found. => Of that many Kpis.
Suggestion : KPIs
Possible spelling mistake found. => Mh.
Suggestion : MH
Possible typo: you repeated a word => The reality is is you can only train a call center agent on a maximum of three skills at any given day.
Suggestion : is
This phrase is duplicated. You should probably use “focusing on” only once. => And by focusing on focusing on problem areas, for a week for a month depending on how bad things are.
Suggestion : focusing on
Possible typo: you repeated a word => And then once you've mastered that skill to take a baseline of of your performance and move on to the next worst skill.
Suggestion : of
```
- Step 4 : This is corrected step
```
******************************************************************************************
CORRECTED TEXT
******************************************************************************************
Another big problem in the speech analytics space.
When customers first bring the software on,
is that they are blown away by the fact that an engine can monitor hundreds of KPIs.
Right? Everything from my new compliance issues to, you know,
human interaction, empathy measurements to upsell aptitude to closing aptitude.
They're hundreds literally of KPIs that one could look at. And the speech analytics
companies have typically gone to the customer and really bang that trump. We'll get all
of these things that we're going to help you keep an eye on. The reality, however, is that
a company even a contact center manager, they can't keep track in their brain even if
they have a report in front of. Of that many KPIs. MH. And frankly, it's overwhelming.
So what successful companies do is they bite off no more than they can chew at any given time.
The reality is you can only train a call center agent on a maximum of three skills at any given day. Right?
And by focusing on problem areas, for a week for a month depending on how bad things are.
And then once you've mastered that skill to take a baseline of your performance and move on to the next worst skill.
Right, is the way that companies succeed using this product?
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
