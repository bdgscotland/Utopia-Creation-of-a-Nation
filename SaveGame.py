import sys
import binascii
import struct
import array
import os




#0x102 - Free colonists
#0x116 - Total colonists?


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

#--------------------------------------
        
def read_gamedate(in_filename):
    # Game Date does not seem to cumulatively affect other items
    # Other counters matter more, this seems to be aesthetic only
    global SaveGameNUMERIC
    if (os.stat(in_filename).st_size == SIZE_SAVENUM):
        SaveGameNUMERIC = True;
        with open(in_filename, 'rb') as fh:
            fh.seek(0x1431); 
            bDate = fh.read(10);
            bDate.decode("utf-8");
            fh.close();
            return bDate;
    else:
        SaveGameNUMERIC = False;    

#---------------------------------------------------

def read_grant(in_filename):
    global SaveGameNUMERIC
    if (os.stat(in_filename).st_size == SIZE_SAVENUM):
        SaveGameNUMERIC = True;
        with open(in_filename, 'rb') as fh:
            fh.seek(0x1212); # qol
            bGrant = fh.read(2);
            bGrant = bytearray(bGrant); # little endian
            bGrant.reverse();
            hGrant = binascii.hexlify(bGrant);
            iGrant = int(hGrant,16);
            
            fh.close();
            return iGrant;
    else:
        SaveGameNUMERIC = False;    

#--------------------------------------------------------
        
def read_qol(in_filename):
    global SaveGameNUMERIC
    if (os.stat(in_filename).st_size == SIZE_SAVENUM):
        SaveGameNUMERIC = True;
        with open(in_filename, 'rb') as fh:
            fh.seek(0x11fc); # qol
            bQOL = fh.read(2);
            bQOL = bytearray(bQOL); # little endian
            bQOL.reverse();
            hQOL = binascii.hexlify(bQOL);
            iQOL = int(hQOL,16);

            #0x1222
            
            fh.close();
            return iQOL;
    else:
        SaveGameNUMERIC = False;    

        
def write_qol(in_filename,out_qol):
    global SaveGameNUMERIC
    if (os.stat(in_filename).st_size == SIZE_SAVENUM):
        SaveGameNUMERIC = True;
        with open(in_filename, 'r+b') as fh:
            out_qol = int(out_qol);
            bQOL = struct.pack('<i2',out_qol);
            hQOL = binascii.hexlify(bQOL); 
            fh.seek(0x11fc);
            fh.write(bQOL);
            fh.close();
    else:
        SaveGameNUMERIC = False;
       
#-------------------------------------

        
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
print("Game Date:\t\t\t%s" % read_gamedate(sgpath));
print("Game QOL:\t\t\t%s (resets via algorithm)" % read_qol(sgpath));
print("Colony Grant:\t\t\t%s (changes only last a single month currently)" % read_grant(sgpath));
print("Read Credits (GR):\t\t%s" % read_credits(sgpath));
write_credits(sgpath, credits);
write_qol(sgpath, 120);
if (SaveGameNUMERIC == True):
    print("------------");
    print("Written Credits (GR):\t\t%s" % read_credits(sgpath));
    print("Written QOL:\t\t\t%s" % read_qol(sgpath));





