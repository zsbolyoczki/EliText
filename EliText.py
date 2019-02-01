

# -*- coding: utf-8 -*-

import sys
import pickle  # for saving GAME.
import os  # for loading GAME.
import random
import time
import math
import getpass  # to get username


class Game(object):
    def __init__(self, pcommander_name, pcommander_combat_rating, pcommander_legal_status, pcommander_credit, pship_type,
                 pship_hull, pship_max_hull, pship_docking_computer, spship_fuel, pship_max_fuel, pship_docking_computerstatus,
                 pgame_position, pmanual_docking_success_rate, pjump_count, pfight_count, pkill_count, pship_cargo,
                 pship_max_cargo, pcurrent_starystem, pship_missile_count, pship_max_missile_count, plightyears_traveled,
                 pship_mining_tool, pship_track, pship_flare_count, pship_max_flare_count):

        # @todo: add time spent with game
        self._commander_name = pcommander_name
        self._commander_combat_rating = pcommander_combat_rating
        self._commander_legal_status = pcommander_legal_status
        self._commander_credit = pcommander_credit
        self._ship_type = pship_type
        self._ship_hull = pship_hull
        self._ship_max_hull = pship_max_hull
        self._ship_docking_computer = pship_docking_computer
        self._ship_fuel = spship_fuel
        self._ship_max_fuel = pship_max_fuel
        self._ship_docking_computerstatus = pship_docking_computerstatus
        self._game_position = pgame_position
        self._manual_docking_success_rate = pmanual_docking_success_rate
        self._jump_count = pjump_count
        self._fight_count = pfight_count
        self._kill_count = pkill_count
        self._ship_cargo = pship_cargo
        self._ship_max_cargo = pship_max_cargo
        self._current_starystem = pcurrent_starystem
        self._ship_missile_count = pship_missile_count
        self._ship_max_missile_count = pship_max_missile_count
        self._lightyears_traveled = plightyears_traveled
        self._ship_mining_tool = pship_mining_tool
        self._ship_track = pship_track
        self._ship_flare_count = pship_flare_count
        self._ship_max_flare_count = pship_max_flare_count

    @property
    def commander_name(self):
        return self._commander_name

    @commander_name.setter
    def commander_name(self, value):
        self._commander_name = value
        return

    @property
    def commander_combat_rating(self):
        return self._commander_combat_rating

    @commander_combat_rating.setter
    def commander_combat_rating(self, value):
        self._commander_combat_rating = value
        return

    @property
    def commander_legal_status(self):
        return self._commander_legal_status

    @commander_legal_status.setter
    def commander_legal_status(self, value):
        self._commander_legal_status = value
        return

    @property
    def commander_credit(self):
        return self._commander_credit

    @commander_credit.setter
    def commander_credit(self, value):
        self._commander_credit = value
        return

    @property
    def ship_type(self):
        return self._ship_type

    @ship_type.setter
    def ship_type(self, value):
        self._ship_type = value
        return

    @property
    def ship_hull(self):
        return self._ship_hull

    @ship_hull.setter
    def ship_hull(self, value):
        self._ship_hull = value
        return

    @property
    def ship_max_hull(self):
        return self._ship_max_hull

    @ship_max_hull.setter
    def ship_max_hull(self, value):
        self._ship_max_hull = value
        return

    @property
    def ship_docking_computer(self):
        return self._ship_docking_computer

    @ship_docking_computer.setter
    def ship_docking_computer(self, value):
        self._ship_docking_computer = value
        return

    @property
    def ship_fuel(self):
        return self._ship_fuel

    @ship_fuel.setter
    def ship_fuel(self, value):
        self._ship_fuel = value
        return

    @property
    def ship_max_fuel(self):
        return self._ship_max_fuel

    @ship_max_fuel.setter
    def ship_max_fuel(self, value):
        self._ship_max_fuel = value
        return

    @property
    def ship_docking_computerstatus(self):
        return self._ship_docking_computerstatus

    @ship_docking_computerstatus.setter
    def ship_docking_computerstatus(self, value):
        self._ship_docking_computerstatus = value
        return

    @property
    def game_position(self):
        return self._game_position

    @game_position.setter
    def game_position(self, value):
        self._game_position = value
        return

    @property
    def manual_docking_success_rate(self):
        return self._manual_docking_success_rate

    @manual_docking_success_rate.setter
    def manual_docking_success_rate(self, value):
        self._manual_docking_success_rate = value
        return

    @property
    def jump_count(self):
        return self._jump_count

    @jump_count.setter
    def jump_count(self, value):
        self._jump_count = value
        return

    @property
    def fight_count(self):
        return self._fight_count

    @fight_count.setter
    def fight_count(self, value):
        self._fight_count = value
        return

    @property
    def kill_count(self):
        return self._kill_count

    @kill_count.setter
    def kill_count(self, value):
        self._kill_count = value
        return

    @property
    def ship_cargo(self):
        return self._ship_cargo

    @ship_cargo.setter
    def ship_cargo(self, value):
        self._ship_cargo = value
        return

    @property
    def ship_max_cargo(self):
        return self._ship_max_cargo

    @ship_max_cargo.setter
    def ship_max_cargo(self, value):
        self._ship_max_cargo = value
        return

    @property
    def current_starystem(self):
        return self._current_starystem

    @current_starystem.setter
    def current_starystem(self, value):
        self._current_starystem = value
        return

    @property
    def ship_missile_count(self):
        return self._ship_missile_count

    @ship_missile_count.setter
    def ship_missile_count(self, value):
        self._ship_missile_count = value
        return

    @property
    def ship_max_missile_count(self):
        return self._ship_max_missile_count

    @ship_max_missile_count.setter
    def ship_max_missile_count(self, value):
        self._ship_max_missile_count = value
        return

    @property
    def lightyears_traveled(self):
        return self._lightyears_traveled

    @lightyears_traveled.setter
    def lightyears_traveled(self, value):
        self._lightyears_traveled = value
        return

    @property
    def ship_mining_tool(self):
        return self._ship_mining_tool

    @ship_mining_tool.setter
    def ship_mining_tool(self, value):
        self._ship_mining_tool = value
        return

    @property
    def ship_track(self):
        return self._ship_track

    @ship_track.setter
    def ship_track(self, value):
        self._ship_track.append(int(value))
        return


    @property
    def ship_flare_count(self):
        return self._ship_flare_count

    @ship_flare_count.setter
    def ship_flare_count(self, value):
        self._ship_flare_count = value
        return

    @property
    def ship_max_flare_count(self):
        return self._ship_max_flare_count

    @ship_max_flare_count.setter
    def ship_max_flare_count(self, value):
        self._ship_max_flare_count.append(int(value))
        return




class CargoItem(object):
    def __init__(self, pgoodsid, pamount):
        self._goodsid = pgoodsid
        self._amount = pamount

    @property
    def goodsid(self):
        return self._goodsid

    @goodsid.setter
    def goodsid(self, value):
        self._goodsid = value
        return

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        return

class EnemyShip(object):
    def __init__(self, ptype, phull, pmissile):
        self.ship_type = ptype
        self.ship_hull = phull
        self.missile = pmissile

    @property
    def ship_type(self):
        return self._ship_type

    @ship_type.setter
    def ship_type(self, value):
        self._ship_type = value
        return

    @property
    def ship_hull(self):
        return self._ship_hull

    @ship_hull.setter
    def ship_hull(self, value):
        self._ship_hull = value
        return


class GameConfig(object):
    def __init__(self, pclearscreen, pmenuborder):
        self._clearscreen = pclearscreen
        self._menuborder = pmenuborder

    @property
    def clearscreen(self):
        return self._clearscreen

    @clearscreen.setter
    def clearscreen(self,value):
        self._clearscreen = value
        return

    @property
    def menuborder(self):
        return self._menuborder

    @menuborder.setter
    def menuborder(self, value):
        self._menuborder = value
        return

class Starsystem(object):
    def __init__(self, psystemname, pstationname, pposx, pposy, peconomy, ppolitics, ptechlevel, pdockingfee,
                 pfuelprice, phullrepairprice, pgoods, pdockingcomputerprice, pminingtoolprice, pmissileprice,
                 pflareprice):
        self._systemname = psystemname
        self._stationname = pstationname
        self._posx = pposx
        self._posy = pposy
        self._economy = peconomy
        self._politics = ppolitics
        self._techlevel = ptechlevel  # 1-5 defines hull fixing price and fuel price
        self._dockingfee = pdockingfee
        self._fuelprice = pfuelprice
        self._hullrepair = phullrepairprice
        self._goods = pgoods
        self._dockingcomputerprice = pdockingcomputerprice
        self._miningtoolprice = pminingtoolprice
        self._missileprice = pmissileprice
        self._flareprice = pflareprice

    @property
    def systemname(self):
        return self._systemname

    @systemname.setter
    def systemname(self, value):
        self._systemname = value
        return

    @property
    def stationname(self):
        return self._stationname

    @stationname.setter
    def stationname(self, value):
        self._stationname = value
        return

    @property
    def posx(self):
        return self._posx

    @posx.setter
    def posx(self, value):
        self._posx = value
        return

    @property
    def posy(self):
        return self._posy

    @posy.setter
    def posy(self, value):
        self._posy = value
        return

    @property
    def economy(self):
        return self._economy

    @economy.setter
    def economy(self, value):
        self._economy = value
        return

    @property
    def politics(self):
        return self._politics

    @politics.setter
    def politics(self, value):
        self._politics = value
        return

    @property
    def techlevel(self):
        return self._techlevel

    @techlevel.setter
    def techlevel(self, value):
        self._techlevel = value
        return

    @property
    def dockingfee(self):
        return self._dockingfee

    @dockingfee.setter
    def dockingfee(self, value):
        self._dockingfee = value
        return

    @property
    def fuelprice(self):
        return self._fuelprice

    @fuelprice.setter
    def fuelprice(self, value):
        self._fuelprice = value
        return

    @property
    def hullrepair(self):
        return self._hullrepair

    @hullrepair.setter
    def hullrepair(self, value):
        self._hullrepair = value
        return

    @property
    def goods(self):
        return self._goods

    @goods.setter
    def goods(self, value):
        self._goods = value
        return

    @property
    def dockingcomputerprice(self):
        return self._dockingcomputerprice

    @dockingcomputerprice.setter
    def dockingcomputerprice(self, value):
        self._dockingcomputerprice = value
        return

    @property
    def miningtoolprice(self):
        return self._miningtoolprice

    @miningtoolprice.setter
    def miningtoolprice(self, value):
        self._miningtoolprice = value
        return

    @property
    def missileprice(self):
        return self._missileprice

    @missileprice.setter
    def missileprice(self, value):
        self._missileprice = value
        return


    @property
    def flareprice(self):
        return self._flareprice

    @flareprice.setter
    def flareprice(self, value):
        self._flareprice = value
        return



class Goods(object):
    def __init__(self, pgoodsid, pgoodslocalprice, pgoodslegal, pgoodsamount):
        self._goodsid = pgoodsid
        self._goodslocalprice = pgoodslocalprice
        self._goodslegal = pgoodslegal
        self._goodsamount = pgoodsamount

    @property
    def goodsid(self):
        return self._goodsid

    @goodsid.setter
    def goodsid(self, value):
        self._goodsid = value
        return

    @property
    def goodslocalprice(self):
        return self._goodslocalprice

    @goodslocalprice.setter
    def goodslocalprice(self, value):
        self._goodslocalprice = value
        return

    @property
    def goodslegal(self):
        return self._goodslegal

    @goodslegal.setter
    def goodslegal(self, value):
        self._goodslegal = value

    @property
    def goodsamount(self):
        return self._goodsamount

    @goodsamount.setter
    def goodsamount(self, value):
        self._goodamount = value
        return


GOODS = ["ALIEN ITEMS", "ALLOYS", "COMPUTERS", "FOOD", "FURS", "GEM-STONES", "GOLD", "LIQUOR/WINES", "LUXURIES",
         "MACHINERY", "MINERALS", "NARCOTICS", "PLATINUM", "RADIOACTIVES", "SLAVES", "TEXTILES", "WEAPONS"]

GOODS_DEFAULT_PRICES = [80, 5, 15, 7, 7, 10, 10, 8, 20, 10, 5, 25, 12, 8, 75, 5, 30]

INIT_STARSYSTEM_NAMES = ["ASIMOV", "CLARKE", "LEM", "BRABEN", "BELL-I"]

STARSYSTEM_NAMES = ["ALAZA", "ANLAMA", "AONA", "ARARUS", "ARAZAES", "ARONAR", "ARUSQUDI", "ARUSZATI", "ATAGE", "ATRISO",
                    "CPLUS-IV", "BEMAERA", "BIARGE", "BIISZA", "BIORIS", "CEINZALA", "CEMAVE", "CEVEGE", "DIGEBITI",
                    "DISO", "DIUSREZA", "EMIL", "ENCERESO", "ENGEMA", "ERBITI", "ERLAZA", "ESTEONBI", "GEINONA",
                    "INERA",
                    "INONRI", "ISATRE", "ISINOR", "ISVEVE", "LAEDEN", "LARAIS", "LAVE", "LEESTI", "LELEER", "LEONED",
                    "MAISES", "ONLEMA", "ONRIRA", "ONTIAT", "ORERVE", "ORESEREN", "ORESLE", "ORESQU", "ORESRI",
                    "ORRERE", "QUBE", "QUCERERE", "QUITRI", "QUZADI", "RATEEDAR", "REBIA", "REESDICE", "REGEATGE",
                    "REORTE", "RIEDQUAT", "SOINUSTE", "SOLADIES", "SORI", "SOTERA", "SOTIQU", "TEAATIS", "TIBECEA",
                    "TIONISLA", "USRAREMA", "USZAA", "VEBEGE", "VETITICE", "XEER", "XEQUQUTI", "ZAALELA", "ZAONCE"]

COMBAT_RATING = ["ROOKIE", "MOSTLY HARMLESS", "AVERAGE", "COMPETENT", "DANGEROUS", "ELITE"]

LEGAL_STATUS = ["CLEAN", "OFFENDER", "FUGITIVE"]

# @todo: more ship types
SHIP_TYPE = ["Cobra Mk III"]

# https://forums.frontier.co.uk/showthread.php/57296-Ships-from-the-original-Elite
# http://wiki.alioth.net/index.php/Classic_Elite_ships_firepower
# http://wiki.alioth.net/index.php/Classic_Elite_ships
# http://wiki.alioth.net/index.php/Ship_data_table_here

ENEMY_SHIP_TYPE = ["RAPTOR", "VIPER", "TROLL"]

# ECONOMY = ["AGRICULTURAL", "INDUSTRIAL"]
ECONOMY = ["AGRICULTURAL", "INDUSTRIAL", "TECHNOLOGICAL"]

POLITICS = ["CHAOTIC", "NEUTRAL", "LAWFUL"]

ENVTEXT_STATION_PEACEFUL = ["The smell is strange here.", "Gravity is strange here. Better be careful.",
                            "Loud music plays in the background.",
                            "All kind of space travelling species are everywhere."]

ENVTEXT_SPACE_PEACEFUL = ["The stars are shining in the distance.", "The Stars, Like Dust",
                          "The stars are shining like diamond dust. Hmmm... Diamonds...", "Not much happens.",
                          "Other ships are coming and going. Space is busy today."]
ENVTEXT_SPACE_HOSTILE = [""]

GAME_START_TIME = time.time()

# @todo: probably should be a part of "Game" class
STARSYSTEMS = []

game_config = GameConfig(1, "_")

DEFAULT_MANUAL_DOCKING_SUCCESS_RATE = 80
DEFAULT_FUEL_PRICE = 10  # PER 1 LIGHTYEAR
DEFAULT_HULL_FIXING_PRICE = 1  # PER 10% HULL

cargo = []
for c in range(0, len(GOODS)):
    cargoitem = CargoItem(c, 0)
    cargo.append(cargoitem)

INIT_COMMANDER_NAME = ""
INIT_COMMANDER_COMBAT_RATING = 0
INIT_COMMANDER_LEGAL_STATUS = 0
INIT_COMMANDER_CREDIT = 100
INIT_SHIP_TYPE = 0
INIT_SHIP_HULL = 100
INIT_SHIP_MAX_HULL = 100
INIT_SHIP_DOCKING_COMPUTER = 0
INIT_SHIP_FUEL = 10
INIT_SHIP_MAX_FUEL = INIT_SHIP_FUEL
INIT_SHIP_DOCKING_COMPUTER_STATUS = 1
INIT_SHIP_GAME_POSITION = "STATION-HANGAR"
INIT_SHIP_MANUAL_DOCKING_SUCCESS_RATE = DEFAULT_MANUAL_DOCKING_SUCCESS_RATE
INIT_SHIP_JUMP_COUNT = 0
INIT_SHIP_FIGHT_COUNT = 0
INIT_SHIP_KILL_COUNT = 0
INIT_SHIP_CARGO = cargo
INIT_SHIP_MAX_CARGO = 100
INIT_SHIP_CURRENT_STARSYSTEM = 0
INIT_SHIP_MISSILE_COUNT = 0
INIT_SHIP_MAX_MISSILE_COUNT = 5
INIT_SHIP_LIGHTYEARS_TRAVELED = 0
INIT_SHIP_MININGTOOL = 0
INIT_SHIP_TRACK = [0]
INIT_SHIP_FLAIR_COUNT = 0
INIT_SHIP_MAX_FLAIR_COUNT = 3

GAME = Game(INIT_COMMANDER_NAME, INIT_COMMANDER_COMBAT_RATING, INIT_COMMANDER_LEGAL_STATUS, INIT_COMMANDER_CREDIT,
            INIT_SHIP_TYPE, INIT_SHIP_HULL, INIT_SHIP_MAX_HULL, INIT_SHIP_DOCKING_COMPUTER, INIT_SHIP_FUEL,
            INIT_SHIP_MAX_FUEL, INIT_SHIP_DOCKING_COMPUTER_STATUS, INIT_SHIP_GAME_POSITION,
            INIT_SHIP_MANUAL_DOCKING_SUCCESS_RATE, INIT_SHIP_JUMP_COUNT, INIT_SHIP_FIGHT_COUNT, INIT_SHIP_KILL_COUNT,
            INIT_SHIP_CARGO, INIT_SHIP_MAX_CARGO, INIT_SHIP_CURRENT_STARSYSTEM, INIT_SHIP_MISSILE_COUNT,
            INIT_SHIP_MAX_MISSILE_COUNT, INIT_SHIP_LIGHTYEARS_TRAVELED, INIT_SHIP_MININGTOOL, INIT_SHIP_TRACK,
            INIT_SHIP_FLAIR_COUNT, INIT_SHIP_MAX_FLAIR_COUNT)

LINE_WIDTH = 85

LASER_DAMAGE_MIN = 10
LASER_DAMAGE_MAX = 25
MISSILE_DAMAGE_MIN = 40
MISSILE_DAMAGE_MAX = 70


def GenerateGalacticMap():
    global STARSYSTEMS

    STARSYSTEMS.clear()
    MAP_MAX_X = round(len(STARSYSTEM_NAMES) * 1, 0)
    MAP_MAX_Y = round(len(STARSYSTEM_NAMES) * 1, 0)

    # generate data for initial station
    SYSNAME = random.choice(INIT_STARSYSTEM_NAMES)
    SYSPOSX = random.randint(0, MAP_MAX_X)
    SYSPOSY = random.randint(0, MAP_MAX_Y)
    SYSECONOMY = random.choice(["", "POOR", "RICH"]) + ' ' + random.choice(ECONOMY)
    SYSECONOMY = SYSECONOMY.lstrip()
    SYSPOLITICS = random.choice(POLITICS)  # POLITICS, TEXT
    SYSTECHLEVEL = random.randint(1, 5)  # TECH LEVEL, INT
    SYSDOCKINGFEE = random.randint(0, 100) / 50  # DOCKING FEE, FLOAT
    SYSFUELPRICE = 1
    SYSHULLFIXPRICE = 1
    MISSILEPRICE = random.randint(5, 10)
    DOCKINGCOMPUTERPRICE = random.randint(120, 150)
    MININGTOOLPRICE = random.randint(50, 75)
    FLAREPRICE = random.randint(5, 10)

    SYSGOODS = []
    for G in range(0, len(GOODS)):
        GOODS_PRICE_MODIFIER = round(random.randint(75, 125) / 100, 2)
        ACTUAL_PRICE = round(GOODS_DEFAULT_PRICES[G] * GOODS_PRICE_MODIFIER, 2)
        SYSGOODS.append(Goods(G, ACTUAL_PRICE, 1, 0))

    s = Starsystem(SYSNAME, SYSNAME, SYSPOSX, SYSPOSY, SYSECONOMY, SYSPOLITICS, SYSTECHLEVEL, SYSDOCKINGFEE,
                   SYSFUELPRICE, SYSHULLFIXPRICE, SYSGOODS, DOCKINGCOMPUTERPRICE, MININGTOOLPRICE, MISSILEPRICE,
                   FLAREPRICE)

    STARSYSTEMS.append(s)

    # determine if there are at least 4 star systems within range
    CURRENTPOSX = STARSYSTEMS[0].posx
    CURRENTPOSY = STARSYSTEMS[0].posy

    SYSTEMS_IN_RANGE = 0

    TEMP_STARSYSTEMS = []
    while SYSTEMS_IN_RANGE < 4:

        TEMP_STARSYSTEMS.clear()
        # generate data for the rest of the world
        for i in range(0, len(STARSYSTEM_NAMES)):
            SYSNAME = STARSYSTEM_NAMES[i]
            SYSPOSX = random.randint(random.randint(3, 6), MAP_MAX_X)
            SYSPOSY = random.randint(random.randint(3, 6), MAP_MAX_Y)
            SYSECONOMY = random.choice(["", "POOR", "RICH"]) + ' ' + random.choice(ECONOMY)
            SYSECONOMY = SYSECONOMY.lstrip()
            SYSPOLITICS = random.choice(POLITICS)  # POLITICS, TEXT
            SYSTECHLEVEL = random.randint(1, 5)  # TECH LEVEL, INT
            SYSDOCKINGFEE = random.randint(0, 100) / 50  # DOCKING FEE, FLOAT
            SYSFUELPRICE = 1
            SYSHULLFIXPRICE = 1
            MISSILEPRICE = random.randint(5, 10)
            DOCKINGCOMPUTERPRICE = random.randint(120, 150)
            MININGTOOLPRICE = random.randint(50, 75)
            FLAREPRICE = random.randint(5, 10)

            SYSGOODS = []
            for G in range(0, len(GOODS)):
                GOODS_PRICE_MODIFIER = round(random.randint(75, 115) / 100, 2)
                SYSTEM_PRICE = round(GOODS_DEFAULT_PRICES[G] * GOODS_PRICE_MODIFIER, 2)
                SYSGOODS.append(Goods(G, SYSTEM_PRICE, 1, 0))

            s = Starsystem(SYSNAME, SYSNAME, SYSPOSX, SYSPOSY, SYSECONOMY, SYSPOLITICS, SYSTECHLEVEL, SYSDOCKINGFEE,
                           SYSFUELPRICE, SYSHULLFIXPRICE, SYSGOODS, DOCKINGCOMPUTERPRICE, MININGTOOLPRICE, MISSILEPRICE,
                           FLAREPRICE)

            TEMP_STARSYSTEMS.append(s)

            D = round(math.sqrt(
                (CURRENTPOSX - SYSPOSX) * (CURRENTPOSX - SYSPOSX) + (CURRENTPOSY - SYSPOSY) * (CURRENTPOSY - SYSPOSY)),
                0)

            if D <= GAME.ship_fuel:
                SYSTEMS_IN_RANGE += 1

    STARSYSTEMS += TEMP_STARSYSTEMS
    return


def _print(text):
    print(" " + str(text))
    return


def ShowTime(t1, t2):
    _print("Time wasted from your life: " + str(int(t2) - int(t1)) + "s")
    return


def ClearScreen():
    if game_config.clearscreen == 1:
        os.system("clear")
    return


def QuitGame():
    _print("" * 2)
    ShowTime(GAME_START_TIME, time.time())
    _print("")
    _print("Bye.")
    _print("")
    sys.exit()

def ShowFooter():
    _print(game_config.menuborder * LINE_WIDTH)
    _print("? - Stats | . - Save game | Q - Exit game | X - Exit game (and save)")
    _print("")
    return

def SaveAndExit():
    _print("" * 2)
    SaveGame()
    QuitGame()
    return


def CalculateDocking():
    #
    # returns the percentage of hull damage
    #

    # does the ship have docking computer
    if GAME.ship_docking_computer:
        # docking computer is present, only 5% chance of any problem
        if random.randint(0, 100) > 5:
            # no problems at all
            DAMAGE = 0
        else:
            # 20% chance that some minor thing happens
            if random.randint(0, 100) <= 20:
                # minimal damage
                DAMAGE = random.randint(1, 10)
            else:
                # something went terribly wrong...
                DAMAGE = 100
    else:
        # docking computer is not available
        if random.randint(0, 100) >= (100 - GAME.manual_docking_success_rate):
            DAMAGE = 0
        else:
            # 20% chance that some minor thing happens
            if random.randint(0, 100) <= 20:
                # minimal damage
                DAMAGE = random.randint(1, 10)
            else:
                # something went terribly wrong...
                DAMAGE = 100

    return DAMAGE


def CrashedDuringDocking():
    ClearScreen()
    _print("\n" * 2)
    _print("During the maneuvre you crash into the docking station.")
    _print("The hull tears open and the precious oxygene leaves the ship with a loud boom.")
    _print("You suffocate, freeze and boil at the same time.")
    _print("You are dead.")
    _print("")
    return


def GenerateSpaceEvent():

    RETURNCODE=""
    if random.randint(0, 10) < 2:  # asteroids or space fight in the distance
        if random.randint(0, 10) < 2:
            RETURNCODE = 4 # space fight in the distance
        else:
            if random.randint(0, 10) < 2:
                RETURNCODE = 1 # asteroids
    else:
        if random.randint(0,10) < 4:  # police or pirates
            POLITICS = STARSYSTEMS[GAME.current_starystem].politics
            if POLITICS == "CHAOTIC":
                if random.randint(0, 10) <= 6:
                    if random.randint(0, 10) <= 3:
                        RETURNCODE = 3  # corrupt police
                    else:
                        RETURNCODE = 0  # !!! pirates !!!
            elif POLITICS == "NEUTRAL":
                if random.randint(0, 10) <= 4:  # police
                    RETURNCODE = 2
            elif POLITICS == "LAWFUL":
                if random.randint(0, 10) <= 2:  # police
                    RETURNCODE = 2
    
    return RETURNCODE


def SpaceFightInTheDistance():

    ClearScreen()
    _print("" * 3)
    _print("Your travel is interrupted by a distant space fight.")
    _print("It is unclear whether it is a prirate attack or just a minor misunderstanding between other merchants.")
    #@todo: when higher rank join the fight
    _print("You better leave.")
    _print("")
    _print("")
    input("ENTER")
    return


def PoliceInvestigation():

    ClearScreen()
    _print("" * 3)
    # @todo: find illegal stuff, fight police ship
    _print("You stumble upon a police ship.")
    _print("You are instructed to let the police ship's squad board your ship to search for illegal goods.")
    _print("")
    _print("They found nothing and let you go.")
    _print("")
    _print("")
    input("ENTER")

    return

def CorruptPoliceInvestigation():

    ClearScreen()
    _print("" * 3)
    # @todo: find illegal stuff, fight police ship
    _print("You stumble upon a police ship.")
    _print("Blue and red lights everywhere.")
    _print("You are instructed to let the police ship's squad board your ship to search for illegal goods.")
    _print("")
    FEE=int(random.randint(1,round(GAME.commander_credit * 0.2,0)))
    if random.randint(1,2) == 1:
        REASON="your \"windshield is dirty\""
    else:
        REASON="your \"left turn signal didn't work\""
    _print("")
    _print("They found nothing but charge you for " + str(FEE)+ " credit because " + REASON +".")
    _print("What a scum. But you just smile and hope the police ship's engine will blow up soon.")
    _print("")
    _print("")
    GAME.commander_credit-=FEE
    input("ENTER")

    return


def GameOver():
    global GAME

    _print("Game Over")
    _print("")
    if input(" Do you want to see the game statistics? [Y/n] ").upper() != "N":
        MenuShowStats(GAME, "game_over")
    _print("")
    QuitGame()

    return


def NewOrLoad():

    global GAME
    global STARSYSTEMS
    
    # there is no previous GAME.
    if not os.path.isfile("./game.save"):
        NewGame()
    else:
        _print("")
        ANSWER = input(" Load previous game? [Y/n] ").upper()
        if ANSWER == "" or ANSWER == "Y":
            with open('game.save', 'rb') as fin:
                GAME=pickle.load(fin)
                STARSYSTEMS=pickle.load(fin)
            fin.close()
        else:
            NewGame()
    
    return


"""
===============================================================
SHOWS STAR MAP (NEAREST SYSTEMS)
===============================================================
"""


def ShowStarMap():
    _print("\n" * 2)
    _print("Starsystems within range (fuel is good for " + str(round(GAME.ship_fuel, 0)) + " lightyears):")
    _print("")

    CURRENTX = STARSYSTEMS[GAME.current_starystem].posx
    CURRENTY = STARSYSTEMS[GAME.current_starystem].posy

    _print('{:>4} {:<15} {:>5}'.format("ID", "NAME", "DISTANCE"))
    NEARSYSTEMS = []
    for i in range(len(STARSYSTEMS)):
        if i != GAME.current_starystem:
            STARSYSTEMX = STARSYSTEMS[i].posx
            STARSYSTEMY = STARSYSTEMS[i].posy
            D = round(math.sqrt((CURRENTX - STARSYSTEMX) * (CURRENTX - STARSYSTEMX) + (CURRENTY - STARSYSTEMY) * (
                    CURRENTY - STARSYSTEMY)), 1)
            if D <= GAME.ship_fuel:
                NEARSYSTEMS.append(i)
                INFO = STARSYSTEMS[i].economy + ' ' + STARSYSTEMS[i].politics + ' WORLD AT TECHLEVEL ' + str(
                    STARSYSTEMS[i].techlevel) + ', DOCKING FEE: ' + str(STARSYSTEMS[i].dockingfee)
                _print('{:>4} {:<15} {:>8} --> {:<25}'.format(i, STARSYSTEMS[i].systemname, D, INFO))


    # @todo: draw ascii starmap

    if not len(NEARSYSTEMS):
        _print("")
        _print("There aren't any STARSYSTEMS you can reach with this few fuel. Go and buy some.")
        _print("")

    _print("")
    _print("R - Return")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" In which system do you want to jump (enter ID or return to the ship's command console) > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    if ANSWER.isdigit():
        if int(ANSWER) not in NEARSYSTEMS:
            ANSWER = ""

    return ANSWER


def SaveGame():


  ClearScreen()

  with open('game.save', 'wb') as fout:
    pickle.dump(GAME, fout)
  fout.close()

  with open('game.save', 'ab') as fout:
    pickle.dump(STARSYSTEMS, fout)
  fout.close()

  _print("" * 3)
  _print("")
  _print("Game saved.")
  _print("")
  _print("")
  input(" ENTER")

  return

def NewGame():

    global GAME

    commander_name = ""
    while commander_name == "":
        commander_name = getpass.getuser()
        commander_name = input(" New Commander: ["+ commander_name.upper() + "]: " )
        if commander_name == "":
            commander_name = getpass.getuser()

    GAME.commander_name = commander_name.upper()



def AsteroidHullLaser():
    E = random.randint(0, 2)
    C = ""
    while C not in ['A', 'H', 'L', 'X']:
        C = input(" Your choice (A, H, L, (X for Escape)): ").upper()

    if C == 'X':
        RESULT = "X"
    else:
        if C == 'A':
            C = 0
        if C == 'H':
            C = 1
        if C == 'L':
            C = 2

        if E == C:
            RESULT = "D"

        if E == 0:
            if C == 1:
                RESULT = "C"
            elif C == 2:
                RESULT = "E"

        if E == 1:
            if C == 0:
                RESULT = "E"
            elif C == 2:
                RESULT = "C"

        if E == 2:
            if C == 0:
                RESULT = "C"
            elif C == 1:
                RESULT = "E"

    return RESULT


def LoadConfig():
   ## _print("LoadConfig() - FIXME")

    return


"""
===============================================================
SPACE FIGHT
===============================================================
"""


def SpaceFight():
    global GAME

    RETURNCODE = ""
    GAME.fight_count += 1

    ClearScreen()
    _print("" * 3)
    _print("The space jump is interrupted by a gravity anomaly and you fall out from hyperspace.")
    _print("")

    # quickly build a handful hostile ships
    enemyships = []
    for i in range(random.randint(1, 3)):
        # type, hull, missiles
        e = EnemyShip(random.choice(ENEMY_SHIP_TYPE), random.randint(50, 100), random.randint(0, 3))
        enemyships.append(e)

    _print("")
    _print("!!! PIRATES !!!")
    _print("")
    if len(enemyships) > 1:
        _print("You are facing " + str(len(enemyships)) + " hostile ships.")
        _print("You have to fight them one by one in a ASTEROID-HULL-LASER game.")
    else:
        _print("You are attacked by a hostile ship.")
        _print("You have to fight it in a ASTEROID-HULL-LASER game.")

    _print("")
    CHOICE = random.randint(0, 5)
    if CHOICE < 2:
        _print("You toss a power metal audio cassette in the player and hit the play button.")
    if CHOICE >= 5:
        _print("You let out a rebel yell and head jump into the battle.")
    _print("")

    ENEMY_SHIP_INDEX = 0

    AHL_RESULT = ""

    while ENEMY_SHIP_INDEX < len(enemyships) and GAME.ship_hull > 0 and AHL_RESULT != "X":

        # fight 'til the end
        while GAME.ship_hull > 0 and enemyships[ENEMY_SHIP_INDEX].ship_hull > 0 and AHL_RESULT != "X":

            _print("")
            _print("Enemy ship #" + str(ENEMY_SHIP_INDEX + 1) + ", type: \"" + enemyships[
                ENEMY_SHIP_INDEX].ship_type + "\", hull: " + str(
                enemyships[ENEMY_SHIP_INDEX].ship_hull))

            AHL_RESULT = AsteroidHullLaser()

            if AHL_RESULT != "X":

                if GAME.ship_missile_count:
                    GAME.ship_missile_count -= 1
                    COMMANDER_DAMAGE = random.randint(MISSILE_DAMAGE_MIN, MISSILE_DAMAGE_MAX)
                    TEXT = "You launched a missile. (" + str(GAME.ship_missile_count) + " left)"
                    _print('{:>80}'.format(TEXT))
                else:
                    COMMANDER_DAMAGE = random.randint(LASER_DAMAGE_MIN, LASER_DAMAGE_MAX)
                    _print("You fired your laser.")
                    if random.randint(1, 5) >= 4:
                        _print("Red and yellow lines draw deadly shapes on the background.")

                if enemyships[ENEMY_SHIP_INDEX].missile:
                    _print("Enemy ship #" + str(ENEMY_SHIP_INDEX + 1) + " launched a missile !!!")

                    # use flare if exists
                    if GAME.ship_flare_count:
                        _print("You have released a flare container. A small white-hot ball of fire is burning behind you.")
                        # 70% chance that the flare distracts the incoming missile
                        if random.randint(0, 100) > 70:
                         ENEMY_DAMAGE = random.randint(MISSILE_DAMAGE_MIN, MISSILE_DAMAGE_MAX)
                         GAME.ship_flare_count -= 1
                        else:
                            ENEMY_DAMAGE = 0
                    enemyships[ENEMY_SHIP_INDEX].missile -= 1
                else:
                    ENEMY_DAMAGE = random.randint(LASER_DAMAGE_MIN, LASER_DAMAGE_MAX)
                    _print("Enemy ship #" + str(ENEMY_SHIP_INDEX + 1) + " fires with laser.")

                _print("")
                # enemy ship wins the round
                if AHL_RESULT == "E":
                    if ENEMY_DAMAGE:
                        GAME.ship_hull -= ENEMY_DAMAGE
                        if GAME.ship_hull < 0:
                           GAME.ship_hull = 0
                        _print("---> Your ship got hit. Hull damage is " + str(ENEMY_DAMAGE) + " points (" + str(
                            GAME.ship_hull) + " left)")
                    else:
                        _print("Ememy shot missed. You ecstatically hit the console with your fist.")

                # commander wins the round
                if AHL_RESULT == "C":
                    enemyships[ENEMY_SHIP_INDEX].ship_hull -= COMMANDER_DAMAGE
                    _print("<--- You hit the enemy ship and caused " + str(COMMANDER_DAMAGE) + " points of damage.")

                # both commander and enemy are lame
                if AHL_RESULT == "D":
                    _print(">---< Both of you missed.")

            if enemyships[ENEMY_SHIP_INDEX].ship_hull <= 0:
                _print("!!! You killed Enemy #" + str(ENEMY_SHIP_INDEX + 1) + " !!!")
                BOUNTY = random.randint(5, 10)
                GAME.commander_credit += BOUNTY
                _print("")
                _print("")
                _print("Well done, space is much safer now.")
                _print("")
                _print("You get a bounty of " + str(BOUNTY) + " credit.")
                _print("")
                _print("")
                GAME.kill_count += 1
                if GAME.kill_count == 1:
                    NEW_COMBAT_RATING = 1
                    GAME.commander_combat_rating = NEW_COMBAT_RATING
                    _print("Wow, your combat rating just upgraded to " + COMBAT_RATING[NEW_COMBAT_RATING] + " !!!")
                    _print("")
                elif GAME.kill_count == 5:
                    NEW_COMBAT_RATING = 2
                    GAME.commander_combat_rating = NEW_COMBAT_RATING
                    _print("You are getting more dangerous. From now on you are " + COMBAT_RATING[NEW_COMBAT_RATING])
                    _print("")
                elif GAME.kill_count == 12:
                    NEW_COMBAT_RATING = 3
                    GAME.commander_combat_rating = NEW_COMBAT_RATING
                    _print(
                        "The Intergalactic Combatrating Committee just sent yo a notification that from now on your rating is " +
                        COMBAT_RATING[NEW_COMBAT_RATING])
                    _print("")
                elif GAME.kill_count == 25:
                    NEW_COMBAT_RATING = 4
                    GAME.commander_combat_rating = NEW_COMBAT_RATING
                    _print("Another victory, another promotion. Your new rating is " + COMBAT_RATING[NEW_COMBAT_RATING])
                    _print("")
                elif GAME.kill_count == 50:
                    NEW_COMBAT_RATING = 5
                    GAME.commander_combat_rating = NEW_COMBAT_RATING
                    _print("You reached " + COMBAT_RATING[NEW_COMBAT_RATING] + " combat rating which is nice.")
                    _print("")
                _print("")
                _print("")

            if GAME.ship_hull <= 0:
                _print("")
                _print("Enemy #" + str(ENEMY_SHIP_INDEX + 1) + " killed you.")
                ENEMY_SHIP_INDEX = 99999
                RETURNCODE = "SPACEFIGHT-GAMEOVER"
            else:
                # next enemy
                ENEMY_SHIP_INDEX += 1

        # end of individual enemy ship loop

    # end of big while loop, end of fight


    if AHL_RESULT == "X":
        _print("")
        if ENEMY_SHIP_INDEX < len(enemyships):
            ENEMY_DAMAGE = random.randint(0, round(GAME.ship_hull * 0.5))
            _print(
                "You try to escape the fight. All the enemy ships fire at you with all their weapons and cause a " + str(
                    ENEMY_DAMAGE) + " points of damage.")
        else:
            ENEMY_DAMAGE = random.randint(0, round(GAME.ship_hull * 0.2))
            _print(
                "You try to escape the fight. The remaining enemy ship fires at you with all its weapons and cause a " + str(
                    ENEMY_DAMAGE) + " points of damage.")
        GAME.ship_hull -= ENEMY_DAMAGE

    # end of fight
    if GAME.ship_hull:

        if AHL_RESULT != "X":
            if random.randint(0, 100) < 35:
                # there is some leftover floating in space
                if GAME.ship_mining_tool:
                    AMOUNT = GAME.ship_max_cargo - CargoCount()
                    if AMOUNT:
                        ALLOY_ID = GOODS.index("ALLOYS")
                        _print(
                            "The space is full of precious alloy floating around you. It is free money! You just enter the mining tool's activation sequence in your command console and your cargo slowly gets filled with alloy.")
                        _print("You harvested " + str(AMOUNT) + " alloy. Good work!")
                        AddItemToCargo(ALLOY_ID, AMOUNT)
                    else:
                        _print(
                            "The space is full of precious alloy floating around you. It is free money! But your cargo is already full...")
                        _print("You stare at it with a long face and feel sorry for yourself.")
                        _print("")
                        _print("Some time later you kick in the engines and continue your journey.")

                else:
                    _print(
                        "There is a lot of alloy floating around you. However you still didn't equip your ship with a mining tool so you are just sitting there with a long face thinking about the easy money you'll never have.")
    else:
        _print("You barely escape the fight.")
        _print("")

    print("" * 3)
    try:
        ANSWER = input(" Enter").upper()
    except KeyboardInterrupt:
        QuitGame()

    return RETURNCODE


"""
===============================================================
ASTEROID DURING JUMP
===============================================================
"""


def AsteroidDuringJump():
    global GAME

    ClearScreen()
    _print("" * 3)
    _print("The space jump is interrupted by a gravity anomaly and you fall out from hyperspace.")
    _print("")
    _print("You find yourself in the middle of an asteroid field.")
    _print("")
    _print("")

    if GAME.ship_mining_tool:
        if CargoCount() < GAME.ship_max_cargo:
            _print("")
            _print("M - Mine some minerals using the All-purpose Mining Toolkit \u2122")
        else:
            _print("")
            _print("Your cargo bay is full of goods, you can't mine.")

    else:
        _print("")
        _print("It's a pity you don't have a mining toolkit.")
        _print(
            "So you are just sitting sad in your ship looking at the asteroids and thinking about the precious minerals you can not gather.")

    _print("")
    _print("Enter to continue to " + STARSYSTEMS[GAME.current_starystem].systemname)
    _print("")
    _print("")

    try:
        ANSWER = input(" > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    if ANSWER == "M":
        AVAILABLE_CARGO_SPACE = GAME.ship_max_cargo - CargoCount()
        ITEMID = GOODS.index("MINERALS")
        AddItemToCargo(ITEMID, AVAILABLE_CARGO_SPACE)

    return ANSWER


"""
===============================================================
GET CARGO SIZE
===============================================================
"""


def CargoCount():

    amount=0

    for i in range(0, (len(GAME.ship_cargo))):
        cargoitem = GAME.ship_cargo[i]
        amount += cargoitem.amount

    return amount


"""
===============================================================
ADD AN ITEM TO THE CARGO
===============================================================
"""


def AddItemToCargo(pcargoid, pamount):

    global GAME

    GAME.ship_cargo[int(pcargoid)].amount += float(pamount)

    return


"""
===============================================================
REMOVE AN ITEM FROM THE CARGO
===============================================================
"""


def RemoveItemFromCargo(pcargoid, pamount):


    global GAME

    GAME.ship_cargo[int(pcargoid)].amount -= float(pamount)

    return



"""
===============================================================
SHOW CARGO ITEMS
===============================================================
"""

def ShowCargoItems():

    _print('{:<15} {:>6}'.format("ITEM", "AMOUNT"))
    _print(game_config.menuborder * 22)
    _print("")
    for i in range(0, len(GAME.ship_cargo)):
        if GAME.ship_cargo[i].amount:
            _print('{:<15} {:>6}'.format(GOODS[GAME.ship_cargo[i].goodsid], GAME.ship_cargo[i].amount))

    return


"""
===============================================================
SHOW CARGO ITEMS WITH LOCAL PRICE
===============================================================
"""

def ShowCargoItemsWithLocalPrice():

    _print('{:>4} {:<15} {:>6} {:>7}'.format("ID", "ITEM", "AMOUNT", "PRICE"))
    _print(game_config.menuborder * 35)
    _print("")

    local_goods=STARSYSTEMS[GAME.current_starystem].goods
    for i in range(0, len(GAME.ship_cargo)):
        if GAME.ship_cargo[i].amount:
            # @todo: ez tuti hibas, itt a defa arat kell szorozni a modositoval
            LOCALPRICE=round(local_goods[i].goodslocalprice,2)
            _print('{:>4} {:<15} {:>6} {:>7}'.format(i, GOODS[GAME.ship_cargo[i].goodsid], GAME.ship_cargo[i].amount, LOCALPRICE))

    return


def MenuStationHangar():

    global GAME

    _print("\n " * 2)
    _print("Welcome Commander " + GAME.commander_name + ". You are at station " + STARSYSTEMS
    [GAME.current_starystem].systemname + ".")
    if GAME.current_starystem == 0:
        _print("The synthwave version of Blue Danube waltz is playing in the background.")
    else:

        if STARSYSTEMS[GAME.current_starystem].systemname == "EMIL":
            _print("Somehow it feels like home here.")
        else:
            if random.randint(1, 10) >= 8:
               _print(random.choice(ENVTEXT_STATION_PEACEFUL))

    _print("")
    CC=CargoCount()
    if CC == 0:
        STATUSTEXTCARGO = "nothing in the cargo bay."
    elif CC < 50:
        STATUSTEXTCARGO = "some goods in the cargo bay."
    else:
        STATUSTEXTCARGO = "a big pile of goods in the cargo bay."

    _print("You have " + str(round(GAME.commander_credit, 0)) + " credit and " + STATUSTEXTCARGO)
    _print("")
    _print("What's next?")
    _print("")
    _print("C - Show cargo / inventory")
    _print("B - Buy goods")
    _print("S - Sell goods")
    _print("")
    _print("F - Refuel ship")
    _print("R - Repair ship")
    _print("I - Improve ship")
    _print("")
    #_print("$ - Bank")
    #_print("")
    #_print("M - Show starmap")
    #_print("")
    _print("L - Leave station")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    return ANSWER


def MenuShowStats(GAME, game_over):
    if game_over != "game_over":
        ClearScreen()

    _print("\n " * 2)
    _print("Stats of Commander " + GAME.commander_name)
    _print("")
    _print("Rank: " + COMBAT_RATING[GAME.commander_combat_rating])
    _print("Criminal status: " + LEGAL_STATUS[GAME.commander_legal_status])
    _print("Credit: " + str(round(GAME.commander_credit,2)))
    _print("")
    _print("Jump count: " + str(GAME.jump_count))
    _print("Fight count: " + str(GAME.fight_count))
    _print("Kill count: " + str(GAME.kill_count))
    _print("Lightyears traveled: " + str(GAME.lightyears_traveled))
    _print("")
    _print("Ship model: " + SHIP_TYPE[GAME.ship_type])
    _print("Ship hull status: " + str(GAME.ship_hull) + " / " + str(GAME.ship_max_hull))
    _print("Fuel: " + str(round(GAME.ship_fuel, 1)) + " / " + str(GAME.ship_max_fuel))
    if GAME.ship_docking_computer == 1:
        _print("Docking computer status: FUNCTIONAL")
    else:
        _print("Docking comupter: NOT AVAILABLE")

    if GAME.ship_mining_tool == 1:
        _print("Mining tool: PRESENT")
    else:
        _print("Mining tool: NOT AVAILABLE")

    _print("")
    _print("Weapons")
    _print("* beam laser")
    if GAME.ship_missile_count:
        _print("* " + str(GAME.ship_missile_count) + " missile(s)")

    if GAME.ship_flare_count:
        _print("* " + str(GAME.ship_flare_count) + " flare containers")


    if len(GAME.ship_track):
        TRACK=""
        for i in range(0, len(GAME.ship_track)):
            if TRACK == "":
                TRACK=STARSYSTEMS[GAME.ship_track[i]].systemname
            else:
                TRACK = TRACK + " > " + STARSYSTEMS[GAME.ship_track[i]].systemname
        _print("")
        _print("Your journey so far: " + TRACK)

    if game_over != "game_over":
        _print("\n " * 2)
        input(" Enter")

    return


def MenuSpaceNearStation():
    _print("\n" * 2)
    _print("Your ship is floating idle around Station " + STARSYSTEMS[GAME.current_starystem].systemname + ".")

    if STARSYSTEMS[GAME.current_starystem].systemname == "EMIL":
        _print("The star of this system is as bright and yellow as a cat's eye.")
        _print("It is very peaceful here.")
    else:
        if random.randint(0, 5) > 2:
            _print(random.choice(ENVTEXT_SPACE_PEACEFUL))

    _print("\n" * 3)
    _print("D - Dock to the station")
    _print("")
    _print("L - Look around")
    _print("")
    _print("J - Jump to another system")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    return ANSWER


"""
===============================================================
STATION - REPAIR
===============================================================
"""


def MenuStationRepair():
    global GAME

    _print("\n" * 2)
    _print("You are at the Dockyard.")
    _print("")
    if int(GAME.ship_hull) < 100:
        _print("")
        _print("The price to repair 1% hull damage is " + str(DEFAULT_HULL_FIXING_PRICE) + " credit.")
        _print("")
    if int(GAME.ship_hull) > 90:
        HULLRATING = "a good"
    elif int(GAME.ship_hull) > 85:
        HULLRATING = "a fair"
    elif int(GAME.ship_hull) > 50:
        HULLRATING = "a dangerous"
    elif int(GAME.ship_hull) > 25:
        HULLRATING = "an exciting"
    else:
        HULLRATING = "a very brave"

    _print("You have " + str(round(GAME.commander_credit,2)) + " credit and " + HULLRATING + " " + str(
        int(GAME.ship_hull)) + "% hull.")

    _print("")

    _print("")
    _print("R - Return to the Hangar (now for free)")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" How much do you want to spend (or return to the hangar) > ").upper()
    except KeyboardInterrupt:
        QuitGame()

    if ANSWER.isdigit():
        if int(ANSWER) > GAME.commander_credit:
            ANSWER = GAME.commander_credit

    return (ANSWER)


def MenuShowCargo():
    ClearScreen()

    _print("\n" * 2)
    _print("You are standing in the cargo bay.")

    if CargoCount():
        _print("")
        _print("Items in the cargo:")
        _print("")
        ShowCargoItems()

    else:
        _print("")
        _print("Nothing is here, your footsteps echo on the bare walls.")
        _print("")

    _print("")
    _print("")
    _print("Available cargo space: " + str(GAME.ship_max_cargo - CargoCount()))
    _print("Available credit: " + str(round(GAME.commander_credit,2)))
    _print("")
    _print("")
    _print("ENTER to leave")
    _print("")

    try:
        ANSWER = input(" > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    return ANSWER


"""
===============================================================
REFUEL THE SHIP
===============================================================
"""

def MenuStationRefuel():
    _print("\n" * 2)
    _print("You are at the Refueling Hangar.")
    _print("")
    _print("Credit: " + str(round(GAME.commander_credit,2)))
    _print("Fuel price: " + str(STARSYSTEMS[GAME.current_starystem].fuelprice) + " credit per lightyear.")
    _print("")
    _print("")

    if (GAME.ship_max_fuel - GAME.ship_fuel):

        _print("You have " + str(round(GAME.ship_fuel,2)) + " / " + str(GAME.ship_max_fuel) + " fuel and " + str(round(GAME.commander_credit,2)) + " credit.")

        # this much could be bought with the credits available
        BY_CREDIT = int(GAME.commander_credit / STARSYSTEMS[GAME.current_starystem].fuelprice)

        # this much can be bought (this much is missing)
        if (GAME.ship_max_fuel - GAME.ship_fuel) > BY_CREDIT:
            MAX_AMOUNT = BY_CREDIT
        else:
            MAX_AMOUNT = GAME.ship_max_fuel - GAME.ship_fuel

        _print("You can buy " + str(round(MAX_AMOUNT, 0)) + " amount of fuel.")
        PROMPT = "How much do you buy? (max " + str(round(MAX_AMOUNT, 0)) + ")"
        _print("")
    else:
        _print("Your ship is fully tanked, no need to buy more.")
        PROMPT = ""
        _print("")

        _print("")
        _print("")
        _print("R - Return to the hangar")
        _print("")
        ShowFooter()
        
    try:
        ANSWER = input(PROMPT + " > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    return ANSWER


"""
===============================================================
STATION - BUYING GOODS_
===============================================================
"""


def MenuStationBuyGoods():

    _print("\n" * 2)
    _print("You have logged in to the station's online market app.")
    _print("")

    CURRENTSTARSYSTEM=STARSYSTEMS[GAME.current_starystem]
    _print("")
    _print("")
    _print("Credit: " + str(round(GAME.commander_credit,2)))
    _print("Free cargo space: " + str(GAME.ship_max_cargo - CargoCount()))
    _print("")
    _print("")
    _print('{:>6} {:<15} {:>5} {:>6} {:>3}'.format("ITEMID", "NAME", "PRICE", "AMOUNT", "LEGAL"))

    for G in range(0,len(CURRENTSTARSYSTEM.goods)):
        GOODS_ID=CURRENTSTARSYSTEM.goods[G].goodsid
        GOODS_NAME=GOODS[GOODS_ID]
        GOODS_LOCALPRICE=CURRENTSTARSYSTEM.goods[G].goodslocalprice
        GOODS_AMOUNT = random.randint(0,25)
        GOODS_LEGAL = CURRENTSTARSYSTEM.goods[G].goodslegal
        _print('{:>6} {:<15} {:>5} {:>6} {:>3}'.format(GOODS_ID, GOODS_NAME, GOODS_LOCALPRICE, GOODS_AMOUNT, GOODS_LEGAL))

    _print("")
    _print("R - Return to the Hangar (now for free)")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" Enter ITEMID and AMOUNT (i.e. 1 1) or return to the hangar > ").upper()
    except KeyboardInterrupt:
        QuitGame()

    return ANSWER




"""
===============================================================
STATION - SELLING GOODS
===============================================================
"""


def MenuStationSellGoods():

    _print("\n" * 2)
    _print("You have logged in to the station's online market app.")
    _print("")
    _print("You have " + str(round(GAME.commander_credit,2)) + " credit.")
    _print("")

    if CargoCount():

        _print("")
        _print("Items in your cargo:")
        _print("")
        _print("")
        ShowCargoItemsWithLocalPrice()
        _print("")

    else:
        _print("")
        _print("You don't have anything to sell.")
        _print("")


    _print("")
    _print("R - Return to the Hangar (now for free)")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" Enter ITEMID and AMOUNT (i.e. 1 1) or return to the hangar > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    return ANSWER



"""
===============================================================
STATION - IMPROVE
===============================================================
"""


def MenuStationImprove():
    global GAME

    _print("")
    _print("You are at the Dockyard.")
    _print("")
    _print("")
    _print("You have " + str(int(round(GAME.commander_credit, 2))) + " credit.")
    _print("")
    _print("")

    if not int(GAME.ship_docking_computer):
        PRICE = STARSYSTEMS[GAME.current_starystem].dockingcomputerprice
        _print("D - Docking computer. It is a must. Price: " + str(PRICE) + " credit")
        _print("")

    if not int(GAME.ship_mining_tool):
        PRICE = STARSYSTEMS[GAME.current_starystem].miningtoolprice
        _print("T - Equip your ship with a mining tool. The price is just " + str(PRICE) + " credit")
        _print("")

    if GAME.ship_missile_count < GAME.ship_max_missile_count:
        PRICE = STARSYSTEMS[GAME.current_starystem].missileprice
        _print("M - An IR guided missile is the merchant's best friend. Friendship is priceless but it costs. Now " + str(PRICE) + " credit. Each.")
        _print("")

    if GAME.ship_flare_count < GAME.ship_max_flare_count:
        PRICE = STARSYSTEMS[GAME.current_starystem].flareprice
        _print("F - flare (" + str(PRICE) + " credit per container, you have " + str(
            GAME.ship_flare_count) + "/" + str(GAME.ship_max_flare_count) + " container.)")
        _print("")

    # @todo: EMP, advanced missiles, rear laser

    _print("")
    _print("R - Return to the Hangar (now for free)")
    _print("")
    ShowFooter()

    try:
        ANSWER = input(" Spend some money! (Flare: F amount) > ")
        ANSWER = ANSWER.upper()
    except KeyboardInterrupt:
        QuitGame()

    return (ANSWER)


def MainLoop():

    LoadConfig()


    #GAME. = NewOrLoad()

    NewOrLoad()

    if len(STARSYSTEMS) == 0:
        GenerateGalacticMap()

    KEY = ""

    while 1:

        ClearScreen()

        # ------------------------------------------------------------------------ IN THE STATION'S HANGAR
        if GAME.game_position == "STATION-HANGAR":
            KEY = MenuStationHangar()
            if KEY == "L":
                GAME.game_position = "SPACE-NEARSTATION"
            elif KEY == "R":
                GAME.game_position = "STATION-REPAIR"
            elif KEY == "I":
                GAME.game_position = "STATION-IMPROVE"
            elif KEY in ["J"]:
                GAME.game_position = "STARMAP"
            elif KEY == "C":
                MenuShowCargo()
            elif KEY == "F":
                GAME.game_position = "STATION-REFUEL"
            elif KEY == "B":
                GAME.game_position = "STATION-BUYGOODS"
            elif KEY == "S":
                GAME.game_position = "STATION-SELLGOODS"

        # ------------------------------------------------------------------------ STATION - BUYING GOODS
        elif GAME.game_position == "STATION-BUYGOODS":
            KEY = MenuStationBuyGoods()
            if KEY in ["R", "?", ".", "Q", "X", ""]:
                GAME.game_position = "STATION-HANGAR"
            else:
                # split the answer into GOODSID and AMOUNT
                if KEY.find(" ") > 0:
                    ANSWER = KEY.rsplit(' ', 1)
                    GOODSID = ANSWER[0]
                    GOODSAMOUNT = round(float(ANSWER[1]),2)
                    CURRENTSTARSYSTEM = STARSYSTEMS[GAME.current_starystem]
                    GOODSLOCALPRICE = round(CURRENTSTARSYSTEM.goods[int(GOODSID)].goodslocalprice, 2)
                    PRICE = round(GOODSAMOUNT * round(GOODSLOCALPRICE, 2),2)
                    if PRICE > GAME.commander_credit:
                        PRICE=GAME.commander_credit
                        GOODSAMOUNT= round(PRICE / CURRENTSTARSYSTEM.goods[int(GOODSID)].goodslocalprice,2)
                        
                    GAME.commander_credit -= PRICE
                    AddItemToCargo(GOODSID, GOODSAMOUNT)

        # ------------------------------------------------------------------------ STATION - SELLING GOODS
        elif GAME.game_position == "STATION-SELLGOODS":
            KEY = MenuStationSellGoods().strip()
            if KEY in ["R", "?", ".", "Q", "X", ""]:
                GAME.game_position = "STATION-HANGAR"
            else:
                # split the answer into GOODSID and AMOUNT
                if KEY.find(" ") > 0:
                    ANSWER = KEY.rsplit(' ', 1)
                    GOODSID = ANSWER[0]
                    GOODSAMOUNT = round(float(ANSWER[1]),2)
                    CURRENTSTARSYSTEM = STARSYSTEMS[GAME.current_starystem]
                    GOODSLOCALPRICE = round(CURRENTSTARSYSTEM.goods[int(GOODSID)].goodslocalprice, 2)
                    if int(GOODSAMOUNT) > GAME.ship_cargo[int(GOODSID)].amount:
                        GOODSAMOUNT = GAME.ship_cargo[int(GOODSID)].amount
                    PRICE = round(GOODSAMOUNT * round(GOODSLOCALPRICE, 2),2)

                    GAME.commander_credit += PRICE
                    RemoveItemFromCargo(GOODSID, GOODSAMOUNT)


        # ------------------------------------------------------------------------ STATION - IMPROVE SHIP
        elif GAME.game_position == "STATION-IMPROVE":
            KEY = MenuStationImprove().strip()
            if KEY in ["R", ""]:
                GAME.game_position = "STATION-HANGAR"
            elif KEY in ["D"]:
                PRICE=STARSYSTEMS[GAME.current_starystem].dockingcomputerprice
                if GAME.commander_credit >= PRICE:
                    if not GAME.ship_docking_computer:
                        GAME.ship_docking_computer = 1
                        GAME.commander_credit -= PRICE
            elif KEY in ["M"]:
                PRICE=STARSYSTEMS[GAME.current_starystem].missileprice
                if GAME.commander_credit >= PRICE:
                    if GAME.ship_missile_count < GAME.ship_max_missile_count:
                        GAME.ship_missile_count += 1
                        GAME.commander_credit -= PRICE
            elif KEY in ["T"]:
                PRICE=STARSYSTEMS[GAME.current_starystem].miningtoolprice
                if GAME.commander_credit >= PRICE:
                    if not GAME.ship_mining_tool:
                        GAME.ship_mining_tool = 1
                        GAME.commander_credit -= PRICE
            elif KEY in ["F"]:
                if GAME.ship_flare_count < GAME.ship_max_flare_count:
                    PRICE=STARSYSTEMS[GAME.current_starystem].flareprice
                    GAME.commander_credit-=PRICE
                    GAME.ship_flare_count+=1

        # ------------------------------------------------------------------------ STATION - REFUEL
        elif GAME.game_position == "STATION-REFUEL":
            KEY = MenuStationRefuel()
            if KEY in ["R", ""]:
                GAME.game_position = "STATION-HANGAR"
            elif KEY.isdigit():

                KEY = float(KEY)
                if int(KEY) < 0:
                    KEY=0

                if round(KEY,2) > (GAME.ship_max_fuel - GAME.ship_fuel):
                    KEY = GAME.ship_max_fuel - GAME.ship_fuel

                GAME.commander_credit = GAME.commander_credit - (int(KEY) * STARSYSTEMS[GAME.current_starystem].fuelprice)
                GAME.ship_fuel += int(KEY)
                GAME.game_position = "STATION-HANGAR"

        # ------------------------------------------------------------------------ SPACE - NEAR THE STATION
        elif GAME.game_position == "SPACE-NEARSTATION":
            KEY = MenuSpaceNearStation()
            if KEY == "D":
                DAMAGE = CalculateDocking()
                GAME.ship_hull = GAME.ship_hull - DAMAGE
                GAME.game_position = "STATION-HANGAR"
            elif KEY in ["J"]:
                GAME.game_position = "STARMAP"

        # ------------------------------------------------------------------------ STATION - REPAIR
        elif GAME.game_position == "STATION-REPAIR":
            KEY = MenuStationRepair()
            if KEY in ["R", ""]:
                GAME.game_position = "STATION-HANGAR"
            elif KEY.isdigit():
                GAME.commander_credit -= int(int(KEY) * DEFAULT_HULL_FIXING_PRICE)
                GAME.ship_hull+=int(KEY)
                GAME.game_position = "STATION-HANGAR"

        # ------------------------------------------------------------------------ STARMAP
        elif GAME.game_position == "STARMAP":
            KEY = ShowStarMap()
            if KEY in ["R", ""]:
                GAME.game_position = "SPACE-NEARSTATION"
            elif KEY.isdigit():
                # @todo: not calculated correctly, leaving and immediate docking also counts which is a bug
                GAME.jump_count += 1
                GAME.ship_track.append(int(KEY))

                GAME.game_position = "SPACE-NEARSTATION"

                # calculate the distance and modify stats
                CURRENTX = STARSYSTEMS[GAME.current_starystem].posx
                CURRENTY = STARSYSTEMS[GAME.current_starystem].posy
                STARSYSTEMX = STARSYSTEMS[int(KEY)].posx
                STARSYSTEMY = STARSYSTEMS[int(KEY)].posy
                D = round(math.sqrt((CURRENTX - STARSYSTEMX) * (CURRENTX - STARSYSTEMX) + (CURRENTY - STARSYSTEMY) * (
                        CURRENTY - STARSYSTEMY)), 1)
                GAME.current_starystem = int(KEY)
                GAME.ship_fuel -= D
                GAME.lightyears_traveled += D

                # does anything happen during the jump?
                # pirates, asteroid field, police, corrupt police, space fight in the distance
                SpaceEvent=GenerateSpaceEvent()
                if SpaceEvent == 0: # pirates
                    if SpaceFight() == "SPACEFIGHT-GAMEOVER":
                        GameOver()
                    else:
                        GAME.game_position = "SPACE-NEARSTATION"
                elif SpaceEvent == 1: # asteroid field
                    AsteroidDuringJump()
                    GAME.game_position = "SPACE-NEARSTATION"
                elif SpaceEvent == 2: # neutral/lawful police
                    PoliceInvestigation()
                elif SpaceEvent == 3: # corrupt police
                    CorruptPoliceInvestigation()
                elif SpaceEvent == 4: # space fight in the distance
                    SpaceFightInTheDistance()

        # ------------------------------------------------------------------------ DIMENSIONAL EXCEPTION
        #else:
        #    _print("You have jumped to an unknown dimension.")
        #    _print("Strange stars, strange colors.")
        #    _print("Is this Final Space?")
        #    _print("")
        #    _print("The memory of the Great Old Ones is very strong here and you faint while starting to lose your sanity.")
        #    _print("")
        #    _print("")
        #    _print("")
        #    input("ENTER")
#
#            GAME.game_position = "STATION-HANGAR"

        # ------------------------------------------------------------------------ OTHER STUFF
        if GAME.ship_hull <= 0:
            GAME.ship_hull = 0
            CrashedDuringDocking()
            GameOver()

        # FOOTER OPTIONS
        if KEY == "?":
            MenuShowStats(GAME, 0)

        if KEY == ".":
            SaveGame()

        if KEY == "Q":
            QuitGame()

        if KEY == "X":
            SaveAndExit()




"""
===============================================================
RUN!!!
===============================================================
"""


MainLoop()


