ZZTONG-PREFABS READ-ME for A20.5-ZZ010

GOAL:

This modlet provides semi-plain "meat and potatoes" POIs, Parts, Tiles,
Decorations and Stamps of an acceptable quality and in enough quantity to fill
gaps in world generation and make a meaningful dent in player demands for
variety.

DEPENDENCIES:

This modlet depends only on the vanilla game and introduces no other
requirements or dependencies.

CLIENT INSTALLATION: (Windows)

1. Go to %APPDATA%/7DaysToDie
2. Locate or Create a "Mods" folder.
	The folder does not exist by default. If this is your first Mod, then you
	will need to create the Mods folder.
3. Place the "ZZTong-Prefabs" folder in the Mods folder:
	%APPDATA%/7DaysToDie/Mods ... %APPDATA/7DaysToDie/Mods/ZZTong-Prefabs
4. Review the "Conflicts" Section, below.

CLIENT INSTALLATION (Mac) - TBD
CLIENT INSTALLATION (Linux) - TBD
SERVER INSTALLATION - TBD

IS THE MODLET SERVER-SIDE OR CLIENT-SIDE?

I don't know, but I'm going to assert I think it works as a server-side only
modlet. The advice I get from more experienced POI developers is that all of a
modlet's POIs need to be installed on the client-side. Please let me know if
your testing reveals something conclusive. I don't want to be spreading
incorrect information.

VANILLA RANDOM WORLD GENERATOR (RWG):

Installing this Mod should be all that is necessary to include this content
when generating a new world using the 7D2D built-in Random World Generator. Of
course, it is up the the RWG to determine if, when, and where to place things.

As of ZZ009, this modlet changes the configuration of rwgmixer.xml to put two
more TFP Tiles into play for increased variety. Also, it changes Cities to be
ringed by Residential rather than Rural content. This way, Country Towns are
surrounded by Farms, but Cities are surrounded by Houses. If you don't like
that, then change the rwgmixer.xml file in this modlet.

WORLD EDITOR:

If you have already made a map and plan to place these POIs by hand then be
aware that I make extensive use of Parts. Manual placement does not know about
Parts, so you run the risk of ending up with a POI that is missing content.
That content can include loot. This is an A20 reality. I have no idea if A21
will include more widespread support for Parts.

CONFLICTS: (CompoPack)

These POIs are also contributed to the CompoPack. If you are also using the
CompoPack then you have a choice to make:

(1) Do nothing. You'll run a chance of getting duplicate POIs close to each
other in vanilla settlements. Some will be from the CompoPack and some will be
from this modlet. They're likely to be slightly different. This is the easiest
choice to accomplish.

(2) Remove this modlet. This will eliminate the chance of duplication in
vanilla settlements, but you'll probably be using slightly older POIs and you
might be missing a few new POIs.

(3) Remove the "by_ZZTong" files found in the CompoPack's folders of POIs for
vanilla settlements. Leave the "by_ZZTong" POIs in all of the CompoPack's
custom settlements. This gives you the best combination, but involves the most
work.

CONFLICTS: (Overhaul Mods)

Overhaul Mods make extensive changes to the game and I cannot give you a recipe
for how to include these POIs. I need to know specifics. Sometimes an Overhaul
Mod needs to change the POIs and sometimes they don't. Sometimes an Overhaul
Mod knows how to find content in a modlet, and sometimes it doesn't.

POI NOTES:

If you'd like extra information about each POI, check out the ABOUT.txt file
also located in this directory. I decided to put all the 'behind the scenes'
stuff there.

DECORATIONS

Decorations are not questable POIs, but they do not take the place of POIs on
your map so you're not missing anything. All of the full POIs are questable.
Beware, some of the Hunters Traps are deadly. If you do not want these to be
included in your map then edit/remove the biomes.xml file found in the Mod's
config directory.

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

Finally, special thanks to Stallionsden and Battlepapi of CompoPack fame, plus
any and all who lurk on in the #prefabbers-hangout Discord channel. Their
guidance throughout the CompoPack submission process and advice via the
CompoPack Discord channels taught me a lot about 7D2D Prefabs, the Prefab
Editor, game performance issues, and more. You're awesome!

RELEASE NOTES: (Newest to Oldest)

A20.5-ZZ010 - Converted 13 field parts into rural POIs with dig quests.
Added Car_Wash_01, Trailer_01, and Trailer_Park_02. Added four rural Tiles.
The Apartment_02 landlord has finally painted the place. Yeeesh!
Fixed a bug in Ranch_01 part list. Fixed a bug in Farm_08. Fixed three
Storm Cellar Parts that had some weird layer of stone inserted in them.
Water Tower Parts now have water. What a novel concept.

A20.5 - ZZ009 - Added Dog_Park_01 rural filler. (Beware of the Dog)
Added NTT_Hub_01 and NTT_HQ_01.
Added Survivor_Base_Ruin_01 which has special purpose (see ABOUT.txt).
Added a Gateway Tile and a bunch of Parts to allow for lots of possabilities.
Added some decorations that look like ruined horde bases.
Re-rebalanced loot in Tier 5's because I really screwed those up.
Re-rebalanced loot in Masonry_01 and Cement_Plant_01. Still too much cement.
Removed fetch quests from Tiers 3, 4, and 5. Apparently they're too easy.
Applied numerous bug fixes spotted by the CP's eagle-eyed testers.

A20.5 - ZZ008 - Fixed numerous bugs and rebalanced loot. Added
rwg_tile_downtown_intersection_zztong_01 and Intersection_01, Intersection_02
and Intersection_03 to go with it. Added Ranch_01 and Vault_K9_01.
Added all my custom Parts because parts are cool, parts are wonderful.
Spinkled Parts into many existing POIs for some subtle variety.
A couple of POIs changed tiers. Added decorations for the Wasteland.

Introduced this modlet to GitHub for my own sanity and peace of mind.
This should have no effect on modlet distribution, but may open up options for
those who work on other projects, plus it gives me a nice backup location.
I do NOT recommend consumers of this modlet pull from the head of main branch.

Introduced this modlet to the GPLv3 license. See LICENSE.TXT and the
LICENSE-NOTES.txt files for details. It should not represent a significant
change for those of you who repackage, or curate, this modlet's content.

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
