"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    def __init__(self, hypos, mixes):
        """Initialize self.

        hypos: sequence of string bowl IDs
        mixes: one dict with bowl mixture per bowl ID
        """
        super().__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()
        self.mixes = dict(mixes)

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
        like = mix[data]
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']
    mixes = {
        hypos[0] : dict(vanilla=0.75, chocolate=0.25),
        hypos[1] : dict(vanilla=0.5, chocolate=0.5),
        }

    pmf = Cookie(hypos, mixes)

    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print("{} {:.2f}".format(hypo, prob))


if __name__ == '__main__':
    main()
