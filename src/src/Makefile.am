bin_SCRIPTS = system-config-firewall-tui
if ! USE_USERMODE
bin_SCRIPTS += system-config-firewall
endif
sbin_SCRIPTS = lokkit

scfwdir = $(pkgdatadir)
scfw_PYTHON = *.py convert-config
if USE_USERMODE
scfw_PYTHON += system-config-firewall
endif

scfwindir = $(pkgdatadir)
scfwin_in_files = *.py.in
scfwin_PYTHON = $(scfwin_in_files:.in=)

gladedir = $(pkgdatadir)
glade_PYTHON = *.glade

icondir = $(datadir)/icons/hicolor
iconFILES = icons/*/apps/*

EXTRA_DIST = $(bin_SCRIPTS) $(sbin_SCRIPTS) $(iconFILES)

CLEANFILES = *~ *\# .\#* *.py?

install-data-local:
if USE_USERMODE
	ln -sf consolehelper $(DESTDIR)/$(bindir)/system-config-firewall
endif
	install -d $(DESTDIR)/$(icondir)
	cp -fpR icons/* $(DESTDIR)/$(icondir)
