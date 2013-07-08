
call	svn	export --force	"https://google-reader-simulator.googlecode.com/svn/trunk/ReaderGAE/Source"	".\release"

appcfg.py --email=xxxk.l.xxx@gmail.com update ".\\release\\"

pause
