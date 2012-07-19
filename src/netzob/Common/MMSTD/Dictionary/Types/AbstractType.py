# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports                                                  |
#+---------------------------------------------------------------------------+
from abc import abstractmethod
from gettext import gettext as _
import logging
import random

#+---------------------------------------------------------------------------+
#| Related third party imports                                               |
#+---------------------------------------------------------------------------+


#+---------------------------------------------------------------------------+
#| Local application imports                                                 |
#+---------------------------------------------------------------------------+


class AbstractType():
    """AbstractType:
            It defines the type of a variable.
    """

    def __init__(self, atomicSize):
        """Constructor of AbstractType:
                @type atomicSize: integer
                @param atomicSize: the size of an element of this type in bits. 1 for bits, 8 for bytes.
        """
        self.log = logging.getLogger('netzob.Common.MMSTD.Dictionary.Type.AbstractType.py')
        self.atomicSize = atomicSize

    def generateRandomString(self, stringType, minSize, maxSize):
        """generateRandomString:
                Generate a random string of the given size withen the given min and max size.

                @type stringType: integer
                @param stringType: a string type as string.digits, string.letters, string.printable...
                @type minSize: integer
                @param minSize: the minimum size of the generated string.
                @type maxSize: integer
                @param maxSize: the maximum size of the generated string.
                @rtype: string
                @return: the randomly generated string.
        """
        size = random.randint(minSize, maxSize)
        value = ""
        for i in range(size):
            value = value + random.choice(stringType)
        return value

    @abstractmethod
    def generateValue(self, generationStrategy, minSize, maxSize):
        """generateValue:
                Generate a bit array value according to the generationStrategy specification and which size is between minSize and maxSize.

                @type generationStrategy: string
                @param generationStrategy: a strategy ("random" for instance) that defines the way the value will be generated.
                @type minSize: integer
                @param minSize: the minimum size of the value in bits.
                @type maxSize: integer
                @param maxSize: the maximum size of the value in bits.
                @rtype: bitarray
                @return: the generated value.
        """
        raise NotImplementedError(_("The current type does not implement 'generateValue'."))

    @abstractmethod
    def type2bin(self, typeValue):
        """type2bin:
                Transform a type value (string for a word, integer for a number...) in a binary value.

                @type typeValue: linked to the instance of Type.
                @param typeValue: the original value in the authentic type format.
                @rtype: bitarray
                @return: the value in binary format.
        """
        raise NotImplementedError(_("The current type does not implement 'type2bin'."))

#+---------------------------------------------------------------------------+
#| Getters and setters                                                       |
#+---------------------------------------------------------------------------+
    def getAtomicSize(self):
        return self.atomicSize
