#!/usr/bin/env python
from Struct import Struct
import struct

class SelfHeader(Struct):
	__endian__ = Struct.BE
	def __format__(self):
		self.magic	= Struct.uint32
		self.headerVer  = Struct.uint32
		self.flags	= Struct.uint16
		self.type	= Struct.uint16
		self.meta	= Struct.uint32
		self.headerSize = Struct.uint64
		self.encryptedSize = Struct.uint64
		self.unknown	= Struct.uint64
		self.AppInfo	= Struct.uint64
		self.elf	= Struct.uint64
		self.phdr	= Struct.unit64
		self.shdr	= Struct.uint64
		self.shdrOffsets = Struct.uint64
		self.sceversion = Struct.uint64
		self.digest	= Struct.uint64
		self.digestSize = Struct.uint64

class AppInfo(Struct):
	__endian__ = Struct.BE
	def __format__(self):
		self.authid	= Struct.uint64
		self.unknown	= Struct.uint32
		self.appType	= Struct.uint32
		self.appVersion = Struct.uint64

class phdrOffsets(Struct):
	__endian__ = Struct.BE
	def __format__(self):
		self.offset	= Struct.uint64
		self.size	= Struct.uint64
		self.unk1	= Struct.uint32
		self.unk2	= Struct.uint32
		self.unk3	= Struct.uint32
		self.unk4	= Struct.uint32

class Digest(Struct):
	__endian__ = Struct.BE
	def __format__(self):
		self.type1		= Struct.uint32
		self.size1		= Struct.uint32
		self.isLast1		= Struct.uint64
		self.magicBits		= Struct.uint8[0x14]
		self.digest		= Struct.uint8[0x14]
		self.padding		= Struct.uint8[0x08]
		self.type2		= Struct.uint32
		self.size2		= Struct.uint32
		self.isLast2		= Struct.uint64
		self.magic 		= Struct.uint32
		self.unk1 		= Struct.uint32
		self.drmType 		= Struct.uint32
		self.unk2		= Struct.uint32
		self.contentID 		= Struct.uint8[0x30]
		self.fileSHA1 		= Struct.uint8[0x10]
		self.notSHA1 		= Struct.uint8[0x10]
		self.notXORKLSHA1 	= Struct.uint8[0x10]
		self.nulls 		= Struct.uint8[0x10]

class Elf64_ehdr(Struct):
	__endian__ = Struct.BE
	def __format__(self):
		self.ident 		= Struct.uint8[16]
		self.type		= Struct.uint16
		self.machine		= Struct.uint16
		self.version		= Struct.uint32
		self.entry		= Struct.uint64
		self.phoff		= Struct.uint64
		self.shoff		= Struct.uint64
		self.flags		= Struct.uint32
		self.ehsize		= Struct.uint16
		self.phentsize		= Struct.uint16
		self.phnum		= Struct.uint16
		self.shentsize		= Struct.uint16
		self.shnum		= Struct.uint16
		self.shstrndx		= Struct.uint16

class Elf64_phdr(Struct):
	__endian__ = Struct.BE
	def __format__(self):
		self.type	= Struct.uint32
		self.flags	= Struct.uint32
		self.offset	= Struct.uint64
		self.vaddr	= Struct.uint64
		self.paddr	= Struct.uint64
		self.filesz	= Struct.uint64
		self.memsz	= Struct.uint64
		self.align	= Struct.uint64


