# -*- coding: utf-8 -*-

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)

import urllib, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, xbmcvfs

from common import *
from favourites import *

params = get_params()
mode = None

plugin_handle = int(sys.argv[1])
dialog = xbmcgui.Dialog()
mysettings = xbmcaddon.Addon(id = 'plugin.video.favourites')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')

#===============================================================================
def Main():


    Add_Dir(
        name="【Mostly ENGLISH】琅琊榜 Nirvana In Fire", url="plugin://plugin.video.youtube/playlist/PLzfNoYeTnhXK8DEE7VrcB4E8TTgJcdhfB/", folder=True,
        icon="https://upload.wikimedia.org/wikipedia/en/9/9b/Nirvana_In_Fire_%28Lang_Ya_Bang%29_official_poster.jpg?20200531015616")
        
    Add_Dir(
        name="【ENG SUB】琅琊榜 Nirvana In Fire", url="plugin://plugin.video.youtube/playlist/PLtt_YYUGi1gXRt2XVJZrHDBkZECcfmuAJ/", folder=True,
        icon="https://upload.wikimedia.org/wikipedia/en/9/9b/Nirvana_In_Fire_%28Lang_Ya_Bang%29_official_poster.jpg?20200531015616")
        
    Add_Dir(
        name="【ENG SUB】琅琊榜之风起长林 Nirvana in Fire Ⅱ", url="plugin://plugin.video.youtube/playlist/PLvpAVnYN4lb0rKGJD0bKRIvBQ9erpx8WZ/", folder=True,     
        icon="https://upload.wikimedia.org/wikipedia/en/b/bc/Nirvana_in_Fire_2_drama_poster.jpg")
 
 
    Add_Dir(
        name="御赐小仵作", url="plugin://plugin.video.youtube/channel/UC3PKcYXUAhao3p4kuNS4_9w/playlist/PL9yRf-Ghij3YIJj8j2Y8rEVMWBqGuLD9A/", folder=True)

 
if mode == 0 or mode is None:
    Main()
        
xbmcplugin.endOfDirectory(plugin_handle)
