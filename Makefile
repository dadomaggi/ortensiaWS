
#insert the install path
INSTALLPATH = /home/pi/ortensia_ws
SRCPATH     = /home/pi/workspace/WS

# ambiente da 
PYTHON = /usr/local/lib/python2.7/site-packages:/home/pi/ortensia_ws/lib/python
export PYTHONPATH=$(PYTHON)

# set directory for datapath
WSDATAPATH = $(SRCPATH)/data
WWWDATAPATH = /var/www/html

install:
	@cd $(SRCPATH) && python setup.py install --home=$(INSTALLPATH)
	@cp -r $(SRCPATH)/data $(INSTALLPATH)/data
	@cp -r $(SRCPATH)/www/* $(WWWDATAPATH)/.
	@echo "export SRCPATH=$(SRCPATH) \n\
	export WWWDATAPATH=$(WWWDATAPATH) \n\
	export WSDATAPATH=$(WSDATAPATH) \n\
	export PYTHONPATH=$(PYTHON) \n\
	" >$(INSTALLPATH)/ws.env
	@echo "\nORTENSIA WS succesfully installed\n\
	source $(INSTALLPATH)/ws.env to load the environment.\n"
	
