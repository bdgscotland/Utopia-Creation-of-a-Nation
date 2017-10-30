import sys
import binascii
import struct
import array

#credits = sys.argv[2];
sgpath  = sys.argv[1];

#if file length is 5191 it is numeric save file
#if file length if XXXXX it is alpha save file

#chunk_size = 5191
#data = in_file.read(chunk_size)

def read_credits(in_filename):
    with open(in_filename, 'rb') as fh:
        fh.seek(0x0586);
        bCredits = fh.read(4);
        bCreditsLE = bytearray(bCredits); # little endian
        bCreditsLE.reverse();
        hCredits = binascii.hexlify(bCreditsLE);
        iCredits = int(hCredits,16);
        return iCredits;


def backup_file(in_filename):
    out_filename = in_filename + '.BAK'
    byte_string = ''
    
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            char = infile.read(1)
            byte = ord(char)
            # print byte
            byte_string += chr(byte)
            while char != "":
                char = infile.read(1)
                if char != "":
                    byte = ord(char)
                    # print byte
                    byte_string += chr(byte)
            outfile.write(byte_string)
            outfile.close()
        print("Backup %s backed up to %s") % (in_filename, out_filename);

## MAIN
print("\nUtopia - Creation of a Nation Save Game Editor\n==============================================");
backup_file(sgpath);    
print("Player credits: %s" % read_credits(sgpath));





