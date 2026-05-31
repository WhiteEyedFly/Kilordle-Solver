Goal: Find a solution to Kilordle that takes just 30 words
I approached this problem in a huge variety of ways which I'll attempt to better document here.

kilordle.py
First I made 2 greedy algorithms. These were both based on the idea that we would choose a starting word for the cover and then loop through the list of acceptable words to find the best one to 
add given the coverage we had already. I did this by selecting the word that maximise the "number of letter positions that haven't already been covered".

kilordleInitialSolver.py
This was an exhaustive algorithm. It started with a maxCover (the list of all acceptable words) and stripped away one word at a time, checking if it remained a valid cover. 
If so, remove another word, and check again, if not, record the minimum cover found and backtrack to rermove a different word.
This finds all possible local minimum covers and, thus, the true minimum cover but does so extremely inefficiently, to the point it could never truly finish running

kilordleSemiSolver.py
This algorithm randomly added words to a solution until a cover was made. It then chained into itself, selecting random words from itself until a new, smaller cover was made.
It then repeats, prioritising words that appear in minimal covers most often until it simplifies down.
This would obviously never get a real optimal solution but it performed surprisingly well with the right parameters.

kilordleSuperSolver.py
This was another exhaustive algorithm from a vastly more efficient method. Instead of looping over all possible words, it: 
Found the number of times each letter appeared in each position
Found the minimum, non-zero such letter position and found the first word in the wordlist that covered that position
It then recalculated all of the letter positions (setting any letterposition covered by the added word to 0) and repeated this process until it found a minimal cover
Then, it backtracked through every choice to find every local minimal cover (and, thus, the true minimum)
This was more efficient than kilordleInitialSolver.py by an amount that is hard to conceptualise but still not efficient enough to run feasibly on a PC

kilordleJointSolver.py
This used an exhaustive algorithm to find a good start point, then a greedy algorithm to fill in the rest of the cover (to speed up the exhaustive aspect and reduce the greedy bias).
This actually underperformed compared to my other greedy algorithms however

betterWord.py
This was another greedy algorithm with a little more thought put in.

D&C.py
This was another attempt to speed up an exhaustive algorithm by reducing it into smaller problems that could be finished far quicker.
It would split the word list into sublists into sublists etc until each sublist was one word. A minimal cover of one word is obviously just the word itself.
It would then rejoin the lists and, at each step, find the minimal cover of those sublists until it built a cover of the lsit as a whole.
Unfortunately "x is a minimum cover of a and y is a minimum cover of b" does not necessarily mean that a minimum cover of a+b can be made using x and y so this failed to create a true minimum.

zeroingIn.py
We chose an initial good word, restricted the wordlist based on what words that word covered, found the next best word to add based on the restricted list and repeated.

satSolver.py & satSolver2.py
These were my attempts to build a SAT Solver by hand after realising I could phrase the problem as a linear programming problem and, whilst they worked, 
they unfortunately kept getting stuck in local maxima and I'm unsure as to how to fix that problem.

SATSolver.py
I then used orTools' cpModel() SAT Solver and found an optimal solution