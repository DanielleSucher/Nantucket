### On the structure of a limericks

Limericks have a fairly loose form. The rhyme scheme and syllable count is typically something like this:

 > A (7, 8 or 9 syllables*) 
 > A (7, 8 or 9) 
 > B (5 or 6) 
 > B (5 or 6) 
 > A (7, 8 or 9)

And as if that weren't loosey-goosey enough, they can have either anapaestic meter (duh-duh-DUM, duh-duh-DUM) or amphibrachic meter (duh-DUM-duh, duh-DUM-duh)!

So, I chose an old favorite as the canonical example to work from when building this limerick detector:

## God in the Quad
by Ronald Knox

> There was a young man who said "God
> Must find it exceedingly odd
> To think that the tree
> Should continue to be
> When there's no one about in the quad."

> "Dear Sir: Your astonishment's odd;
> I am always about in the quad.
> And that's why the tree
> Will continue to be
> Since observed by, Yours faithfully, God."

It has a strange rhyme scheme for a limerick, in that not all the A lines have the same syllable count, and the 
B lines also differ from each other. But it flows so beautifully that I couldn't quite resist!

So, we're looking for limericks with the following structure, because if it was good enough for Richard Knox, it's good enough for us:

 > A (8)
 > A (8)
 > B (5)
 > B (6) 
 > A (9)

> duh DUM duh duh DUM duh duh DUM
> duh DUM duh duh DUM duh duh DUM
> duh DUM duh duh DUM 
> duh DUM duh duh duh DUM 
> duh duh DUM duh duh DUM duh duh DUM


### How to use

Written with Python 2.7.2, using the awesome nltk library and its CMU pronunciation dictionary. 

pip install numpy
pip install nltk

To get the CMU dictionary (which is critical):
python
import nltk
nltk.download()
d
cmudict

Once you have all that... well, I'll tell you what to do once there's something to do. This is in-progress for now, sorry!