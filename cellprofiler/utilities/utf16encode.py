'''utf16encode.py - encode unicode strings as escaped utf16

CellProfiler is distributed under the GNU General Public License,
but this file is licensed under the more permissive BSD license.
See the accompanying file LICENSE for details.

Copyright (c) 2003-2009 Massachusetts Institute of Technology
Copyright (c) 2009-2013 Broad Institute
All rights reserved.

Please see the AUTHORS file for credits.

Website: http://www.cellprofiler.org
'''

def utf16encode(x):
    '''Encode a unicode string in 7-bit US ascii
    
    x - unicode string to be encoded
    
    returns utf8-escape-encoded string
    
    The escapes:

    \ (backslash) -> \\
    
    0x20 <= c < 0xff -> c
    
    all others -> \u####
    '''
    y = ''
    for z in x:
        t = ord(z)
        if t < 0x20 or t >= 0x7f:
            y += "\\u%04x" % t
        elif z == "\\":
            y += "\\\\"
        else:
            y += str(z)
    return y

def utf16decode(x):
    '''Decode an escaped utf8-encoded string
    '''
    y = u""
    state = -1
    for z in x:
        if state == -1:
            if z == "\\":
                state = 0
            else:
                y += unicode(z)
        elif state == 0:
            if z == "u":
                state = 1
                acc = ""
            else:
                y += unicode(z)
                state = -1
        elif state < 4:
            state += 1
            acc += z
        else:
            state = -1
            y += unichr(int(acc+z, 16))
    return y
