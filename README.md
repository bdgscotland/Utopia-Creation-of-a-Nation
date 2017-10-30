# Utopia-Creation-of-a-Nation
Various data for Utopia RTS game from 1991

Purpose is to learn structure of how to create new content for the game.

Save Games
===
Initial investigation and reverse engineering of the save game file format. No specification available.

Scenarios
===
TBA

Map Editor
===
TBA

Save Game Trainer
===
```
DMBP:utopia duncan$ python python/SaveGame.py ./SAVEGAME.0 999999

Utopia - Creation of a Nation Save Game Editor
==============================================
Backup:				./SAVEGAME.0 backed up to ./SAVEGAME.0.BAK
Game Date:			12/12/1990
Game QOL:			120
Read Credits (GR):		999999
Written Credits (GR):		999999
```

Game Remake
===
Possible?

Art Extraction
===
TBA

Music
===
Amiga modules included. Play on Mac/PC via VLC.

GDD
===
Requires study of manual, gameplay, and reverse engineering data

Amiga Version
===
Unknown at this stage. WHDLoad uses floppy disk images and the floppy disk is raw binary storage not regular filesystem. I suspect that general structure is the same but there is an extra layer of unknown structure that I don't want to deal with right now.
