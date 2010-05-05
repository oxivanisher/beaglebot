#!/usr/bin/python

import xmpp
import os
from jabberbot import JabberBot, botcmd
from ConfigParser import RawConfigParser

class SystemBot(JabberBot):
    @botcmd
    def who(self, mess, args):
        """Who is currently logged in?"""
        who_pipe = os.popen('/usr/bin/who', 'r')
        who = who_pipe.read().strip()
        who_pipe.close()

        return 'Currently online users:\n' + who

    @botcmd
    def reboot(self, mess, args):
	"""Reboot Beagle"""
	reboot_pipe = os.popen('reboot','r')
	reboot = reboot_pipe.read().strip()
	reboot_pipe.close()

	return 'Rebooting Beagle...\n' + reboot

    @botcmd
    def poweroff(self, mess, args):
	"""Power off beagle"""
	poweroff_pipe = os.popen('/sbin/poweroff','r')
	poweroff = poweroff_pipe.read().strip()
	poweroff_pipe.close()

	return 'Powering beagle down...' + poweroff

    @botcmd
    def cmd(self, mess, args):
	"""Run cmd as root"""
	cmd_pipe = os.popen(args,'r')
	cmd = cmd_pipe.read().strip()
	cmd_pipe.close()

	uptime_pipe = os.popen('uptime','r')
	uptime = uptime_pipe.read().strip()
	uptime_pipe.close()

	return uptime + ':\n' + cmd

    @botcmd
    def myip(self, mess, args):
	"""Show IP of Beagle"""
	ip_pipe = os.popen ('ifconfig | grep "inet addr" | grep -v 127.0.0.1 | awk \'{print $2}\' | sed s/addr://g','r')
	ip = 'my ip: ' + ip_pipe.read().strip()
	ip_pipe.close()

	return ip

    @botcmd
    def play(self, mess, args):
	"""Music play"""
	play_pipe = os.popen('mpc play','r')
	play = play_pipe.read().strip()
	play_pipe.close()

	return 'Starting to play\n'

    @botcmd
    def stop(self, mess, args):
	"""Music stop"""
	stop_pipe = os.popen('mpc stop','r')
	stop = stop_pipe.read().strip()
	stop_pipe.close()

	return 'Stopping music\n'


    @botcmd
    def lspls(self, mess, args):
	"""Lists all playlists"""
	lspls_pipe = os.popen('ls /var/lib/mpd/playlists/ | sed s/.m3u//g','r')
	lspls = lspls_pipe.read().strip()
	lspls_pipe.close()

	return 'Available playlists:\n' + lspls

    @botcmd
    def ldpls(self, mess, args):
	"""Load playlist"""
	loadpls_pipe = os.popen('mpc clear && mpc load ' + args + ' && mpc play','r')
	loadpls_pipe.close()

	return 'MPC loading playlist: ' + args

    @botcmd
    def sleep(self, mess, args):
	"""Music sleep timer"""
	mpcsleep_pipe = os.popen('screen -dmS mpc_sleep scripts/mpc_sleep.sh','r')
	mpcsleep_pipe.close()

	return 'mpc sleepmode ENABLED.\nSleep well!'

    @botcmd
    def wturak(self, mess, args):
	"""Wake turak"""
	mpcsleep_pipe = os.popen('etherwake 00:22:15:85:25:09','r')
	mpcsleep_pipe.close()

	return 'Waking turak'

    @botcmd
    def wradio(self, mess, args):
	"""Wake radiobox"""
	mpcsleep_pipe = os.popen('etherwake 00:1f:c6:b5:f0:a1','r')
	mpcsleep_pipe.close()

	return 'Waking radiobox'

    @botcmd
    def wakeup(self, mess, args):
	"""Wakeup at given time"""
	wakeup_pipe = os.popen('at -f scripts/wakeup.sh ' + args, 'r')
	wakeup = wakeup_pipe.read().strip()
	wakeup_pipe.close()

	return 'MPC will wake you at: ' + args + '\n' + wakeup

    @botcmd
    def at(self, mess, args):
	"""Notify on given time"""
	at_pipe = os.popen('scripts/at.sh ' + args, 'r')
	at = at_pipe.read().strip()
	at_pipe.close()
	return 'Timer set!\n' + at

    def idle_proc(self):
        status = []

	mpc_pipe = os.popen('mpc | head -n 1','r')
	mpc = mpc_pipe.read().strip()
	status.append(mpc)

        status = '\n'.join(status)
        # TODO: set "show" based on load? e.g. > 1 means "away"
        if self.status_message != status:
            self.status_message = status
        return

config = RawConfigParser()
config.read(['/etc/beaglebot.cfg','beaglebot.cfg'])

bot = SystemBot(config.get('systembot','username'),
                config.get('systembot','password'))
bot.serve_forever()
