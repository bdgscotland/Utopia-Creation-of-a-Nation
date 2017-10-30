# Utopia-Creation-of-a-Nation
Various data for Utopia RTS game from 1991

Purpose is to learn structure of how to create new content for the game.

Save Games
===
Initial investigation and reverse engineering of the save game file format. No specification available.
* Byte grouping seems to be 4 bytes for at least map populated content - FFAAABBB 00XY0001
* FFAAABBB - Map coordinates
* 00XY0001 - Object type - buildings
_ See Excel sheet _

Scenarios
===
TBA

Map Editor
===
TBA

Save Game Trainer
===
```DMBP:utopia duncan$ python python/SaveGame.py ./SAVEGAME.0 999999

Utopia - Creation of a Nation Save Game Editor
Backup:				./SAVEGAME.0 backed up to ./SAVEGAME.0.BAK
Read Credits (GR):		45040
Written Credits (GR):		999999
DMBP:utopia duncan$```


Game Remake
===
Possible?

Art Extraction
===
TBA

GDD
===
Requires study of manual, gameplay, and reverse engineering data

Amiga Version
===
Unknown at this stage. WHDLoad uses floppy disk images and the floppy disk is raw binary storage not regular filesystem. I suspect that general structure is the same but there is an extra layer of unknown structure that I don't want to deal with right now.
