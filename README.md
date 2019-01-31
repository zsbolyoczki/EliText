# EliText


Text based space trading game based on David Braben and Ian Bell's Elite (https://en.wikipedia.org/wiki/Elite_(video_game)).

Run it with python 3.

Tested on:
* Linux Mint 19
* FreeBSD 12
* Windows (works with some unexpected minor issues)




# Gameplay

When starting the game it either asks for the new Commander's name or asks to load a previously saved game.
In case of a new game player starts their adventure in the hangar of the the initial starystem's space station with a standard lightly armed Cobra Mk III ship, 100 credit and fuel good for 10 lightyears of travel.

In the game player is tarveling between starsystems, trading goods and fights other merchants and pirates.


## Locations

**Hangar** is the main place of every station. From here player can go to the **Dockyard** to refuel, repair or improve their space ship. Also the **online market app** is available from here where player can buy and sell goods. 

**Space near the station** is a place where player initiates space jump and where the player arrives after a jump.

Occassionally the space jump is interrupted by **asteroid fields** which can be mined when the ship is equipped with mining tool.

**Space** itself is a very busy location with pirates, corrupt police and strange anomalies.


## Trading

To trade log in to the station's market app and enter the ID of the goods and the amount you want to buy/sell.


## Space fight

Sometimes player is attacked by pirates. 

The fight is round based and player has to beat the hostile ships one by one in a game called "Asteroid-Hull-Laser" (very similar to "rock-paper-scissors"). 

In every round if any of the fighting ships have missiles, they shoot them, otherwise they shoot with laser.
In every round if any of the fighting ships have flare, they release it automatically to disctract incoming missiles.
After every victory player's kill count increases and gains better ranking.
Also a small amount of bounty is paid.

