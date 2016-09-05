# nzdigitalresearch
Script for harvesting information from nzdigital, given a set of scopusIDs

To run this you'll need:

- A Digital NZ API key http://www.digitalnz.org/developers
- Lucy-Janes' script for getting results out of scopus https://github.com/ljewalsh/SCOPUS-Citation-Gatherer

Once you have a set of results from Lucy-Jane's script, you can run it through this one, and it will look for items with the same handles.  Both sets of results will have the SCOPUS-ID, so you can stitch them together using an RDBMS of your choosing.  Or some python.  Whatever.

anton.angelo@canterbury.ac.nz 5/9/2016

