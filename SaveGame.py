import sys
import binascii
import struct
import array
import os

## CLI ARGUMENTS
credits = sys.argv[2];
sgpath  = sys.argv[1];

## VARS
SIZE_SAVENUM = 5191;
SIZE_SAVEALP = 37199;
SaveGameNUMERIC = False;
SaveGameALPHA = False;

## FUNCTIONS


def read_credits(in_filename):
    global SaveGameNUMERIC
    if (os.stat(in_filename).st_size == SIZE_SAVENUM):
        SaveGameNUMERIC = True;
        with open(in_filename, 'rb') as fh:
            fh.seek(0x0586);
            bCredits = fh.read(4);
            bCreditsLE = bytearray(bCredits); # little endian
            bCreditsLE.reverse();
            hCredits = binascii.hexlify(bCreditsLE);
            iCredits = int(hCredits,16);
            fh.close();
            return iCredits;
    else:
        SaveGameNUMERIC = False;


        
def write_credits(in_filename,out_credits):
    global SaveGameNUMERIC
    if (os.stat(in_filename).st_size == SIZE_SAVENUM):
        SaveGameNUMERIC = True;
        with open(in_filename, 'r+b') as fh:
            out_credits = int(out_credits);
            bCredits = struct.pack('<i2',out_credits);
            hCredits = binascii.hexlify(bCredits); 
            fh.seek(0x0586);
            fh.write(bCredits);
            fh.close();
    else:
        SaveGameNUMERIC = False;
       

def backup_file(in_filename):
    if (os.stat(in_filename).st_size == SIZE_SAVENUM or os.stat(in_filename).st_size == SIZE_SAVEALP):        
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
            print("Backup:\t\t\t\t%s backed up to %s") % (in_filename, out_filename);
    else:
        print("Backup:\t\t\tFilesize unexpected - not backed up");


## MAIN
print("\nUtopia - Creation of a Nation Save Game Editor\n==============================================");
backup_file(sgpath);    
print("Read Credits (GR):\t\t%s" % read_credits(sgpath));
write_credits(sgpath, credits);
if (SaveGameNUMERIC == True):
    print("Written Credits (GR):\t\t%s" % read_credits(sgpath));





