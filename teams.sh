#!/bin/bash
# Don't use this it is so slow
for i in {1..1000}
do
   ../../pokemon-showdown/pokemon-showdown generate-team | ../../pokemon-showdown/pokemon-showdown json-team >> $1
done
