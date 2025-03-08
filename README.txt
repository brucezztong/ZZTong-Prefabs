ZZTONG-PREFABS READ-ME for V1.3.ZZ027

GOAL:

This modlet provides semi-plain "meat and potatoes" POIs, Tiles, Parts, 
Decorations and Stamps of an acceptable quality and in enough quantity to fill
gaps in world generation and make a meaningful dent in player demands for
variety.

DEPENDENCIES:

There are currently no dependencies. This modlet can stand alone.

CLIENT INSTALLATION: (Windows)

1. Go to %APPDATA%/7DaysToDie

2. Locate or Create a "Mods" folder.
	The folder does not exist by default. If this is your first Mod, then you
	will need to create the Mods folder.

3. Place the "ZZTong-Prefabs" folder in the Mods folder:
	%APPDATA%/7DaysToDie/Mods ... %APPDATA/7DaysToDie/Mods/ZZTong-Prefabs

SEE ALSO: INSTALL.png

NOTE: The Internet is full of OLD information. You will find many sites and
meet people who will suggest an OLD location for Mods. The following path
is DEPRECATED by TFP and will NOT work in some future release.

C:\Program Files (x86)\Steam\steamapps\common\7 Days To Die\Mods


CLIENT INSTALLATION (Mac) - TBD
CLIENT INSTALLATION (Linux) - TBD
SERVER INSTALLATION - TBD

WARNING: If you choose to extract POIs from this modlet you need to know
how Parts and Localization work or you will not end up with complete POIs
and Tiles! I suggest you leave everything packed up in the modlet.

IS THE MODLET SERVER-SIDE OR CLIENT-SIDE?

Both. You want the modlet on both the server and all the clients. Anyone who
tells you POIs can be server-side only is conveying information without
enough nuance. Going Server-side only mostly works. (Keyword "mostly.")

While a server-side only installation will convey the blocks of a POI, it does
not convey the Localization information and the details of triggers linked to
keyracks and similar blocks. These quirks are NOT bugs in the modlet or POIs.

Perhaps someday TFP will allow the server to send the additional information
necessary, but for now that is not the case.

VANILLA RANDOM WORLD GENERATOR (RWG):

Installing this Mod should be all that is necessary to include this content
when generating a new world using the 7D2D built-in Random World Generator. Of
course, it is up the the RWG to determine if, when, and where to place things.

TERAGON:

Support for Teragon is current as of the release date, but since Teragon is
undergoing active development you may find that my support becomes out-of-date.
Please let me know if that happens.

You should refer to notes and configuration files found in the Teragon folder
within this modlet. As I write this I am aware of bugs in Teragon, but also
excited to see that the Teragon teams takes these issue seriously and works to
resolve them.

COMPOPACK:

These POIs are also contributed to the CompoPack. If you are also using the
CompoPack then you have a choice to make:

(1) Do nothing. You'll run a chance of getting duplicate POIs close to each
other in vanilla settlements. Some will be from the CompoPack and some will be
from this modlet. They're likely to be slightly different. This is the easiest
choice to accomplish.

(2) Remove this modlet. This will eliminate the chance of duplication in
vanilla settlements, but you'll probably be using older POIs and you might be
missing a few new POIs.

(3) Remove the "ZZTong" files found in the CompoPack's folders of POIs for
vanilla settlements but leave the "ZZTong" POIs in all of the CompoPack's
custom settlements. This gives you the best combination, but involves the most
work.

OVERHAUL MODS:

Overhaul Mods make extensive changes to the game and I cannot give you a recipe
for how to include these POIs. Plainly stated, I'm focused on Vanilla. There
are too many overhauls to support them all, so I provide support when requsted
so long as I don't have to make an overhaul-unique version of the modlet.

Some Overhaul Mods choose to embed this modlet, or portions of this modlet,
in their own distributions. I cannot predict the possible collisions and
ramifications. I also cannot force overhaul modders to update to the latest
versions of POIs.

PLAYING WITHOUT TRADERS

This modlet includes an alternative collections of Traders that you can use to
replace the traders on a map that you have just made. You can find these
trader files in the Prefabs/Traders/ folder. Filenames that end in "x" are dead
trader versions, when the trader has been overrun by zombies and the trader is
now just a POI.

None of these files are rigged for RWG to detect them. To use them, you
generate a world like normal. Then you find the "prefabs.xml" for your new
world in your %AppData%/Roaming/7DaysToDie/GeneratedWorlds folder. You edit
prefabs.xml in your favorite text editor, find all the POIs with that start
with "trader_" and add "x" to the name.

For example, change trader_jen to trader_jenx.

Then, when somebody approaches those locations playing the game, the game will
load the alternative POI instead. If you've already been playing the world, it
won't retroactively revert the POI.

Why would you use these? These are in support of people who play with heavily
modified games. Have you ever wanted to play without any traders? Having these
variant POIs in the modlet makes that easy to configure and play.

LINUX SERVERS:

I often get questions about how to install this modlet on a Linux Server.
Server Admins have a lot of flexibility and I usually cannot provide a solid
answer when I'm ignorant of what they've done. The best I can do is make my
own notes available related to how I configure things for my little in-house
test server. You can find those notes here:

https://drive.google.com/drive/folders/1Hq8d-k37kOFs7xgft7P2IeZesasGuI5s?usp=sharing

POI NOTES:

If you'd like extra information about each POI, check out the ABOUT.txt file
also located in this directory. I decided to put all the 'behind the scenes'
stuff there.

DECORATIONS

Decorations are not questable POIs, but they do not take the place of POIs on
your map so you're not missing anything. Beware, some of the Hunters Traps are
deadly. If you do not want these to be included in your map then edit/remove
the biomes.xml file found in the Mod's config directory.

INCLUSION IN OTHER PACKS AND MODS:

I am receptive to others including these POIs into their own packs and Overhaul
mods. All I ask is that you give proper credit and/or attribution. (I prefer
you use the handle "ZZTong" or "zztong".) If you do include these POIs in
something you plan to distribute, I'd appreciate knowing. Just send me a quick
message at zztong@gmail.com and let me know.

Please note the GPLv3 license on this modlet. You should find it accomodating
for your project. If not, reach out to me and we can discuss the matter.

COPYRIGHT

These original POIs (and derivatives) are copyright by Bruce Tong. This does
not preclude derivitive works. It only establishes my rights in accordance with
the GPLv3. Note that I am not able to express the copyright on the individual
files of the modlet because they are often binary files. This notice covers the
entire modlet. My copyright only applies to my changes to any POIs that are
derivitite works, such as TFP POIs brought forward from older versions of the
game. I don't think this violates TFP's copyrights. I'll also note the license
for 7D2D gives TFP an automatic license to use any POIs I've created.

THANKS:

A few prefabs contain content that is a derivation from a vanilla POI. For
example, you might find a trailer that was based on a vanilla trailer, but was
modified. The TFP's front loader from their Saw Mill was also modified. My
thanks to TFP for creating inspiring POIs and amazing arrangements of blocks.

One or more POIs may include references to "Canuck Coffee" by Not-a-Gamer
Gaming (DaphyDuck91 and Genosis). NAGG, as they are known, have provided to the
community a number of POIs as well as providing YouTube/Twitch entertainment.

I'd like to also thank the many folks with whom I collaborate, trade ideas,
chat, and otherwise geek-out on 7D2D: Deverezieaux, Cranberry Monster,
Voltralux and everyone who leaves me feedback scattered about Discord. Thanks
to Guppycur for providing me an "office" channel on his Discord server.

Finally, special thanks to Stallionsden and Battlepapi of CompoPack fame, plus
any and all who lurk on in the #prefabbers-hangout Discord channel. Their
guidance throughout the CompoPack submission process and advice via the
CompoPack Discord channels taught me a lot about 7D2D Prefabs, the Prefab
Editor, game performance issues, and more. You're awesome!
