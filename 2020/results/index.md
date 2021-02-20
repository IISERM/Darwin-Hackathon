# Organisers note
I really hope you all enjoyed the Hackathon.
This was my first hackathon and I really wasn't
expecting such a big turn-up. There were a few
mistakes in the questions which I apologise for.
However, I hope that you'll learnt something new
in this event, and understood how things which
we can solve so easily in our heads are not so
easy to write down as an algorithm. I hope that
you all keep searching for questions, and keep
coding.

Thanks,
Dhruva.

---
# Solutions and Results

## Q1. BP Counting
Use `str.count(char)`

## Q2. Protein Making
For RNA use `str.replace(char1, char2)`. Remember that template strand is given.

For Protein, use
```python
s = "..."
l=[]
dict = {"...":"..."}
for i in range(0, len(s), 3)
    l.append(dict[s[i, i+3]])
print("-".join(l))
```

## Q3. Evolution.
This question was long, and requires a thought
process similar to what one needs in a
production software. The vast number of
variables requires a modular system to
efficiently code and maintain.

You can view my implementation of it [here](https://github.com/DhruvaSambrani/Evolution-Simulation/)

## Q4. Viral Relatedness.
This was an extremely difficult question, compared to the others.
This is a well-known problem called Levenstein distance, or edit-distance, and is commonly used in auto correct.
It is also a common problem in what is known as Dynamic Programming (a nice tutorial [here](https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/)).
The solution to this problem can be found [here](https://www.geeksforgeeks.org/edit-distance-dp-5/).

## Q5. File handling and plotting
This was a relativly simple code. You just had to read the csv and plot accordingly.
To facilitate easy time handling, computers use
[Unix Timestamps](https://www.unixtimestamp.com/).

You had to convert each reading into a unix timestamp and simply subtract from the first reading and plot accordingly. Ideally, of course, you should subtract it from the start of the session time, but no points are deducted if done otherwise.

Species were supposed to be counted only once.
Hamas Team has a clean implementation of it.

## Q6. Bird call
This question was actually an experimental
question. It arose from an idea of trying to
define a bird call as a path in a hyperspace of
some component subcalls and time. If then a
sample call was converted to a path, id-ing the
bird may be more efficient than using a CNN or
DL on a spectrograph, as it is usually done.
If someone is still interested in this, they
may want to look up Principle Component
Analysis, which does exactly this. I have not
researched enough about people using it on audio
identification, but [Lia Medeiros](https://www.ias.edu/scholars/lia-medeiros)
works on using PCA on Black hole images to
study them further.
Paper
- [DOI:	10.3847/1538-4357/aad37a](https://iopscience.iop.org/article/10.3847/1538-4357/aad37a)
- [arXiv:1804.05903](https://arxiv.org/abs/1804.05903)

There were a few problems with this question
though. The `5-10% not sure` was necessary as
differences are not transitive. But I forgot
that during the event and asked you all to
ignore that. That is also why the points for
this question were so much higher than the
rest. The solution to Evolution was practically
laid out, and Levenstein distance could
potentially be searched online.

---

# [Participant's codes with my comments and Results]()
- [_Assassins.zip_](Assassins.zip)
- [_DWH - J.A.R.V.I.S.zip_](DWH%20-%20J.A.R.V.I.S.zip)
- [_Gowri_didn't_do_anything.zip_](Gowri_didn't_do_anything.zip)
- [_Hamas_Darwin_Hackathon.zip_](Hamas_Darwin_Hackathon.zip)
- [_League of 69.zip_](League%20of%2069.zip)
- [_Madhu-Vini.zip_](Madhu-Vini.zip)
- [_Results.xlsx_](Results.xlsx)
