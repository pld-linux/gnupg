#!/bin/sh

if [ -r "${HOME}/.gnupg/gpg.conf" ]; then
    CFG="${HOME}/.gnupg/gpg.conf"
else
    CFG="${HOME}/.gnupg/options"
fi

X11=no
if [ -r "${HOME}/.gnupg/gpg-agent.conf" ]; then
    grep -qE "^pinentry-program.*pinentry-(qt|gtk)" "${HOME}/.gnupg/gpg-agent.conf" && X11=yes
fi

if grep -q "^use-agent" ${CFG} 2>/dev/null; then
    if [ -f "${HOME}/.gnupg/GPG_AGENT_INFO" ] && kill -0 "$(cut -d: -f2 $HOME/.gnupg/GPG_AGENT_INFO)" 2>/dev/null; then
	export GPG_AGENT_INFO="$(cat ${HOME}/.gnupg/GPG_AGENT_INFO)"
    else
	if [ -n "$DISPLAY" -a "$X11" = "yes" ] || [ -z "$DISPLAY" -a "$X11" = "no" ]; then
	    eval "$(gpg-agent --daemon)"
	    echo $GPG_AGENT_INFO > ~/.gnupg/GPG_AGENT_INFO
	    export GPG_AGENT_INFO
	fi
    fi
fi
