#!/bin/bash

for i in {1..1000}
do
   ../../pokemon-showdown/pokemon-showdown generate-team | ../../pokemon-showdown/pokemon-showdown json-team >> teams.txt
done
