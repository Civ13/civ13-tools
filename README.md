# Tools
This repo is an assortment of tools to help the development of [Civ13 Typespess](https://github.com/Civ13/civ13-typespess).

Before using the tools, edit the `config.txt` file with your game's folders.

Most of the tools are in python so you will need it installed. You will also need node.js for `dmi2png-ts` and `object-fetcher` (since it requires `dmi2png-ts`).

The `byond-hoster` tool requires an installation of BYOND.


## [unused-files-finder](https://github.com/Civ13/civ13-tools/tree/master/unused-files-finder)
This program indexes image and sound assets and then checks for mentions in the code, returning a list of orphaned files. It also lets you delete them automatically (altough you probably shouldn't)

## [dmi2png-ts](https://github.com/Civ13/civ13-tools/tree/master/dmi2png-ts)
Convert BYOND dmi's into a png and a json file with the metadata.

## [object-fetcher](https://github.com/Civ13/civ13-tools/tree/master/object-fetcher)
Grab civ13's DMI assets and convert them to png/json using the `dmi2png-ts` tool. Then writes .atom files listing the objects it creates.

## [byond-hoster](https://github.com/Civ13/civ13-tools/tree/master/byond-hoster)
This makes it possible for people to use BYOND to connect to civ13's TypeSpess though DreamDaemon. The server will appear on the Hub too.

## [recipe-converter](https://github.com/Civ13/civ13-tools/tree/master/recipe-converter)
Converts the `material_recipes.txt` file into .crafting CSON files that can be read by Typespess.

## [recipe-consolidator](https://github.com/Civ13/civ13-tools/tree/master/recipe-consolidator)
Runs both `object-fetcher` and `recipe-converter`, then checks which objects listed in the .crafting files have been created in the `object-fetcher`'s .atom files. Then it removes the ones that are orphaned (no template exists).