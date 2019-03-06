# -*- coding: utf-8 -*-
"""
Módulo tools com funcoes auxiliares para o fplayer
"""

from flask import url_for
import glob

from mutagen import File
from model import model

MUSICFOLDER = 'static/musics/'

def updatemusic():
	db = model()
	musiclist = glog.glob(MUSIFOLDER + "*.mp3")
	musicnames = [mi.split("/")[-1] for mi in musiclist]

	indb = [msi.arquivo for msi in db().iterselect(db.musica.arquivo)
			if msi.arquivo in musicnames]

	notindb = list(set(musicnames) - set(indb))

	for msi in notindb:
		tag = File(MUSICFOLDER + msi)
		tempo = sec2minString(File(MUSICFOLDER + msi).info.length))

		if('TIT2' in tag.keys()):
			db.musica.insert(nome=tag['TIT2'].text[0],
							 cantor=tag['TPE1'].text[0],
							 arquivo=msi,
							 tempo=tempo
							 )

		else:
			db.musica.insert(arquivo=msi,
							 tempo=tempo
							 )

	notindir = [msi.arquivo
				for msi in db().iterselect(db.musica.arquivo)
				if msi.arquivo not in musicnames
				]

	for msi in notindir:
		db(db.musica.arquivo == msi).delete()

	db.commit()


def get_musics():
	db = model()
	musiclist = db().select(db.musica.arquivo,
							db.musica.tempo,
							db.musica.cantor,
							db.musica.nome,
							orderby=db.musica.arquivo|db.musica.nome)

	if len(musiclist) > 0:
		musicJ = [{"fileName": mi.arquivo,
				   "coverURL": url_for('coverImage',
				   music=MUSICFOLDER + mi.arquivo),
				   'fileUrl': url_for('sounds',
				   					  music=MUSICFOLDER + mi.arquivo),
				   					  'length': mi.tempo,
				   					  'Tags': None
				   					  }
				   					  for mi in musiclist
				   					  ]

				   for i in range(len(musicJ)):
				       if musiclist[i].cantor is not None:
				       		musicJ[i]['Tags'] = {
				       				'TIT2': musiclist[i].nome,
				       				'TPE1': musiclist[i].cantor
				       						}
	else:
		musicJ = []
	return musicJ

@app.route("/")
def home():
	updatemusic()
	musicJ = get_musica()

	return render_template("home.html",
							musicJ=musicJ)
