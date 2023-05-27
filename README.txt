ZZTONG-PREFABS READ-ME for A21.EXP.ZZ015

GOAL:

This modlet provides semi-plain "meat and potatoes" POIs, Tiles, Parts, Blocks,
Decorations and Stamps of an acceptable quality and in enough quantity to fill
gaps in world generation and make a meaningful dent in player demands for
variety.

DEPENDENCIES:

This modlet depends upon the "Custom Blocks Pack" modlet, which you should
find has also been distributed with this modlet. Future versions of this
modlet may become to dependent on other modlets.

CLIENT INSTALLATION: (Windows)

1. Go to %APPDATA%/7DaysToDie

2. Locate or Create a "Mods" folder.
	The folder does not exist by default. If this is your first Mod, then you
	will need to create the Mods folder.

3. Place the "00-Custom-Blocks-Pack" folder in the Mods folder:
	%APPDATA%/7DaysToDie/Mods ... %APPDATA/7DaysToDie/Mods/00-Custom-Blocks-Pack

4. Place the "ZZTong-Prefabs" folder in the Mods folder:
	%APPDATA%/7DaysToDie/Mods ... %APPDATA/7DaysToDie/Mods/ZZTong-Prefabs

CLIENT INSTALLATION (Mac) - TBD
CLIENT INSTALLATION (Linux) - TBD
SERVER INSTALLATION - TBD

WARNING: If you choose to extract POIs from this modlet that you need to know
Parts and Custom Block XML works, or you will not end up with a complete POI!

IS THE MODLET SERVER-SIDE OR CLIENT-SIDE?

I recommend installation on both, but Server-Side only should largely work with
some noticable quirks. As near as I have been able to determine, because POIs
are rolled into the world distributed by the server, and all the modlet's
additions to the game configuration are in XML, this can be a Server-Side only
modlet.

The most notable issue observed by players without a local installation of the
modlet is the lack of local "imposter" files will mean custom POIs only become
visible when you get close to them. This alone can be enough to annoy players.

The next complication relates to features such as using F11 to identify a POI
and Admin abilities such as being able to teleport to a POI. Neither of those
features will not work without a local copy. Players may also find that odd
things, like key boxes, only work if they have the modlet installed.

These quirks are NOT bugs in the modlet or the POIs.

VANILLA RANDOM WORLD GENERATOR (RWG):

Installing this Mod should be all that is necessary to include this content
when generating a new world using the 7D2D built-in Random World Generator. Of
course, it is up the the RWG to determine if, when, and where to place things.

As of ZZ009, this modlet changes the configuration of rwgmixer.xml to put more
Tiles into play for increased variety.

Also, it changes Cities to be ringed by Residential rather than Rural content.
This way, Country Towns are surrounded by Farms, but Cities are surrounded by
Houses. If you don't like that, then change the rwgmixer.xml file in this
modlet. This change to cities will be removed from this modlet with A21 because
it has been picked up as a feature in A21's RWG. How cool!

TERAGON:

Support for Teragon is current as of the release date, but since Teragon is
undergoing active development you may find that my support becomes out-of-date.
Please let me know if that happens.

You should refer to notes and configuration files found in the Teragon folder
within this modlet. As I write this I am aware of bugs in Teragon, but also
excited to see that the Teragon teams takes these issue seriously and works to
resolve them.

WORLD EDITOR AND MAP MAKERS:

If you have already made a map and plan to place these POIs by hand then be
aware that I make extensive use of Parts and Custom Blocks. The World Editor
does not know about Parts, so you run the risk of ending up with a POI that is
missing content.

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

As far as I know: (Please correct me if I'm wrong.)

APOCALYPSE NOW - I'm under the impression you can using the Game's RWG to make
maps and if this modlet is installed when you do that, then I'm told you will
have a viable map.

DARKNESS FALLS - Requires special POIs to be on a map, so you need somebody
to make you a map and do specific placement. If that effort involves using
the Game's RWG while this modlet is installed, then you'll see these POIs in
the resulting map.

RAVENHEARST - I'm under the impression you can use the Game's RWG to make
maps. If so, make sure this modlet is installed when you do that.

REBIRTH - I'm aware this overhaul is actively integrating my modlet into maps
and content, so look to them for advice on the best practices. I probably get
the most feedback from Rebirth players and creators.

UNDEAD LEGACY - I'm under the impression you can using the Game's RWG to make
maps and if this modlet is installed when you do that, then I'm told you will
have a viable map. I'm aware of at least one incompatibility. UL has deleted
the "dyes" lootlist from the Vanilla configuration. I have custom blocks that
depended on that lootlist. You'll get errors if you use my modlet with UL.
There is a compatibility modlet by iV7Z available on Nexus that deals with
those errors.

WAR3ZUK - I do not know. I'm hoping you just need this modlet installed and
that you can use RWG.

OTHER - My hope is that if you can use RWG to generate a map for your overhaul
that all you would have to do is correctly install this modlet.

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
and everyone who leaves me feedback scattered about Discord. Thanks to Guppy
for providing me an "office" channel on his Discord server.

Finally, special thanks to Stallionsden and Battlepapi of CompoPack fame, plus
any and all who lurk on in the #prefabbers-hangout Discord channel. Their
guidance throughout the CompoPack submission process and advice via the
CompoPack Discord channels taught me a lot about 7D2D Prefabs, the Prefab
Editor, game performance issues, and more. You're awesome!
