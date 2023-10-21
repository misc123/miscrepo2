# -*- coding: utf-8 -*-

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)

import urllib, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, xbmcvfs

from common import *

params = get_params()
mode = None

addon_id     = xbmcaddon.Addon().getAddonInfo('id') 

#===============================================================================

selfAddon = xbmcaddon.Addon(id=addon_id)

try:
    datapath= xbmcvfs.translatePath(selfAddon.getAddonInfo('profile'))
except:
    datapath= xbmc.translatePath(selfAddon.getAddonInfo('profile'))

plugin_handle = int(sys.argv[1])
dialog = xbmcgui.Dialog()
mysettings = xbmcaddon.Addon(id = 'plugin.video.favourites')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')

mediapath = ''

#===============================================================================

BASE  = "plugin://plugin.video.youtube/"

#======================================================================================================================


#xbmcplugin.endOfDirectory(plugin_handle)
