Input file:  A list of Rubik's Cube algorithms in a text file.
Output file:  A list of each algorithm's inverse (in order)


I had hoped to use this to verify that for each alg in my list of 200,000 algs for No Parity Pochmann, the 
inverse of the alg is ALSO in the list.  But I forgot (as usual!) that the algs are confounded by subtle differences
in turn order. For instance, the output list (of inverses) might have an alg containing the turns L R'.
But the matching alg in the original list might, by chance, list those 2 turns in the functionally 
equivalent (and opposite) way:  R' L.

This problem is not overwhelming.  I would need to standardize turn order, and convert each alg to a standard notation
before searching for matches.  But it is beyond today's scope.

For now, the app at least does generate a list of inverses.