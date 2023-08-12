#!/usr/bin/bash
# placement-percent.bash <PATH-TO-WORLD>

PATH=$1
cd "$PATH"
totalPOIs=`/usr/bin/grep "model" prefabs.xml | /usr/bin/grep -v "part_" | /usr/bin/grep -v "rwg_tile_" | /usr/bin/wc -l`
zzPOIs=`/usr/bin/grep "model" prefabs.xml | /usr/bin/grep -v "part_" | /usr/bin/grep -v "rwg_tile_" | /usr/bin/grep "zztong_" | /usr/bin/wc -l`
vanillaPOIs=`/usr/bin/echo "$totalPOIs-$zzPOIs" | /usr/bin/bc`

zzPerc=`echo "scale=4; $zzPOIs/$totalPOIs" | /usr/bin/bc`

echo " Vanilla POIs: $vanillaPOIs"
echo "      ZZ POIs: $zzPOIs"
echo "   Total POIs: $totalPOIs"
echo ""
echo "ZZ Percentage: $zzPerc"
