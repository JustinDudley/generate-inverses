Input file:  A list of Rubik's Cube algorithms in a text file.
Output file:  A list of each algorithm's inverse (in order)


I had hoped to use this to verify that for each alg in my list of 200,000 algs for No Parity Pochmann, the 
inverse of the alg is ALSO in the list.  But I forgot (as usual!) that the algs are confounded by subtle differences
in turn order. For instance, the output list (of inverses) might have an alg containing the turns L R'.
But the matching alg in the original list might, by chance, list those 2 turns in the functionally 
equivalent (and opposite) way:  R' L.

This problem could be solved, and is not overwhelming.  I would need to standardize turn order, and convert each 
alg to a standard notation before searching for matches.  But it is beyond today's scope.

For now, the app at least does generate a list of inverses.


Whew -- I had a scare there. Forgetting everything I had written above, I thought that id 32 was incomplete. But I went 
through id 32:  When I generated the inverse of EACH alg in the filtered list, I
found that every single one was already in the list, as expected. But there were the same issues:  D Y' == Y' D, for instance.
So I had to look closely.