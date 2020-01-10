SUBDIRS = src po config

EXTRA_DIST = \
	COPYING \
	system-config-firewall.spec 

CLEANFILES = *~ *\# .\#* *.tar*

DISTCLEANFILES = config.log intltool-*

DISTCLEANDIRS = autom4te.cache system-config-firewall-*

all: report

tag:
	@spec_ver=`awk '/Version:/ { print $$2}' system-config-firewall.spec`; \
	if test "$$spec_ver" != "${PACKAGE_VERSION}"; then \
		echo "Spec file and package versions differ: $$spec_ver != ${PACKAGE_VERSION}"; \
		secs=10; \
		echo -n "Using ./autogen.sh in $$secs seconds: "; \
		for i in `seq $$secs -1 1`; do echo -n "."; sleep 1; done; echo; \
		./autogen.sh; \
		echo; \
		echo "Please run make again to apply version changes."; \
		exit 1; \
	fi
	@if ! git diff --quiet --exit-code; then \
		clear; \
		echo -n "========================================"; \
		echo "========================================"; \
		PAGER= git diff; \
		echo -n "========================================"; \
		echo "========================================"; \
		echo "Do you want to commit these changes? (y/N)"; \
		read answer; \
		[ "$$answer" == "Y" -o "$$answer" == "y" ] || exit 1; \
		perl -pi -e "s/^VERSION = .*/VERSION = '${PACKAGE_VERSION}'/" src/fw_config.py; \
		git commit -a -m "$(PACKAGE_TAG)"; \
	fi
	git tag -f $(PACKAGE_TAG)
	git push --all
	git push --tags

archive: update-po $(desktop_DATA) tag
	git archive --format=tar --prefix="${PACKAGE_NAME}-$(PACKAGE_VERSION)/" "$(PACKAGE_TAG)" | bzip2 >${PACKAGE_NAME}-$(PACKAGE_VERSION).tar.bz2
	scp "${PACKAGE_NAME}-$(PACKAGE_VERSION).tar.bz2" fedorahosted.org:system-config-firewall
	@echo "The archive is in ${PACKAGE_NAME}-$(PACKAGE_VERSION).tar.bz2"
	@echo "Also have a look at https://fedorahosted.org/released/system-config-firewall/"

local: distclean
	@rm -rf ${PACKAGE_NAME}-$(PACKAGE_VERSION).tar.bz2
	@rm -rf /tmp/${PACKAGE_NAME}-$(PACKAGE_VERSION) /tmp/${PACKAGE_NAME}
	@dir=$$PWD; cd /tmp; cp -a $$dir ${PACKAGE_NAME}
	@mv /tmp/${PACKAGE_NAME} /tmp/${PACKAGE_NAME}-$(PACKAGE_VERSION)
	@dir=$$PWD; cd /tmp; tar --bzip2 -cSpf $$dir/${PACKAGE_NAME}-$(PACKAGE_VERSION).tar.bz2 ${PACKAGE_NAME}-$(PACKAGE_VERSION)
	@rm -rf /tmp/${PACKAGE_NAME}-$(PACKAGE_VERSION)	
	@echo "The archive is in ${PACKAGE_NAME}-$(PACKAGE_VERSION).tar.bz2"

test-rpm: dist
	@rpmbuild -ta $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.bz2

test-srpm: dist
	@rpmbuild -ts $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.bz2

update-po:
	ls $(top_srcdir)/po/*.po | sed 's/.*\/po\///;s/.po//' > $(top_srcdir)/po/LINGUAS
	make -C po update-po ${PACKAGE_NAME}.pot

report:
	@for cat in `cat ${top_srcdir}/po/LINGUAS`; do \
		echo -n "$$cat: "; \
		$(MSGFMT) --statistics -o /dev/null $(top_srcdir)/po/$$cat.po; \
	done

distclean-local:
	-test -z "$(DISTCLEANDIRS)" || rm -rf $(DISTCLEANDIRS)
