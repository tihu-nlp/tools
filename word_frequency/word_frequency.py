##
## Copyright 2015 Mostafa Sedaghat Joo
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
##


#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import glob
import operator
import argparse
from collections import Counter
import nltk
from nltk.util import ngrams
import tempfile



class WordCounter(object):

    def Start(self, dname):

        fnames = []

        for f in os.listdir(dname):
            if f.endswith(".txt"):
                with open(dname+os.sep+f, 'r', encoding='utf-8') as r:
                    text = self.RemovePuncs( r.read() )

                    _, t = tempfile.mkstemp()
                    fnames.append(t)
                    with open(t, 'w') as f:
                        f.write(text)


        for i in range(3):
            r = nltk.FreqDist()
            for f in fnames:
                r.update(self.Process(f, i+1))

            print("Dumping result for %d-gram" % (i+1))

            self.DumpFreq('frquency_'+str(i+1), r)



    def Process(self, filename, ngram):

        print("procesing %s for %d-gram occurannces..." % (filename, ngram))

        with open(filename, 'r', encoding='utf-8') as r:
            corpus = r.read()
            tokens = nltk.word_tokenize(corpus)
            return nltk.FreqDist(nltk.ngrams(tokens, ngram))



    def DumpFreq(self, filename, fdist):
        with open(filename, 'w', encoding='utf-8') as w:

            # first 100 000
            for k,v in fdist.most_common(100000):
                w.write('%s\t%d\n'% (" ".join(k), v))


    # https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string
    def RemovePuncs(self, source):
        if source is None:
            return

        #replcae punctuations
        puncs = [u'+', u'-', u'_', u':', u'"', u'\'',u'!', u'.', u';', u';', \
                 u'?', u',', u')', u'(', u'؛', u'؛', u'؟', u'،', u'«', u'»', \
                 u'*', u'&', u'[', u']', u'/', u'-', u'o', u'>', u'<', u'_', \
                 u'%', u'&', u'&', u' ', u'@', u'•', u'–', u'\\']

        for ch in puncs:
            source = source.replace(ch, ' ')

        return source



directory = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Directory of text files")
args = parser.parse_args()

wc = WordCounter()
wc.Start(directory)




