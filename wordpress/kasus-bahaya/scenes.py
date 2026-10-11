from lib import S, W, H

# Vertical road x300-500 (our lane 300-400, center 350; oncoming 400-500, center 450)
# Horizontal road y180-340 (eastbound top lane ~220, westbound bottom lane ~300)


def s1():  # bus sekolah berhenti di kiri
    s = S(); s.vroad(); s.add('<rect x="244" y="0" width="28" height="520" fill="#d9dde3"/>')
    s.bus(332, 200, 0, color='#facc15', label='BUS TK', sig=None, hazard=True)
    s.ped(282, 120, '#e11d48', child=True); s.ped(285, 152, '#2563eb', child=True); s.ped(282, 250, '#16a34a', child=True)
    s.car(450, 70, 180, '#0ea5e9')
    s.car(350, 500, 0, '#64748b')
    s.moto(350, 400, 0, me=True)
    s.path('M350,375 C352,330 392,300 392,250 L392,120', 'go')
    s.path('M300,128 C330,128 360,128 395,128', 'danger'); s.bang(318, 100, 1)
    s.bang(450, 120, 2); s.bang(395, 490, 3)
    s.label(512, 160, 'Anak bisa lari keluar\ndari depan bus', 'start')
    s.label(512, 40, 'Mobil dari depan', 'start')
    s.label(512, 440, 'Kendaraan di belakang', 'start')
    s.title('Kasus 1 · 30 km/h · bus TK berhenti')
    return s.svg()


def s2():  # lurus di samping truk
    s = S(); s.cross()
    s.truck(372, 380, 0, '#64748b', sig='L')
    s.moto(320, 440, 0, me=True)
    s.car(452, 150, 180, '#0ea5e9', sig='R')
    s.blind([(400, 260), (460, 175), (500, 200), (500, 340), (400, 340)])
    s.path('M322,415 L322,120', 'go')
    s.path('M372,318 C372,270 340,215 260,205', 'danger'); s.bang(300, 250, 1)
    s.path('M452,185 C452,250 420,300 250,300', 'danger'); s.bang(420, 290, 2)
    s.label(520, 360, 'Truk sein kiri:\nbisa menyeret (巻き込み)', 'start')
    s.label(520, 90, 'Mobil lawan belok kanan,\ntertutup truk', 'start')
    s.title('Kasus 2 · lurus di sebelah truk')
    return s.svg()


def s3():  # menunggu belok kanan, bus dari depan
    s = S(); s.cross(); s.signal(560, 360, 'G')
    s.moto(392, 300, 0, me=True, sig='R')
    s.car(450, 120, 180, '#0ea5e9', sig='R')
    s.bus(458, 30, 180, '#10b981', length=120)
    s.path('M398,280 C400,240 430,225 520,222 L700,222', 'go')
    s.path('M484,60 C490,130 486,200 486,330', 'danger'); s.bang(484, 160, 1)
    s.path('M440,90 C425,160 470,200 470,330', 'danger'); s.bang(425, 50, 2)
    s.label(520, 280, 'Motor bisa melaju lurus\ndari balik bus', 'start')
    s.label(520, 80, 'Bus bisa menghindari\nmobil & tetap maju', 'start')
    s.title('Kasus 3 · menunggu belok kanan')
    return s.svg()


def s4():  # persimpangan sempit pandangan buruk
    s = S(); s.hroad(200, 290, center=None); s.vroad(330, 470, center=None)
    s.add('<rect x="330" y="200" width="140" height="90" fill="#4b5563"/>')
    for b in [(0, 0, 302, 172), (498, 0, 302, 172), (0, 318, 302, 202), (498, 318, 302, 202)]:
        s.building(*b, fill='#a3a3a3')
    s.mirror(510, 300); s.mirror(290, 300)
    s.ped(445, 245, '#e11d48')
    s.moto(375, 430, 0, me=True)
    s.path('M375,405 L375,120', 'go')
    s.path('M120,245 L320,245', 'danger'); s.bang(170, 215, 1)
    s.path('M700,245 L480,245', 'danger'); s.bang(640, 215, 2)
    s.label(20, 330, 'Orang/mobil bisa\nkeluar dari gang kiri', 'start')
    s.label(780, 330, 'Gang kanan juga\ntidak terlihat', 'end')
    s.label(490, 120, 'Pejalan kaki hampir\nselesai menyeberang', 'start')
    s.title('Kasus 4 · persimpangan sempit')
    return s.svg()


def s5():  # malam, belok kiri
    s = S('#334155'); s.cross(); s.zebra_v(180, 340, 250); s.stopline(300, 400, 370)
    s.beam(340, 400, -35, 210, 70)
    s.dark(0.55)
    s.ped(270, 160, '#facc15')
    s.bike(140, 300, 90)
    s.ped(200, 360, '#f472b6')
    s.moto(345, 410, 0, me=True, sig='L')
    s.path('M345,385 C345,330 335,300 300,300', 'go')
    s.path('M270,170 L270,290', 'danger'); s.bang(240, 150, 1)
    s.path('M140,300 L230,300', 'danger'); s.bang(140, 270, 2)
    s.bang(200, 390, 3)
    s.label(20, 60, 'Pejalan kaki mulai\nmenyeberang', 'start')
    s.label(20, 420, 'Di luar sorot lampu\nsulit terlihat', 'start')
    s.label(520, 400, 'Malam · 10 km/h\nbelok kiri', 'start', bg='#fef3c7')
    s.title('Kasus 5 · malam, belok kiri')
    return s.svg()


def s6():  # truk parkir di jalur lawan, bus datang
    s = S(); s.vroad()
    s.truck(462, 250, 180, '#64748b', hazard=True)
    s.bus(452, 85, 180, '#10b981', length=110)
    s.ped(512, 330, '#e11d48')
    s.moto(350, 430, 0, me=True)
    s.path('M350,405 L350,160', 'go')
    s.path('M440,140 C420,190 385,210 385,320', 'danger'); s.bang(385, 200, 1)
    s.path('M505,330 L410,330', 'danger'); s.bang(530, 360, 2)
    
    s.label(520, 40, 'Bus bisa keluar\ngaris tengah', 'start')
    s.label(560, 380, 'Orang bisa keluar\ndari balik truk', 'start')
    s.title('Kasus 6 · truk parkir, bus mendekat')
    return s.svg()


def s7():  # hujan, pejalan kaki payung
    s = S('#94a3b8'); s.vroad(320, 500, walk=False)
    s.puddle(345, 280); s.puddle(380, 150, 26, 10)
    s.ped(338, 220, '#e11d48', umbrella=True); s.ped(345, 120, '#2563eb', umbrella=True)
    s.ped(305, 175, '#16a34a', child=True)
    s.moto(395, 430, 0, me=True)
    s.path('M395,405 L410,90', 'go')
    s.path('M308,175 C340,175 370,170 400,170', 'danger'); s.bang(300, 145, 1)
    s.bang(345, 280, 2)
    s.rain()
    s.label(520, 120, 'Anak bisa melompat\nke jalan', 'start')
    s.label(520, 240, 'Pejalan kaki berpayung\ntidak sadar Anda datang', 'start')
    s.label(520, 360, 'Genangan: jangan\ncipratkan air', 'start')
    s.title('Kasus 7 · hujan, pejalan kaki')
    return s.svg()


def s8():  # 優先道路
    s = S(); s.cross(priority='v')
    s.car(240, 220, 90, '#a855f7', brake=True)
    s.car(450, 120, 180, '#0ea5e9', sig='R')
    s.moto(350, 440, 0, me=True)
    s.path('M350,415 L350,100', 'go')
    s.path('M450,155 C450,240 420,300 250,300', 'danger'); s.bang(470, 250, 1)
    s.path('M272,220 L380,220', 'danger'); s.bang(240, 180, 2)
    s.label(520, 60, 'Mobil lawan belok kanan', 'start')
    s.label(20, 90, 'Mobil kiri bisa masuk\nwalau Anda di 優先道路', 'start')
    s.label(520, 400, 'Anda di 優先道路\n(garis tengah menerus)', 'start', bg='#dbeafe')
    s.title('Kasus 8 · melintas di 優先道路')
    return s.svg()


def s9():  # belok kiri di belakang truk
    s = S(); s.cross(); s.zebra_v(180, 340, 250); s.signal(560, 150, 'G')
    s.truck(350, 300, -20, '#64748b', sig='L')
    s.moto(355, 450, 0, me=True, sig='L')
    s.ped(265, 150, '#e11d48')
    s.bike(312, 470, 0)
    s.blind([(318, 380), (300, 520), (330, 520)])
    s.path('M355,425 C355,370 340,320 300,300 L200,300', 'ghost')
    s.path('M265,160 L265,280', 'danger'); s.bang(235, 140, 1)
    s.path('M312,445 L312,330', 'danger'); s.bang(282, 430, 2)
    s.label(20, 60, 'Truk bisa berhenti\nsebelum zebra', 'start')
    s.label(20, 470, 'Sepeda di titik buta\n& dari belakang kiri', 'start')
    s.label(520, 420, 'Ikuti di belakang truk,\njangan menyelip kiri', 'start', bg='#dcfce7')
    s.title('Kasus 9 · belok kiri di belakang truk')
    return s.svg()


def s10():  # kuning kedip
    s = S(); s.cross(); s.signal(560, 360, 'YF')
    s.truck(455, 110, 180, '#64748b', sig='R')
    s.moto(220, 220, 90, '#7c3aed')
    s.moto(350, 430, 0, me=True)
    s.path('M350,405 L350,100', 'go')
    s.path('M245,220 L420,220', 'danger'); s.bang(200, 190, 1)
    s.path('M488,90 C480,200 430,290 260,300', 'danger'); s.bang(490, 240, 2)
    s.label(20, 90, 'Motor dari kiri\nbelum tentu berhenti', 'start')
    s.label(560, 100, 'Mobil belok kanan\ndari balik truk', 'start')
    s.title('Kasus 10 · lampu kuning berkedip')
    return s.svg()


def s11():  # tikungan gunung
    s = S('#bbd7a8')
    s.add('<path d="M350,560 C350,330 380,230 640,160" fill="none" stroke="#d9dde3" stroke-width="248"/>')
    s.add('<path d="M350,560 C350,330 380,230 640,160" fill="none" stroke="#4b5563" stroke-width="200"/>')
    s.add('<path d="M350,560 C350,330 380,230 640,160 L900,100" fill="none" stroke="#4b5563" stroke-width="200"/>')
    s.add('<path d="M350,560 C350,330 380,230 640,160 L900,100" fill="none" stroke="#fbbf24" stroke-width="5"/>')
    s.add('<path d="M246,560 C246,300 300,140 610,58 L900,0" fill="none" stroke="#e5e7eb" stroke-width="8" stroke-dasharray="4 10"/>')
    for x, y in [(120, 300), (160, 140), (80, 460), (700, 400), (620, 470), (760, 300)]:
        s.tree(x, y, 22)
    s.moto(300, 440, 0, me=True)
    s.car(620, 235, 252, '#0ea5e9')
    s.path('M300,415 C300,300 330,200 480,135', 'go')
    s.path('M585,232 C530,215 490,200 450,185', 'danger'); s.bang(560, 300, 1)
    s.bang(275, 250, 2)
    s.label(500, 330, 'Mobil lawan bisa\nmelewati garis tengah', 'start')
    s.label(40, 60, 'Kalau terlalu cepat:\nterlempar ke pagar pembatas', 'start')
    s.title('Kasus 11 · tikungan di gunung')
    return s.svg()


def s12():  # 踏切 di belakang bus
    s = S(); s.vroad(); s.tracks(250, 0, W)
    s.gate(300, 300, 90, 0); s.gate(500, 200, 90, 180)
    s.bus(350, 140, 0, '#10b981', length=130)
    s.car(350, 20, 0, '#64748b', brake=True)
    s.truck(455, 80, 180, '#64748b')
    s.ped(525, 120, '#e11d48')
    s.moto(350, 400, 0, me=True)
    s.add('<rect x="300" y="222" width="10" height="56" fill="#dc2626" fill-opacity="0.6"/>')
    s.bang(300, 330, 1); s.bang(265, 250, 2); s.bang(420, 30, 3)
    s.label(520, 280, 'Ada ruang di seberang?\nKalau macet, jangan masuk', 'start')
    s.label(20, 300, 'Terlalu kiri:\nroda bisa terperosok', 'start')
    s.label(520, 30, 'Truk lawan & pejalan kaki', 'start')
    s.title('Kasus 12 · perlintasan kereta')
    return s.svg()


def s13():  # truk antar barang
    s = S(); s.vroad(); s.add('<rect x="250" y="0" width="22" height="520" fill="#a8a29e"/>')
    s.add('<rect x="250" y="170" width="22" height="40" fill="#d9dde3"/>')
    s.truck(455, 200, 180, '#64748b', hazard=True)
    s.ped(470, 100, '#2563eb')
    s.moto(350, 430, 0, me=True)
    s.path('M350,405 L350,90', 'go')
    s.path('M262,190 C320,190 360,190 420,190', 'danger'); s.bang(230, 190, 1)
    s.path('M470,112 L410,112', 'danger'); s.bang(500, 70, 2)
    s.label(20, 260, 'Orang bisa keluar dari\ncelah pagar ambil barang', 'start')
    s.label(520, 280, 'Sopir sibuk antar barang,\ntidak melihat Anda', 'start')
    s.title('Kasus 13 · truk sedang antar barang')
    return s.svg()


def s14():  # belok kanan, truk passing
    s = S(); s.cross(); s.zebra_v(180, 340, 516)
    s.truck(450, 100, 180, '#64748b', lights=True)
    s.moto(488, 40, 180, '#7c3aed')
    s.ped(532, 300, '#e11d48'); s.ped(532, 230, '#16a34a', child=True)
    s.moto(392, 300, 0, me=True, sig='R')
    s.path('M398,280 C405,240 430,225 520,222 L700,222', 'ghost')
    s.path('M488,65 L488,320', 'danger'); s.bang(520, 150, 1)
    s.bang(570, 265, 2)
    s.label(560, 120, 'Motor dari balik truk\nlurus terus', 'start')
    s.label(600, 360, 'Pejalan kaki\nmenyeberang', 'start')
    s.label(20, 60, 'Truk mengedipkan lampu\n(passing) ≠ pasti aman', 'start', bg='#fef3c7')
    s.title('Kasus 14 · belok kanan, truk beri jalan')
    return s.svg()


def s15():  # proyek di jalur kiri
    s = S(); s.vroad()
    s.add('<rect x="305" y="140" width="90" height="90" fill="#fde68a" stroke="#b45309" stroke-width="3" stroke-dasharray="10 6"/>')
    for x, y in [(315, 245), (350, 245), (385, 245), (315, 130), (385, 130)]:
        s.cone(x, y)
    s.sign(270, 320, 'work')
    s.car(450, 80, 180, '#0ea5e9')
    s.moto(350, 430, 0, me=True)
    s.stopline(305, 395, 290)
    s.path('M350,405 L350,305', 'go')
    s.path('M450,115 L450,330', 'danger'); s.bang(480, 200, 1)
    s.label(520, 60, 'Mobil lawan datang', 'start')
    s.label(520, 300, 'Berhenti dulu,\nbiarkan mobil lawan lewat', 'start', bg='#dcfce7')
    s.label(20, 160, 'Proyek menutup\njalur kiri', 'start')
    s.title('Kasus 15 · proyek di jalur Anda')
    return s.svg()


def s16():  # anak sekolah di trotoar
    s = S(); s.vroad()
    s.sign(255, 330, 'school')
    s.ped(286, 160, '#e11d48', child=True); s.ped(286, 200, '#2563eb', child=True); s.ped(286, 240, '#16a34a', child=True)
    s.car(450, 90, 180, '#0ea5e9')
    s.car(350, 500, 0, '#64748b')
    s.moto(350, 400, 0, me=True)
    s.path('M350,375 L350,120', 'go')
    s.path('M292,200 C320,200 340,200 370,200', 'danger'); s.bang(310, 130, 1)
    s.path('M365,330 C420,280 430,200 420,150', 'danger'); s.bang(440, 260, 2)
    s.bang(395, 480, 3)
    s.label(520, 160, 'Anak bisa lari ke jalan', 'start')
    s.label(520, 260, 'Keluar garis tengah =\ntabrakan dengan mobil lawan', 'start')
    s.label(520, 420, 'Mobil belakang: rem\nbertahap', 'start')
    s.title('Kasus 16 · anak sekolah di trotoar')
    return s.svg()


ALL = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]

if __name__ == '__main__':
    import os
    os.makedirs('svg', exist_ok=True)
    for i, f in enumerate(ALL, 1):
        open(f'svg/k{i:02d}.svg', 'w').write(f())
    # preview sheet html
    html = '<html><body style="margin:0;background:#fff">' + ''.join(f'<div style="display:inline-block;margin:4px">{f()}</div>' for f in ALL) + '</body></html>'
    open('preview.html', 'w').write(html)
    print('ok')
