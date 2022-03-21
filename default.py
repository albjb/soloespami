# Esto permite su ejecución en modo emulado
try:
	pluginhandle = int( sys.argv[ 1 ] )
except:
	pluginhandle = ""

# Traza el inicio del canal
xbmc.output("[cinegratis.py] init")

DEBUG = True

# Entry point
def run():
	plugintools.log("albjb.run")

	# Get params
	params = plugintools.get_params()

	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"
  		plugintools.close_item_list()
	
# Main menu 
def main_list(params):
	plugintools.log("albjb.main_list "+repr(params))
	
	# ftp://alb:666@albjb18.zapto.org:21/volume1/PELIS/NEW/
	plugintools.add_item( action="play", title="Disney", fanart="fanart.jpg", thumbnail="fanart.jpg", url="http://www.google.es", plot=plot, folder=True )
	
	plugintools.add_item( action="main_list", title="NEW", fanart="fanart.jpg", thumbnail="fanart.jpg", url="http://www.youtube.com", isPlayable=True, folder=True )
	plugintools.set_view(plugintools.THUMBNAIL)  

addfolder ("hola","aaa","mainlist")

