ZZTONG PREFABS READ-ME for A20.4

GOAL:

My goal is to provide semi-plain "meat and potatoes" POIs, Parts, Tiles,
Decorations and Stamps of an acceptable quality and in enough quantity to fill
gaps in world generation and make a meaningful dent in player demands for
variety. I hope you'll find these to be good enough to help round out the
nooks and crannies of your generated worlds.

INFO:

This mod does not contain any custom blocks, resources, objects, etc. It
depends only on the vanilla game and introduces no other requirements or
dependencies.

This content conforms to CompoPack rules for contributions, which means they
will often contain more Zombies than Vanilla content. The loot is intended to
work out the same as Vanilla content, but that balance is subjective.

CLIENT INSTALLATION: (Windows)

1. Go to %APPDATA%/7DaysToDie
2. Locate or Create a "Mods" folder.
	The folder does not exist by default. If this is your first Mod, then you
	will need to create the Mods folder.
3. Place the "ZZTong-Prefabs" folder in the Mods folder:
	%APPDATA%/7DaysToDie/Mods
4. Review the "Conflicts" Section, below.

CLIENT INSTALLATION (Mac) - TBD
CLIENT INSTALLATION (Linux) - TBD

SERVER INSTALLATION:

There are too many variations for me to address this topic. In general,
something similar to the Client Installation instructions has to happen, but
there will probably be different paths involved.

CONFLICTS: (CompoPack)

Much of this content is also available in the CompoPack. You can use both Mods.
Doing so may skew the weighting of placement by your world generator. That is,
if zztong_Store_XS_01 and xcostum_Store_XS_01(by_ZZTong) are both available,
your world generator won't realize they are the same content and place them
both. When that happens, it becomes likely they'll be placed near each other
(even next to each other) and you probably won't like the results.

The answer is to remove the duplicate content from one of the Mods. The first
choice you have to make is to decide which Mod to change.

If the CompoPack Mod is newer than the ZZTong-Prefabs Mod, then remove the
ZZTong-Prefabs Mod because the CompoPack will include the most current
content.

Generally speaking, however, the CompoPack will be the older Mod since it tends
to get released once or twice a year. If so, remove all the files in the Prefabs
folder with "by_ZZTong" in the filename. In this way, you'll get all the same
ZZTong content that appears in the CompoPack plus any new content which the
CompoPack has not yet released. And, of course, you would still get all of the
wonderful and challenging non-ZZTong content from the CompoPack.

CONFLICTS: (Overhaul Mods)

Overhaul Mods tend to have their own versions of POIs. Those Mods tend to
include the ZZTong POIs in their own mod, so you should not need to also have
the ZZTong Mod installed at the same time. Generating a world with both
installed may lead to unexpected results, including Exceptions related to the
inclusion of unknown blocks.

VANILLA RANDOM WORLD GENERATOR (RWG):

Installing this Mod should be all that is necessary to include this content
when generating a new world using the 7D2D built-in Random World Generator. Of
course, it is up the the RWG to determine if, when, and where to place things.

POI NOTES:

If you'd like extra information about each POI, check out the ABOUT.txt file
also located in this directory. I decided to put all the 'behind the scenes'
stuff there.

DECORATIONS

The Hunters Traps and Tents are built like POIs, but they have no zombies.
They're more like obsticals. An aware player will avoid falling into them.
A distracted, rushed or clumbsy player will fall in. Please know the traps
can be deadly. You'll land on spikes and take damage every few seconds until
either the spikes break or you die. You may not want these to be included in
your map. If not, edit/remove the biomes.xml file found in the Mod's config
directory. The appeal of this is they do not displace POIs.

INCLUSION IN OTHER PACKS AND MODS:

I have been contributing these POIs to the CompoPack, so if you're using the
CompoPack you might find this mod to be redundant. The first of these POIs
should appear in CP48. Anything created after the release of CP48 would then
appear in CP49, and so on.

I am receptive to others including these POIs into their own packs and custom
games. All I ask is that you give proper credit and/or attribution. (I prefer
you use the handle "ZZTong" or "zztong".) If you do include these POIs in
something you plan to distribute, I'd appreciate knowing. Just send me a quick
message at zztong@gmail.com and let me know.

Please note the GPLv3 license on this modlet. You should find it accomodating
for your project. If not, reach out to me and we can discuss the matter.

COPYRIGHT

These POIs are copyright by Bruce Tong. Do not panic. This does not preclude
derivitive works. It only establishes my rights in accordance with the GPLv3.
Note that I am not able to express the copy right on the individual files of
the modlet because they are often binary files. This notice covers the entire
modlet.

THANKS:

A few prefabs contain content that is a derivation from a vanilla POI. For
example, you might find a trailer that was based on a vanilla trailer, but was
modified. The TFP's front loader from their Saw Mill was also modified. My
thanks to TFP for creating inspiring POIs and amazing arrangements of blocks.

One or more POIs may include references to "Canuck Coffee" by Not-a-Gamer
Gaming (DaphyDuck91 and Genosis). NAGG, as they are known, provide a number
of POIs in their own mod and the CompoPack, as well as providing
YouTube/Twitch entertainment and hosting a nice community on their servers.

Finally, special thanks to Stallionsden and Battlepapi of CompoPack fame, plus
any and all who lurk on in the #prefabbers-hangout Discord channel. Their
guidance throughout the CompoPack submission process and advice via the
CompoPack Discord channels taught me a lot about 7D2D Prefabs, the Prefab
Editor, game performance issues, and more. You're awesome!

RELEASE NOTES: (Newest to Oldest)

A20.4 - ZZ008 - Fixed numerous bugs and rebalanced loot. Added
rwg_tile_downtown_intersection_zztong_01 and Intersection_01, Intersection_02
and Intersection_03 to go with it. Added Ranch_01.
Added all my custom Parts because parts are cool, parts are wonderful.
Introduced this modlet to GitHub for my own sanity and peace of mind.
Introduced this modlet to the GPLv3 license.

A20.1 - ZZ007 - Added Farm_01, Farm_02, Farm_03, Farm_04, Farm_05, Farm_06
Farm_07, Farm_08, Garage_01, Stormwater_Detention_Pond_01, Biowaste_Dump_01,
Electrical_Substation_01, Cement_Plant_01. Retrieved skyscraper_02 from A19
and brought it forward as TFP_Skyscraper_02. Promoted Mass_Grave_01 and
Mass_Grave_02 back to being POIs. Fixed minor problems in EMS_01, Bar_Pool_01,
House_01, House_02 and TFP_Cemetary_01. Added rwg_tile_rural_straight_zztong_01.

A20.EXP-ZZ006 - A20 Experimental Support. All POIs converted to A20.

A19.6-ZZ005 - Added POIs: Store_XS_09, Store_XS_10, Skyscraper_01,
Skyscraper_01_destroyed, Warehouse_01, Cave_01 and KZTV_01.
Added Decoration: Tent_01, Tent_02, Tent_03, Tent_04, and Tent_05.

A19.6-ZZ004 - Fixed a problem with TFP_Cemetary.

A19.6-ZZ003 - Many block conversions to support the new version. I shamelessly
piggy-back on the work of Stallionsden for the CompoPack. Many thanks to him
for shepparding me through this process. Added TFP_Army_Barracks_01,
TFP_Cemetery_01, TFP_Ranger_Station_01, TFP_House_New_04, Presidio_Museum_01,
Store_XS_01, Store_XS_02, Store_XS_03, Store_XS_04, Store_XS_05, Store_XS_06, 
Store_XS_07, and Store_XS_08.

A19.5-ZZ002 - Fixed the Cabin_Fort_01 so that it wouldn't collapse into an
empty lot. (Yikes!) Fixed Filename Typo (Farmers Market), Fixed
ShowQuestClearCount settings. New POIs: Destroyed Variants from ZZ001,
House_03, StripMall_01, StripMall_02, Restaurant_01, Remnant_House_01,
and Storm_Cellar_01. Added Decorations: Hunters_Trap_01 and Hunters_Trap_02.
Converted Mass_Grave_01 and Mass_Grave_02 to Decorations.

A19.5-ZZ001 - Initial Release
