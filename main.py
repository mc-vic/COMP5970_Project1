import sys
import hashlib

# ELF header parser

# scan for magic numbers (0x7f 45 4c 46, offset 0x00, 4 bytes)

# check to see if it is 32 or 64 bit (offset 0x04, 1 byte)
# if it is set to 1 -> 32 bit
# if 2 -> 64 bit

# check for endianness (offset 0x05, 1 byte)
# if it is set to 1 -> it is little Endian
# #if it is 2 -> it is big Endian


#def main():
#parse()


def parse():
    with open('gold', 'rb') as f:
        header = f.read(52)
        #lines = f.readlines()

        #print(f.read(52))

        # 32 bit
        #4
        #Class = f.seek(4)
        f.seek(4)
        Class = int.from_bytes(f.read(1), 'little')

            #(header(1), "little")
        #print(str(Class))

        f.seek(5)
        Data = int.from_bytes(f.read(1), "little")

        if Class == 1:
            #little endian
            print("Class is 32-bit architecture")
            if Data == 1:
                print("Data is little Endian")
                # little endian

                f.seek(0, 0)
                Magic = (f.read(4), "little")
                print("Magic Numbers are " + str(Magic))

                f.seek(6)
                Version = int.from_bytes(f.read(1), "little")
                if Version != 1:
                    sys.exit("Version is not 1, invalid")

                f.seek(7)
                OSABI = int.from_bytes(f.read(1), "little")
                if OSABI == 0:
                    print("OSABI is System V")
                if OSABI == 1:
                    print("OSABI is HP-UX")
                if OSABI == 2:
                    print("OSABI is NetBSD")
                if OSABI == 3:
                    print("OSABI is Linux")
                if OSABI == 4:
                    print("OSABI is GNU Hurd")
                if OSABI == 6:
                    print("OSABI is Solaris")
                if OSABI == 7:
                    print("OSABI is AIX (Monterey)")
                if OSABI == 8:
                    print("OSABI is IRIX")
                if OSABI == 9:
                    print("OSABI is Free BSD")
                if OSABI == 10:
                    print("OSABI is Tru64")
                if OSABI == 11:
                    print("OSABI is Novell Modestro")
                if OSABI == 13:
                    print("OSABI is OpenBSD")
                if OSABI == 14:
                    print("OSABI is NonStop Kernel")
                if OSABI == 15:
                    print("OSABI is AROS")
                if OSABI == 16:
                    print("OSABI is FenixOS")
                if OSABI == 17:
                    print("OSABI is Nuxi CloudABI")
                if OSABI == 18:
                    print("OSABI is Stratus Technologies OpenVOS")
                else:
                    sys.exit("OSABI error")

                f.seek(8)
                ABIversion = int.from_bytes(f.read(1), "little")
                print("ABI Version is " + str(ABIversion))

                f.seek(9)
                Pad = int.from_bytes(f.read(7), "little")

                f.seek(16)
                Type = int.from_bytes(f.read(2), "little")
                if Type == 0:
                    print("File Type is NONE")
                if Type == 1:
                    print("File Type is REL")
                if Type == 2:
                    print("File Type is EXEC")
                if Type == 3:
                    print("File Type is DYN")
                if Type == 4:
                    print("File Type is CORE")
                if Type == 65024:
                    print("File Type is LOOS")
                if Type == 65279:
                    print("File Type is HIOS")
                if Type == 65280:
                    print("File Type is LOPROC")
                if Type == 65535:
                    print("File Type is HIPROC")
                else:
                    sys.exit("File Type error")

                f.seek(18)
                Machine = int.from_bytes(f.read(2), "little")

                if Machine == 0:
                    print("No specific machine instructions")

                if Machine == 1:
                    print("Machine instructions are AT&T WE 32100")

                if Machine == 2:
                    print("Machine instructions are SPARC")

                if Machine == 3:
                    print("Machine instructions are x86")

                if Machine == 4:
                    print("Machine instructions are Motorola 6800 (M68k)")

                if Machine == 5:
                    print("Machine instructions are Motorola 8800 (M88k)")

                if Machine == 6:
                    print("Machine instructions are MCU")

                if Machine == 7:
                    print("Machine instructions are Intel 80860")

                if Machine == 8:
                    print("Machine instructions are MIPS")

                if Machine == 9:
                    print("Machine instructions are IBM System/370")

                if Machine == 10:
                    print("Machine instructions are MIPS RS3000 Little-Endian")

                if Machine == 11:
                    print("Machine instructions are reserved for future use")

                if Machine == 12:
                    print("Machine instructions are reserved for future use")

                if Machine == 13:
                    print("Machine instructions are reserved for future use")

                if Machine == 14:
                    print("Machine instructions are Hewlett-Packard PA-RISC")

                if Machine == 15:
                    print("Machine instructions are reserved for future use")

                if Machine == 16:
                    print("Machine instructions are Intel 80960")

                if Machine == 17:
                    print("Machine instructions are Power PC")

                if Machine == 18:
                    print("Machine instructions are Power PC (64-bit)")

                if Machine == 19:
                    print("Machine instructions are S390, including S380x")

                if Machine == 20:
                    print("Machine instructions are IMB SPU/SPC")

                if Machine == 21:
                    print("Machine instructions are reserved for future use")

                if Machine == 22:
                    print("Machine instructions are reserved for future use")

                if Machine == 23:
                    print("Machine instructions are reserved for future use")

                if Machine == 24:
                    print("Machine instructions are reserved for future use")

                if Machine == 25:
                    print("Machine instructions are reserved for future use")

                if Machine == 26:
                    print("Machine instructions are reserved for future use")

                if Machine == 27:
                    print("Machine instructions are reserved for future use")

                if Machine == 28:
                    print("Machine instructions are reserved for future use")

                if Machine == 29:
                    print("Machine instructions are reserved for future use")

                if Machine == 30:
                    print("Machine instructions are reserved for future use")

                if Machine == 31:
                    print("Machine instructions are reserved for future use")

                if Machine == 32:
                    print("Machine instructions are reserved for future use")

                if Machine == 33:
                    print("Machine instructions are reserved for future use")

                if Machine == 34:
                    print("Machine instructions are reserved for future use")

                if Machine == 35:
                    print("Machine instructions are reserved for future use")

                if Machine == 36:
                    print("Machine instructions are NEC V800")

                if Machine == 37:
                    print("Machine instructions are Fujitsu FR20")

                if Machine == 38:
                    print("Machine instructions are TRW RH-32")

                if Machine == 39:
                    print("Machine instructions are Motorola RCE")

                if Machine == 40:
                    print("Machine instructions are ARM (up to Armv7/AArch32)")

                if Machine == 41:
                    print("Machine instructions are Digital Alpha")

                if Machine == 42:
                    print("Machine instructions are Super H")

                if Machine == 43:
                    print("Machine instructions are SPARC Version 9")

                if Machine == 44:
                    print("Machine instructions are Siemens TriCore: Embedded Processor")

                if Machine == 45:
                    print("Machine instructions are Argonaut RISC Core")

                if Machine == 46:
                    print("Machine instructions are Hitachi H3/300")

                if Machine == 47:
                    print("Machine instructions are Hitachi H3/300H")

                if Machine == 48:
                    print("Machine instructions are Hitachi H85")

                if Machine == 49:
                    print("Machine instructions are Hitachi H8/500")

                if Machine == 50:
                    print("Machine instructions are IA-64")

                if Machine == 51:
                    print("Machine instructions are Stanford MIPS-X")

                if Machine == 52:
                    print("Machine instructions are Motorola ColdFire")

                if Machine == 53:
                    print("Machine instructions are M68HC12")

                if Machine == 54:
                    print("Machine instructions are Fujitsu MMA Multimedia Accelerator")

                if Machine == 55:
                    print("Machine instructions are Siemens PCP")

                if Machine == 56:
                    print("Machine instructions are Sony nCPU embedded RISC Processor")

                if Machine == 57:
                    print("Machine instructions are Denso NDRI microprocessor")

                if Machine == 58:
                    print("Machine instructions are Motorola Star*Core Processor")

                if Machine == 59:
                    print("Machine instructions are Toyota ME16 Processor")

                if Machine == 60:
                    print("Machine instructions are STMicroelectronics ST100 Processor")

                if Machine == 61:
                    print("Machine instructions are Advanced Logic Crop. Tiny J embedded processor Family")

                if Machine == 62:
                    print("Machine instructions are AMD x86-64")

                if Machine == 63:
                    print("Machine instructions are Sony DSP Processor")

                if Machine == 64:
                    print("Machine instructions are Digital Equipment Corp. PDP-10")

                if Machine == 65:
                    print("Machine instructions are Digital Equipment Corp. PDP-11")

                if Machine == 66:
                    print("Machine instructions are Siemens FX66 Microcontroller")

                if Machine == 67:
                    print("Machine instructions are STMicroelectronics ST9 + 8/16 bit microcontroller")

                if Machine == 68:
                    print("Machine instructions are STMicroelectronics ST7 8-bit microcontroller")

                if Machine == 69:
                    print("Machine instructions are Motorola MC68HC16 microcontroller")

                if Machine == 70:
                    print("Machine instructions are Motorola MC68HC11 microcontroller")

                if Machine == 71:
                    print("Machine instructions are Motorola MC68HC08")

                if Machine == 72:
                    print("Machine instructions are Motorola MC68HC05")

                if Machine == 73:
                    print("Machine instructions are Silicon Graphics SVx")

                if Machine == 74:
                    print("Machine instructions are STMicroelectronics ST19 8-bit microcontroller")

                if Machine == 75:
                    print("Machine instructions are Digital VAX")

                if Machine == 76:
                    print("Machine instructions are Axis Communications 32-bit embedded processor")

                if Machine == 77:
                    print("Machine instructions are Axis Communications 32-bit embedded processor")

                if Machine == 78:
                    print("Machine instructions are Element 14 64-bit DSP processor")

                if Machine == 79:
                    print("Machine instructions are LSI Logic 16-bit DSP processor")

                if Machine == 140:
                    print("Machine instructions are TMS320 C6000 Family")

                if Machine == 175:
                    print("Machine instructions are MCST Elkbrus e2k")

                if Machine == 183:
                    print("Machine instructions are ARM 64-bit (Arm8/AArch64)")

                if Machine == 220:
                    print("Machine instructions are Zilog z80")

                if Machine == 243:
                    print("Machine instructions are RISC -V")

                if Machine == 247:
                    print("Machine instructions are Berkley Packet Filter")

                if Machine == 257:
                    print("Machine instructions are WDC 65C816")

                f.seek(24)
                entry = (f.read(4), "little")
                print("Entry address is " + str(entry))

                f.seek(28)
                phoff = (f.read(4), "little")
                print("Start of program header table is " + str(phoff))

                f.seek(32)
                shoff = (f.read(4), "little")
                print("Start of section header is " + str(shoff))

                f.seek(36)
                flags = int.from_bytes(f.read(4), "little")
                print("Flags are " + str(flags))

                f.seek(40)
                ehsize = int.from_bytes(f.read(2), "little")
                print("The size of this header is " + str(ehsize))

                f.seek(42)
                phentsize = (f.read(2), "little")
                print("Size of the program header table entry is " + str(phentsize))

                f.seek(44)
                phnum = int.from_bytes(f.read(2), "little")
                print("The number of entries in the program header table entry is " + str(phnum))

                f.seek(46)
                shentsize = int.from_bytes(f.read(2), "little")
                print("The size of the section header table entries is " + str(shentsize))

                f.seek(48)
                shnum = int.from_bytes(f.read(2), "little")
                print("The number of entries in the section header table " + str(shnum))

                f.seek(50)
                shstrndx = int.from_bytes(f.read(2), "little")
                print("The index of section header table entry " + str(shstrndx))

            if Data == 2:
                # big endian

                f.seek(0, 0)
                Magic = (f.read(4), "big")
                print("Magic Numbers are " + str(Magic))

                f.seek(4, 0)
                Class = int.from_bytes(f.read(1), "big")
                if Class == 1:
                    print("Class is 32-bit")
                if Class == 2:
                    print("Class is 64-bit")
                else:
                    sys.exit("Error in Class")

                f.seek(5, 0)
                Data = int.from_bytes(f.read(1), "big")

                if Data == 1:
                    print("Data is little Endian")
                    # change everything
                if Data == 2:
                    print("Data is Big Endian")
                else:
                    sys.exit("Error in Endianness  line 454")

                f.seek(6)
                Version = int.from_bytes(f.read(1), "big")
                if Version != 1:
                    sys.exit("Version is not 1, invalid")

                f.seek(7)
                OSABI = int.from_bytes(f.read(1), "big")
                if OSABI == 0:
                    print("OSABI is System V")
                if OSABI == 1:
                    print("OSABI is HP-UX")
                if OSABI == 2:
                    print("OSABI is NetBSD")
                if OSABI == 3:
                    print("OSABI is Linux")
                if OSABI == 4:
                    print("OSABI is GNU Hurd")
                if OSABI == 6:
                    print("OSABI is Solaris")
                if OSABI == 7:
                    print("OSABI is AIX (Monterey)")
                if OSABI == 8:
                    print("OSABI is IRIX")
                if OSABI == 9:
                    print("OSABI is Free BSD")
                if OSABI == 10:
                    print("OSABI is Tru64")
                if OSABI == 11:
                    print("OSABI is Novell Modestro")
                if OSABI == 13:
                    print("OSABI is OpenBSD")
                if OSABI == 14:
                    print("OSABI is NonStop Kernel")
                if OSABI == 15:
                    print("OSABI is AROS")
                if OSABI == 16:
                    print("OSABI is FenixOS")
                if OSABI == 17:
                    print("OSABI is Nuxi CloudABI")
                if OSABI == 18:
                    print("OSABI is Stratus Technologies OpenVOS")
                else:
                    sys.exit("OSABI error")

                f.seek(8)
                ABIversion = int.from_bytes(f.read(1), "big")
                print("ABI Version is " + str(ABIversion))

                f.seek(9)
                Pad = int.from_bytes(f.read(7), "big")

                f.seek(16)
                Type = int.from_bytes(f.read(2), "big")
                if Type == 0:
                    print("File Type is NONE")
                if Type == 1:
                    print("File Type is REL")
                if Type == 2:
                    print("File Type is EXEC")
                if Type == 3:
                    print("File Type is DYN")
                if Type == 4:
                    print("File Type is CORE")
                if Type == 65024:
                    print("File Type is LOOS")
                if Type == 65279:
                    print("File Type is HIOS")
                if Type == 65280:
                    print("File Type is LOPROC")
                if Type == 65535:
                    print("File Type is HIPROC")
                else:
                    sys.exit("File Type error")

                f.seek(18)
                Machine = int.from_bytes(f.read(2), "big")

                if Machine == 0:
                    print("No specific machine instructions")

                if Machine == 1:
                    print("Machine instructions are AT&T WE 32100")

                if Machine == 2:
                    print("Machine instructions are SPARC")

                if Machine == 3:
                    print("Machine instructions are x86")

                if Machine == 4:
                    print("Machine instructions are Motorola 6800 (M68k)")

                if Machine == 5:
                    print("Machine instructions are Motorola 8800 (M88k)")

                if Machine == 6:
                    print("Machine instructions are MCU")

                if Machine == 7:
                    print("Machine instructions are Intel 80860")

                if Machine == 8:
                    print("Machine instructions are MIPS")

                if Machine == 9:
                    print("Machine instructions are IBM System/370")

                if Machine == 10:
                    print("Machine instructions are MIPS RS3000 Little-Endian")

                if Machine == 11:
                    print("Machine instructions are reserved for future use")

                if Machine == 12:
                    print("Machine instructions are reserved for future use")

                if Machine == 13:
                    print("Machine instructions are reserved for future use")

                if Machine == 14:
                    print("Machine instructions are Hewlett-Packard PA-RISC")

                if Machine == 15:
                    print("Machine instructions are reserved for future use")

                if Machine == 16:
                    print("Machine instructions are Intel 80960")

                if Machine == 17:
                    print("Machine instructions are Power PC")

                if Machine == 18:
                    print("Machine instructions are Power PC (64-bit)")

                if Machine == 19:
                    print("Machine instructions are S390, including S380x")

                if Machine == 20:
                    print("Machine instructions are IMB SPU/SPC")

                if Machine == 21:
                    print("Machine instructions are reserved for future use")

                if Machine == 22:
                    print("Machine instructions are reserved for future use")

                if Machine == 23:
                    print("Machine instructions are reserved for future use")

                if Machine == 24:
                    print("Machine instructions are reserved for future use")

                if Machine == 25:
                    print("Machine instructions are reserved for future use")

                if Machine == 26:
                    print("Machine instructions are reserved for future use")

                if Machine == 27:
                    print("Machine instructions are reserved for future use")

                if Machine == 28:
                    print("Machine instructions are reserved for future use")

                if Machine == 29:
                    print("Machine instructions are reserved for future use")

                if Machine == 30:
                    print("Machine instructions are reserved for future use")

                if Machine == 31:
                    print("Machine instructions are reserved for future use")

                if Machine == 32:
                    print("Machine instructions are reserved for future use")

                if Machine == 33:
                    print("Machine instructions are reserved for future use")

                if Machine == 34:
                    print("Machine instructions are reserved for future use")

                if Machine == 35:
                    print("Machine instructions are reserved for future use")

                if Machine == 36:
                    print("Machine instructions are NEC V800")

                if Machine == 37:
                    print("Machine instructions are Fujitsu FR20")

                if Machine == 38:
                    print("Machine instructions are TRW RH-32")

                if Machine == 39:
                    print("Machine instructions are Motorola RCE")

                if Machine == 40:
                    print("Machine instructions are ARM (up to Armv7/AArch32)")

                if Machine == 41:
                    print("Machine instructions are Digital Alpha")

                if Machine == 42:
                    print("Machine instructions are Super H")

                if Machine == 43:
                    print("Machine instructions are SPARC Version 9")

                if Machine == 44:
                    print("Machine instructions are Siemens TriCore: Embedded Processor")

                if Machine == 45:
                    print("Machine instructions are Argonaut RISC Core")

                if Machine == 46:
                    print("Machine instructions are Hitachi H3/300")

                if Machine == 47:
                    print("Machine instructions are Hitachi H3/300H")

                if Machine == 48:
                    print("Machine instructions are Hitachi H85")

                if Machine == 49:
                    print("Machine instructions are Hitachi H8/500")

                if Machine == 50:
                    print("Machine instructions are IA-64")

                if Machine == 51:
                    print("Machine instructions are Stanford MIPS-X")

                if Machine == 52:
                    print("Machine instructions are Motorola ColdFire")

                if Machine == 53:
                    print("Machine instructions are M68HC12")

                if Machine == 54:
                    print("Machine instructions are Fujitsu MMA Multimedia Accelerator")

                if Machine == 55:
                    print("Machine instructions are Siemens PCP")

                if Machine == 56:
                    print("Machine instructions are Sony nCPU embedded RISC Processor")

                if Machine == 57:
                    print("Machine instructions are Denso NDRI microprocessor")

                if Machine == 58:
                    print("Machine instructions are Motorola Star*Core Processor")

                if Machine == 59:
                    print("Machine instructions are Toyota ME16 Processor")

                if Machine == 60:
                    print("Machine instructions are STMicroelectronics ST100 Processor")

                if Machine == 61:
                    print("Machine instructions are Advanced Logic Crop. Tiny J embedded processor Family")

                if Machine == 62:
                    print("Machine instructions are AMD x86-64")

                if Machine == 63:
                    print("Machine instructions are Sony DSP Processor")

                if Machine == 64:
                    print("Machine instructions are Digital Equipment Corp. PDP-10")

                if Machine == 65:
                    print("Machine instructions are Digital Equipment Corp. PDP-11")

                if Machine == 66:
                    print("Machine instructions are Siemens FX66 Microcontroller")

                if Machine == 67:
                    print("Machine instructions are STMicroelectronics ST9 + 8/16 bit microcontroller")

                if Machine == 68:
                    print("Machine instructions are STMicroelectronics ST7 8-bit microcontroller")

                if Machine == 69:
                    print("Machine instructions are Motorola MC68HC16 microcontroller")

                if Machine == 70:
                    print("Machine instructions are Motorola MC68HC11 microcontroller")

                if Machine == 71:
                    print("Machine instructions are Motorola MC68HC08")

                if Machine == 72:
                    print("Machine instructions are Motorola MC68HC05")

                if Machine == 73:
                    print("Machine instructions are Silicon Graphics SVx")

                if Machine == 74:
                    print("Machine instructions are STMicroelectronics ST19 8-bit microcontroller")

                if Machine == 75:
                    print("Machine instructions are Digital VAX")

                if Machine == 76:
                    print("Machine instructions are Axis Communications 32-bit embedded processor")

                if Machine == 77:
                    print("Machine instructions are Axis Communications 32-bit embedded processor")

                if Machine == 78:
                    print("Machine instructions are Element 14 64-bit DSP processor")

                if Machine == 79:
                    print("Machine instructions are LSI Logic 16-bit DSP processor")

                if Machine == 140:
                    print("Machine instructions are TMS320 C6000 Family")

                if Machine == 175:
                    print("Machine instructions are MCST Elkbrus e2k")

                if Machine == 183:
                    print("Machine instructions are ARM 64-bit (Arm8/AArch64)")

                if Machine == 220:
                    print("Machine instructions are Zilog z80")

                if Machine == 243:
                    print("Machine instructions are RISC -V")

                if Machine == 247:
                    print("Machine instructions are Berkley Packet Filter")

                if Machine == 257:
                    print("Machine instructions are WDC 65C816")

                print("The data is big Endian")

                f.seek(20)
                entry = (f.read(4), "big")
                print("Entry address is " + str(entry))

                f.seek(28)
                phoff = int.from_bytes(f.read(4), "big")
                print("Start of program header table is " + str(phoff))

                f.seek(32)
                shoff = int.from_bytes(f.read(4), "big")
                print("Start of section header is " + str(shoff))

                f.seek(36)
                flags = int.from_bytes(f.read(4), "big")
                print("Flags are " + str(flags))

                f.seek(40)
                ehsize = int.from_bytes(f.read(2), "big")
                print("The size of this header is " + str(ehsize))

                f.seek(42)
                phentsize = int.from_bytes(f.read(2), "big")
                print("Size of the program header table entry is " + str(phentsize))

                f.seek(44)
                phnum = int.from_bytes(f.read(2), "big")
                print("The number of entries in the program header table entry is " + str(phnum))

                f.seek(46)
                shentsize = int.from_bytes(f.read(2), "big")
                print("The size of the section header table entries is " + str(shentsize))

                f.seek(48)
                shnum = int.from_bytes(f.read(2), "big")
                print("The number of entries in the section header table " + str(shnum))

                f.seek(50)
                shstrndx = int.from_bytes(f.read(2), "big")
                print("The index of section header table entry " + str(shstrndx))

        if Class == 2:
            # 64 bit architecture
            # little

            f.seek(0, 0)
            Magic = (f.read(4), "little")
            print("Magic Numbers are " + str(Magic))

            f.seek(4, 0)
            Class = int.from_bytes(f.read(1), "little")
            if Class == 1:
                print("Class is 32-bit")
            if Class == 2:
                print("Class is 64-bit")
            else:
                sys.exit("Error in Class")

            f.seek(5, 0)
            Data = int.from_bytes(f.read(1), "little")
            if Data == 1:
                print("Data is little Endian")
                # change everything
            if Data == 2:
                print("Data is Big Endian")
            if(Data != 1 & Data != 2):
                sys.exit("Data is " + str(Data) + " Error in Endianness line 861")

            f.seek(6)
            Version = int.from_bytes(f.read(1), "little")
            if Version != 1:
                sys.exit("Version is not 1, invalid")

            f.seek(7)
            OSABI = int.from_bytes(f.read(1), "little")
            if OSABI == 0:
                print("OSABI is System V")
            if OSABI == 1:
                print("OSABI is HP-UX")
            if OSABI == 2:
                print("OSABI is NetBSD")
            if OSABI == 3:
                print("OSABI is Linux")
            if OSABI == 4:
                print("OSABI is GNU Hurd")
            if OSABI == 6:
                print("OSABI is Solaris")
            if OSABI == 7:
                print("OSABI is AIX (Monterey)")
            if OSABI == 8:
                print("OSABI is IRIX")
            if OSABI == 9:
                print("OSABI is Free BSD")
            if OSABI == 10:
                print("OSABI is Tru64")
            if OSABI == 11:
                print("OSABI is Novell Modestro")
            if OSABI == 13:
                print("OSABI is OpenBSD")
            if OSABI == 14:
                print("OSABI is NonStop Kernel")
            if OSABI == 15:
                print("OSABI is AROS")
            if OSABI == 16:
                print("OSABI is FenixOS")
            if OSABI == 17:
                print("OSABI is Nuxi CloudABI")
            if OSABI == 18:
                print("OSABI is Stratus Technologies OpenVOS")


            f.seek(8)
            ABIversion = int.from_bytes(f.read(1), "little")
            print("ABI Version is " + str(ABIversion))

            f.seek(9)
            Pad = int.from_bytes(f.read(7), "little")

            f.seek(16)
            Type = int.from_bytes(f.read(2), "little")
            if Type == 0:
                print("File Type is NONE")
            if Type == 1:
                print("File Type is REL")
            if Type == 2:
                print("File Type is EXEC")
            if Type == 3:
                print("File Type is DYN")
            if Type == 4:
                print("File Type is CORE")
            if Type == 65024:
                print("File Type is LOOS")
            if Type == 65279:
                print("File Type is HIOS")
            if Type == 65280:
                print("File Type is LOPROC")
            if Type == 65535:
                print("File Type is HIPROC")

            f.seek(18)
            Machine = int.from_bytes(f.read(2), "little")

            if Machine == 0:
                print("No specific machine instructions")

            if Machine == 1:
                print("Machine instructions are AT&T WE 32100")

            if Machine == 2:
                print("Machine instructions are SPARC")

            if Machine == 3:
                print("Machine instructions are x86")

            if Machine == 4:
                print("Machine instructions are Motorola 6800 (M68k)")

            if Machine == 5:
                print("Machine instructions are Motorola 8800 (M88k)")

            if Machine == 6:
                print("Machine instructions are MCU")

            if Machine == 7:
                print("Machine instructions are Intel 80860")

            if Machine == 8:
                print("Machine instructions are MIPS")

            if Machine == 9:
                print("Machine instructions are IBM System/370")

            if Machine == 10:
                print("Machine instructions are MIPS RS3000 Little-Endian")

            if Machine == 11:
                print("Machine instructions are reserved for future use")

            if Machine == 12:
                print("Machine instructions are reserved for future use")

            if Machine == 13:
                print("Machine instructions are reserved for future use")

            if Machine == 14:
                print("Machine instructions are Hewlett-Packard PA-RISC")

            if Machine == 15:
                print("Machine instructions are reserved for future use")

            if Machine == 16:
                print("Machine instructions are Intel 80960")

            if Machine == 17:
                print("Machine instructions are Power PC")

            if Machine == 18:
                print("Machine instructions are Power PC (64-bit)")

            if Machine == 19:
                print("Machine instructions are S390, including S380x")

            if Machine == 20:
                print("Machine instructions are IMB SPU/SPC")

            if Machine == 21:
                print("Machine instructions are reserved for future use")

            if Machine == 22:
                print("Machine instructions are reserved for future use")

            if Machine == 23:
                print("Machine instructions are reserved for future use")

            if Machine == 24:
                print("Machine instructions are reserved for future use")

            if Machine == 25:
                print("Machine instructions are reserved for future use")

            if Machine == 26:
                print("Machine instructions are reserved for future use")

            if Machine == 27:
                print("Machine instructions are reserved for future use")

            if Machine == 28:
                print("Machine instructions are reserved for future use")

            if Machine == 29:
                print("Machine instructions are reserved for future use")

            if Machine == 30:
                print("Machine instructions are reserved for future use")

            if Machine == 31:
                print("Machine instructions are reserved for future use")

            if Machine == 32:
                print("Machine instructions are reserved for future use")

            if Machine == 33:
                print("Machine instructions are reserved for future use")

            if Machine == 34:
                print("Machine instructions are reserved for future use")

            if Machine == 35:
                print("Machine instructions are reserved for future use")

            if Machine == 36:
                print("Machine instructions are NEC V800")

            if Machine == 37:
                print("Machine instructions are Fujitsu FR20")

            if Machine == 38:
                print("Machine instructions are TRW RH-32")

            if Machine == 39:
                print("Machine instructions are Motorola RCE")

            if Machine == 40:
                print("Machine instructions are ARM (up to Armv7/AArch32)")

            if Machine == 41:
                print("Machine instructions are Digital Alpha")

            if Machine == 42:
                print("Machine instructions are Super H")

            if Machine == 43:
                print("Machine instructions are SPARC Version 9")

            if Machine == 44:
                print("Machine instructions are Siemens TriCore: Embedded Processor")

            if Machine == 45:
                print("Machine instructions are Argonaut RISC Core")

            if Machine == 46:
                print("Machine instructions are Hitachi H3/300")

            if Machine == 47:
                print("Machine instructions are Hitachi H3/300H")

            if Machine == 48:
                print("Machine instructions are Hitachi H85")

            if Machine == 49:
                print("Machine instructions are Hitachi H8/500")

            if Machine == 50:
                print("Machine instructions are IA-64")

            if Machine == 51:
                print("Machine instructions are Stanford MIPS-X")

            if Machine == 52:
                print("Machine instructions are Motorola ColdFire")

            if Machine == 53:
                print("Machine instructions are M68HC12")

            if Machine == 54:
                print("Machine instructions are Fujitsu MMA Multimedia Accelerator")

            if Machine == 55:
                print("Machine instructions are Siemens PCP")

            if Machine == 56:
                print("Machine instructions are Sony nCPU embedded RISC Processor")

            if Machine == 57:
                print("Machine instructions are Denso NDRI microprocessor")

            if Machine == 58:
                print("Machine instructions are Motorola Star*Core Processor")

            if Machine == 59:
                print("Machine instructions are Toyota ME16 Processor")

            if Machine == 60:
                print("Machine instructions are STMicroelectronics ST100 Processor")

            if Machine == 61:
                print("Machine instructions are Advanced Logic Crop. Tiny J embedded processor Family")

            if Machine == 62:
                print("Machine instructions are AMD x86-64")

            if Machine == 63:
                print("Machine instructions are Sony DSP Processor")

            if Machine == 64:
                print("Machine instructions are Digital Equipment Corp. PDP-10")

            if Machine == 65:
                print("Machine instructions are Digital Equipment Corp. PDP-11")

            if Machine == 66:
                print("Machine instructions are Siemens FX66 Microcontroller")

            if Machine == 67:
                print("Machine instructions are STMicroelectronics ST9 + 8/16 bit microcontroller")

            if Machine == 68:
                print("Machine instructions are STMicroelectronics ST7 8-bit microcontroller")

            if Machine == 69:
                print("Machine instructions are Motorola MC68HC16 microcontroller")

            if Machine == 70:
                print("Machine instructions are Motorola MC68HC11 microcontroller")

            if Machine == 71:
                print("Machine instructions are Motorola MC68HC08")

            if Machine == 72:
                print("Machine instructions are Motorola MC68HC05")

            if Machine == 73:
                print("Machine instructions are Silicon Graphics SVx")

            if Machine == 74:
                print("Machine instructions are STMicroelectronics ST19 8-bit microcontroller")

            if Machine == 75:
                print("Machine instructions are Digital VAX")

            if Machine == 76:
                print("Machine instructions are Axis Communications 32-bit embedded processor")

            if Machine == 77:
                print("Machine instructions are Axis Communications 32-bit embedded processor")

            if Machine == 78:
                print("Machine instructions are Element 14 64-bit DSP processor")

            if Machine == 79:
                print("Machine instructions are LSI Logic 16-bit DSP processor")

            if Machine == 140:
                print("Machine instructions are TMS320 C6000 Family")

            if Machine == 175:
                print("Machine instructions are MCST Elkbrus e2k")

            if Machine == 183:
                print("Machine instructions are ARM 64-bit (Arm8/AArch64)")

            if Machine == 220:
                print("Machine instructions are Zilog z80")

            if Machine == 243:
                print("Machine instructions are RISC -V")

            if Machine == 247:
                print("Machine instructions are Berkley Packet Filter")

            if Machine == 257:
                print("Machine instructions are WDC 65C816")

            if Data == 1:
                # little endian

                f.seek(28)
                entry = int.from_bytes(f.read(8), "little")
                print("Entry Address is " + str(entry))

                f.seek(32)
                phoff = int.from_bytes(f.read(8), "little")
                print("Start of program header table is " + str(phoff))

                f.seek(40)
                shoff = int.from_bytes(f.read(8), "little")
                print("Start of section header is " + str(shoff))

                f.seek(48)
                flags = int.from_bytes(f.read(4), "little")
                print("Flags are " + str(flags))

                f.seek(52)
                ehsize = int.from_bytes(f.read(2), "little")
                print("The size of this header is " + str(ehsize))

                f.seek(54)
                phentsize = int.from_bytes(f.read(2), "little")
                print("Size of the program header table entry is " + str(phentsize))

                f.seek(56)
                phnum = int.from_bytes(f.read(2), "little")
                print("The number of entries in the program header table entry is " + str(phnum))

                f.seek(58)
                shentsize = int.from_bytes(f.read(2), "little")
                print("The size of the section header table entries is " + str(shentsize))

                f.seek(60)
                shnum = int.from_bytes(f.read(2), "little")
                print("The number of entries in the section header table " + str(shnum))

                f.seek(62)
                shstrndx = int.from_bytes(f.read(2), "little")
                print("The index of section header table entry " + str(shstrndx))

            if Data == 2:
                # 64, big endain

                f.seek(0, 0)
                Magic = (f.read(4), "big")
                print("Magic Numbers are " + str(Magic))

                f.seek(6)
                Version = int.from_bytes(f.read(1), "big")
                if Version != 1:
                    sys.exit("Version is not 1, invalid")

                f.seek(7)
                OSABI = int.from_bytes(f.read(1), "big")
                if OSABI == 0:
                    print("OSABI is System V")
                if OSABI == 1:
                    print("OSABI is HP-UX")
                if OSABI == 2:
                    print("OSABI is NetBSD")
                if OSABI == 3:
                    print("OSABI is Linux")
                if OSABI == 4:
                    print("OSABI is GNU Hurd")
                if OSABI == 6:
                    print("OSABI is Solaris")
                if OSABI == 7:
                    print("OSABI is AIX (Monterey)")
                if OSABI == 8:
                    print("OSABI is IRIX")
                if OSABI == 9:
                    print("OSABI is Free BSD")
                if OSABI == 10:
                    print("OSABI is Tru64")
                if OSABI == 11:
                    print("OSABI is Novell Modestro")
                if OSABI == 13:
                    print("OSABI is OpenBSD")
                if OSABI == 14:
                    print("OSABI is NonStop Kernel")
                if OSABI == 15:
                    print("OSABI is AROS")
                if OSABI == 16:
                    print("OSABI is FenixOS")
                if OSABI == 17:
                    print("OSABI is Nuxi CloudABI")
                if OSABI == 18:
                    print("OSABI is Stratus Technologies OpenVOS")
                else:
                    sys.exit("OSABI error")
                f.seek(8)
                ABIversion = int.from_bytes(f.read(1), "big")
                print("ABI Version is " + str(ABIversion))

                f.seek(9)
                Pad = int.from_bytes(f.read(7), "big")

                f.seek(16)
                Type = int.from_bytes(f.read(2), "big")
                if Type == 0:
                    print("File Type is NONE")
                if Type == 1:
                    print("File Type is REL")
                if Type == 2:
                    print("File Type is EXEC")
                if Type == 3:
                    print("File Type is DYN")
                if Type == 4:
                    print("File Type is CORE")
                if Type == 65024:
                    print("File Type is LOOS")
                if Type == 65279:
                    print("File Type is HIOS")
                if Type == 65280:
                    print("File Type is LOPROC")
                if Type == 65535:
                    print("File Type is HIPROC")


                f.seek(18)
                Machine = int.from_bytes(f.read(2), "big")

                if Machine == 0:
                    print("No specific machine instructions")

                if Machine == 1:
                    print("Machine instructions are AT&T WE 32100")

                if Machine == 2:
                    print("Machine instructions are SPARC")

                if Machine == 3:
                    print("Machine instructions are x86")

                if Machine == 4:
                    print("Machine instructions are Motorola 6800 (M68k)")

                if Machine == 5:
                    print("Machine instructions are Motorola 8800 (M88k)")

                if Machine == 6:
                    print("Machine instructions are MCU")

                if Machine == 7:
                    print("Machine instructions are Intel 80860")

                if Machine == 8:
                    print("Machine instructions are MIPS")

                if Machine == 9:
                    print("Machine instructions are IBM System/370")

                if Machine == 10:
                    print("Machine instructions are MIPS RS3000 Little-Endian")

                if Machine == 11:
                    print("Machine instructions are reserved for future use")

                if Machine == 12:
                    print("Machine instructions are reserved for future use")

                if Machine == 13:
                    print("Machine instructions are reserved for future use")

                if Machine == 14:
                    print("Machine instructions are Hewlett-Packard PA-RISC")

                if Machine == 15:
                    print("Machine instructions are reserved for future use")

                if Machine == 16:
                    print("Machine instructions are Intel 80960")

                if Machine == 17:
                    print("Machine instructions are Power PC")

                if Machine == 18:
                    print("Machine instructions are Power PC (64-bit)")

                if Machine == 19:
                    print("Machine instructions are S390, including S380x")

                if Machine == 20:
                    print("Machine instructions are IMB SPU/SPC")

                if Machine == 21:
                    print("Machine instructions are reserved for future use")

                if Machine == 22:
                    print("Machine instructions are reserved for future use")

                if Machine == 23:
                    print("Machine instructions are reserved for future use")

                if Machine == 24:
                    print("Machine instructions are reserved for future use")

                if Machine == 25:
                    print("Machine instructions are reserved for future use")

                if Machine == 26:
                    print("Machine instructions are reserved for future use")

                if Machine == 27:
                    print("Machine instructions are reserved for future use")

                if Machine == 28:
                    print("Machine instructions are reserved for future use")

                if Machine == 29:
                    print("Machine instructions are reserved for future use")

                if Machine == 30:
                    print("Machine instructions are reserved for future use")

                if Machine == 31:
                    print("Machine instructions are reserved for future use")

                if Machine == 32:
                    print("Machine instructions are reserved for future use")

                if Machine == 33:
                    print("Machine instructions are reserved for future use")

                if Machine == 34:
                    print("Machine instructions are reserved for future use")

                if Machine == 35:
                    print("Machine instructions are reserved for future use")

                if Machine == 36:
                    print("Machine instructions are NEC V800")

                if Machine == 37:
                    print("Machine instructions are Fujitsu FR20")

                if Machine == 38:
                    print("Machine instructions are TRW RH-32")

                if Machine == 39:
                    print("Machine instructions are Motorola RCE")

                if Machine == 40:
                    print("Machine instructions are ARM (up to Armv7/AArch32)")

                if Machine == 41:
                    print("Machine instructions are Digital Alpha")

                if Machine == 42:
                    print("Machine instructions are Super H")

                if Machine == 43:
                    print("Machine instructions are SPARC Version 9")

                if Machine == 44:
                    print("Machine instructions are Siemens TriCore: Embedded Processor")

                if Machine == 45:
                    print("Machine instructions are Argonaut RISC Core")

                if Machine == 46:
                    print("Machine instructions are Hitachi H3/300")

                if Machine == 47:
                    print("Machine instructions are Hitachi H3/300H")

                if Machine == 48:
                    print("Machine instructions are Hitachi H85")

                if Machine == 49:
                    print("Machine instructions are Hitachi H8/500")

                if Machine == 50:
                    print("Machine instructions are IA-64")

                if Machine == 51:
                    print("Machine instructions are Stanford MIPS-X")

                if Machine == 52:
                    print("Machine instructions are Motorola ColdFire")

                if Machine == 53:
                    print("Machine instructions are M68HC12")

                if Machine == 54:
                    print("Machine instructions are Fujitsu MMA Multimedia Accelerator")

                if Machine == 55:
                    print("Machine instructions are Siemens PCP")

                if Machine == 56:
                    print("Machine instructions are Sony nCPU embedded RISC Processor")

                if Machine == 57:
                    print("Machine instructions are Denso NDRI microprocessor")

                if Machine == 58:
                    print("Machine instructions are Motorola Star*Core Processor")

                if Machine == 59:
                    print("Machine instructions are Toyota ME16 Processor")

                if Machine == 60:
                    print("Machine instructions are STMicroelectronics ST100 Processor")

                if Machine == 61:
                    print("Machine instructions are Advanced Logic Crop. Tiny J embedded processor Family")

                if Machine == 62:
                    print("Machine instructions are AMD x86-64")

                if Machine == 63:
                    print("Machine instructions are Sony DSP Processor")

                if Machine == 64:
                    print("Machine instructions are Digital Equipment Corp. PDP-10")

                if Machine == 65:
                    print("Machine instructions are Digital Equipment Corp. PDP-11")

                if Machine == 66:
                    print("Machine instructions are Siemens FX66 Microcontroller")

                if Machine == 67:
                    print("Machine instructions are STMicroelectronics ST9 + 8/16 bit microcontroller")

                if Machine == 68:
                    print("Machine instructions are STMicroelectronics ST7 8-bit microcontroller")

                if Machine == 69:
                    print("Machine instructions are Motorola MC68HC16 microcontroller")

                if Machine == 70:
                    print("Machine instructions are Motorola MC68HC11 microcontroller")

                if Machine == 71:
                    print("Machine instructions are Motorola MC68HC08")

                if Machine == 72:
                    print("Machine instructions are Motorola MC68HC05")

                if Machine == 73:
                    print("Machine instructions are Silicon Graphics SVx")

                if Machine == 74:
                    print("Machine instructions are STMicroelectronics ST19 8-bit microcontroller")

                if Machine == 75:
                    print("Machine instructions are Digital VAX")

                if Machine == 76:
                    print("Machine instructions are Axis Communications 32-bit embedded processor")

                if Machine == 77:
                    print("Machine instructions are Axis Communications 32-bit embedded processor")

                if Machine == 78:
                    print("Machine instructions are Element 14 64-bit DSP processor")

                if Machine == 79:
                    print("Machine instructions are LSI Logic 16-bit DSP processor")

                if Machine == 140:
                    print("Machine instructions are TMS320 C6000 Family")

                if Machine == 175:
                    print("Machine instructions are MCST Elkbrus e2k")

                if Machine == 183:
                    print("Machine instructions are ARM 64-bit (Arm8/AArch64)")

                if Machine == 220:
                    print("Machine instructions are Zilog z80")

                if Machine == 243:
                    print("Machine instructions are RISC -V")

                if Machine == 247:
                    print("Machine instructions are Berkley Packet Filter")

                if Machine == 257:
                    print("Machine instructions are WDC 65C816")

                f.seek(28)
                entry = int.from_bytes(f.read(8), "big")
                print("Entry Address is " + str(entry))

                f.seek(32)
                phoff = int.from_bytes(f.read(8), "big")
                print("Start of program header table is " + str(phoff))

                f.seek(40)
                shoff = int.from_bytes(f.read(8), "big")
                print("Start of section header is " + str(shoff))

                f.seek(48)
                flags = int.from_bytes(f.read(4), "big")
                print("Flags are " + str(flags))

                f.seek(52)
                ehsize = int.from_bytes(f.read(2), "big")
                print("The size of this header is " + str(ehsize))

                f.seek(54)
                phentsize = int.from_bytes(f.read(2), "big")
                print("Size of the program header table entry is " + str(phentsize))

                f.seek(56)
                phnum = int.from_bytes(f.read(2), "big")
                print("The number of entries in the program header table entry is " + str(phnum))

                f.seek(58)
                shentsize = int.from_bytes(f.read(2), "big")
                print("The size of the section header table entries is " + str(shentsize))

                f.seek(60)
                shnum = int.from_bytes(f.read(2), "big")
                print("The number of entries in the section header table " + str(shnum))

                f.seek(62)
                shstrndx = int.from_bytes(f.read(2), "big")
                print("The index of section header table entry " + str(shstrndx))

parse()