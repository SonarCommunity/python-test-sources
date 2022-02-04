#!/usr/bin/env python
# Copyright (C) 2006-2007 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#
#


from .namespaces import MANIFESTNS
from .element import Element

# Autogenerated


def Manifest(**args):
    return Element(qname=(MANIFESTNS,'manifest'), **args)


def FileEntry(**args):
    return Element(qname=(MANIFESTNS,'file-entry'), **args)


def EncryptionData(**args):
    return Element(qname=(MANIFESTNS,'encryption-data'), **args)


def Algorithm(**args):
    return Element(qname=(MANIFESTNS,'algorithm'), **args)


def KeyDerivation(**args):
    return Element(qname=(MANIFESTNS,'key-derivation'), **args)
