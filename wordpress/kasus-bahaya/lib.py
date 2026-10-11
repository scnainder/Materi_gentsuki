W, H = 800, 520
ROAD = '#4b5563'; GRASS = '#cfe3c3'; WALK = '#d9dde3'; LINE = '#ffffff'; YEL = '#fbbf24'
RED = '#dc2626'; ME = '#f97316'; BLUE = '#2563eb'; NIGHT = '#0f172a'


class S:
    def __init__(self, bg=GRASS):
        self.o = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{bg}"/>']
        self.top = []

    def add(self, s): self.o.append(s)
    def over(self, s): self.top.append(s)

    def svg(self):
        defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#16a34a"/></marker>'
                '<marker id="ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#dc2626"/></marker>'
                '<marker id="ag" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#f8fafc"/></marker></defs>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Inter,Segoe UI,Arial,sans-serif">'
                + defs + ''.join(self.o) + ''.join(self.top) + '</svg>')

    # ---------- roads ----------
    def vroad(self, x0=300, x1=500, y0=0, y1=H, center='dash', walk=True):
        if walk:
            self.add(f'<rect x="{x0-28}" y="{y0}" width="28" height="{y1-y0}" fill="{WALK}"/><rect x="{x1}" y="{y0}" width="28" height="{y1-y0}" fill="{WALK}"/>')
        self.add(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{ROAD}"/>')
        self.add(f'<line x1="{x0+6}" y1="{y0}" x2="{x0+6}" y2="{y1}" stroke="{LINE}" stroke-width="2"/><line x1="{x1-6}" y1="{y0}" x2="{x1-6}" y2="{y1}" stroke="{LINE}" stroke-width="2"/>')
        cx = (x0 + x1) / 2
        if center == 'dash':
            self.add(f'<line x1="{cx}" y1="{y0}" x2="{cx}" y2="{y1}" stroke="{LINE}" stroke-width="4" stroke-dasharray="26 22"/>')
        elif center == 'solid':
            self.add(f'<line x1="{cx}" y1="{y0}" x2="{cx}" y2="{y1}" stroke="{LINE}" stroke-width="4"/>')
        elif center == 'yellow':
            self.add(f'<line x1="{cx}" y1="{y0}" x2="{cx}" y2="{y1}" stroke="{YEL}" stroke-width="5"/>')

    def hroad(self, y0=180, y1=340, x0=0, x1=W, center='dash', walk=True):
        if walk:
            self.add(f'<rect x="{x0}" y="{y0-28}" width="{x1-x0}" height="28" fill="{WALK}"/><rect x="{x0}" y="{y1}" width="{x1-x0}" height="28" fill="{WALK}"/>')
        self.add(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{ROAD}"/>')
        cy = (y0 + y1) / 2
        if center == 'dash':
            self.add(f'<line x1="{x0}" y1="{cy}" x2="{x1}" y2="{cy}" stroke="{LINE}" stroke-width="4" stroke-dasharray="26 22"/>')
        elif center == 'solid':
            self.add(f'<line x1="{x0}" y1="{cy}" x2="{x1}" y2="{cy}" stroke="{LINE}" stroke-width="4"/>')

    def cross(self, vx0=300, vx1=500, hy0=180, hy1=340, vcenter='dash', hcenter='dash', priority=None):
        """intersection; priority='v' keeps vertical center line through"""
        self.hroad(hy0, hy1, center=hcenter)
        self.vroad(vx0, vx1, center=vcenter)
        # clear the box
        self.add(f'<rect x="{vx0}" y="{hy0}" width="{vx1-vx0}" height="{hy1-hy0}" fill="{ROAD}"/>')
        if priority == 'v':
            cx = (vx0 + vx1) / 2
            self.add(f'<line x1="{cx}" y1="{hy0}" x2="{cx}" y2="{hy1}" stroke="{LINE}" stroke-width="4" stroke-dasharray="26 22"/>')
        # sidewalk corners
        for (x, y, w, h) in [(vx0-28, hy0-28, 28, 28), (vx1, hy0-28, 28, 28), (vx0-28, hy1, 28, 28), (vx1, hy1, 28, 28)]:
            self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{WALK}"/>')

    def zebra_h(self, x0, x1, y, h=34):  # crossing across a vertical road (stripes vertical)
        n = int((x1 - x0) / 18)
        for i in range(n):
            self.add(f'<rect x="{x0+4+i*18}" y="{y}" width="10" height="{h}" fill="#f8fafc"/>')

    def zebra_v(self, y0, y1, x, w=34):  # crossing across a horizontal road
        n = int((y1 - y0) / 18)
        for i in range(n):
            self.add(f'<rect x="{x}" y="{y0+4+i*18}" width="{w}" height="10" fill="#f8fafc"/>')

    def stopline(self, x0, x1, y):
        self.add(f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="6" fill="#f8fafc"/>')

    def building(self, x, y, w, h, fill='#94a3b8'):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#64748b" stroke-width="2" rx="4"/>')

    def tree(self, x, y, r=16):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4d7c0f"/><circle cx="{x-4}" cy="{y-4}" r="{r*0.55}" fill="#65a30d"/>')

    def blind(self, pts):
        p = ' '.join(f'{x},{y}' for x, y in pts)
        self.add(f'<polygon points="{p}" fill="#111827" fill-opacity="0.28"/>')

    # ---------- actors (drawn facing up, then rotated) ----------
    def _g(self, x, y, ang, inner, top=False):
        s = f'<g transform="translate({x},{y}) rotate({ang})">{inner}</g>'
        (self.over if top else self.add)(s)

    def car(self, x, y, ang=0, color=BLUE, sig=None, brake=False):
        sigs = ''
        if sig in ('L', 'B'): sigs += '<circle cx="-15" cy="-28" r="5" fill="#fde047" stroke="#ca8a04"/><circle cx="-15" cy="28" r="5" fill="#fde047" stroke="#ca8a04"/>'
        if sig in ('R', 'B'): sigs += '<circle cx="15" cy="-28" r="5" fill="#fde047" stroke="#ca8a04"/><circle cx="15" cy="28" r="5" fill="#fde047" stroke="#ca8a04"/>'
        if brake: sigs += '<rect x="-15" y="28" width="9" height="4" fill="#ef4444"/><rect x="6" y="28" width="9" height="4" fill="#ef4444"/>'
        self._g(x, y, ang, f'<rect x="-18" y="-32" width="36" height="64" rx="9" fill="{color}" stroke="#0f172a" stroke-width="2"/>'
                f'<rect x="-13" y="-20" width="26" height="13" rx="3" fill="#cbd5e1"/><rect x="-13" y="12" width="26" height="9" rx="3" fill="#cbd5e1"/>{sigs}')

    def truck(self, x, y, ang=0, color='#64748b', length=120, sig=None, hazard=False, lights=False):
        L = length
        extra = ''
        if sig in ('L', 'B') or hazard: extra += f'<circle cx="-22" cy="{-L/2+6}" r="5" fill="#fde047" stroke="#ca8a04"/><circle cx="-22" cy="{L/2-4}" r="5" fill="#fde047" stroke="#ca8a04"/>'
        if sig in ('R', 'B') or hazard: extra += f'<circle cx="22" cy="{-L/2+6}" r="5" fill="#fde047" stroke="#ca8a04"/><circle cx="22" cy="{L/2-4}" r="5" fill="#fde047" stroke="#ca8a04"/>'
        if lights: extra += f'<path d="M-14,{-L/2} L-60,{-L/2-110} L60,{-L/2-110} L14,{-L/2} z" fill="#fef08a" fill-opacity="0.45"/>'
        self._g(x, y, ang, f'{extra}<rect x="-22" y="{-L/2}" width="44" height="30" rx="6" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>'
                f'<rect x="-16" y="{-L/2+5}" width="32" height="10" rx="2" fill="#94a3b8"/>'
                f'<rect x="-24" y="{-L/2+34}" width="48" height="{L-34}" rx="3" fill="{color}" stroke="#0f172a" stroke-width="2"/>')

    def bus(self, x, y, ang=0, color='#10b981', label='', length=130, sig=None, hazard=False):
        L = length
        extra = ''
        if sig in ('L', 'B') or hazard: extra += f'<circle cx="-22" cy="{-L/2+6}" r="5" fill="#fde047" stroke="#ca8a04"/><circle cx="-22" cy="{L/2-6}" r="5" fill="#fde047" stroke="#ca8a04"/>'
        if sig in ('R', 'B') or hazard: extra += f'<circle cx="22" cy="{-L/2+6}" r="5" fill="#fde047" stroke="#ca8a04"/><circle cx="22" cy="{L/2-6}" r="5" fill="#fde047" stroke="#ca8a04"/>'
        win = ''.join(f'<rect x="-18" y="{-L/2+22+i*20}" width="36" height="12" rx="2" fill="#e0f2fe" fill-opacity="0.7"/>' for i in range(int((L-40)/20)))
        lab = f'<text x="0" y="4" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a" transform="rotate(90)">{label}</text>' if label else ''
        self._g(x, y, ang, f'{extra}<rect x="-23" y="{-L/2}" width="46" height="{L}" rx="9" fill="{color}" stroke="#0f172a" stroke-width="2"/>{win}{lab}')

    def moto(self, x, y, ang=0, color='#7c3aed', me=False, sig=None):
        c = ME if me else color
        extra = ''
        if sig == 'R': extra = '<circle cx="9" cy="-15" r="4" fill="#fde047" stroke="#ca8a04"/>'
        if sig == 'L': extra = '<circle cx="-9" cy="-15" r="4" fill="#fde047" stroke="#ca8a04"/>'
        inner = (f'{extra}<rect x="-7" y="-22" width="14" height="44" rx="7" fill="{c}" stroke="#0f172a" stroke-width="2"/>'
                 f'<rect x="-13" y="-14" width="26" height="4" rx="2" fill="#0f172a"/><circle cx="0" cy="2" r="9" fill="{"#fde68a" if me else "#e5e7eb"}" stroke="#0f172a" stroke-width="2"/>')
        self._g(x, y, ang, inner, top=me)
        if me:
            self.over(f'<g><rect x="{x-27}" y="{y+28}" width="54" height="22" rx="11" fill="{ME}" stroke="#7c2d12" stroke-width="1.5"/><text x="{x}" y="{y+44}" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">ANDA</text></g>')

    def bike(self, x, y, ang=0, color='#0891b2'):
        self._g(x, y, ang, f'<rect x="-3" y="-20" width="6" height="40" rx="3" fill="#0f172a"/><rect x="-11" y="-13" width="22" height="3" fill="#0f172a"/><circle cx="0" cy="0" r="8" fill="{color}" stroke="#0f172a" stroke-width="2"/>')

    def ped(self, x, y, color='#e11d48', child=False, umbrella=False, cane=False):
        r = 10 if child else 14
        s = ''
        if umbrella: s += f'<circle cx="{x}" cy="{y}" r="{r+11}" fill="#6366f1" fill-opacity="0.75" stroke="#312e81" stroke-width="2"/>'
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#0f172a" stroke-width="2"/><circle cx="{x}" cy="{y}" r="{r*0.45}" fill="#fcd9b6"/>'
        self.over(s)

    def signal(self, x, y, state='G', ang=0):
        cols = {'R': ['#ef4444', '#374151', '#374151'], 'Y': ['#374151', '#facc15', '#374151'], 'G': ['#374151', '#374151', '#22c55e'], 'YF': ['#374151', '#facc15', '#374151']}[state]
        inner = f'<rect x="-30" y="-11" width="60" height="22" rx="6" fill="#111827"/>' + ''.join(f'<circle cx="{-18+i*18}" cy="0" r="7" fill="{c}"/>' for i, c in enumerate(reversed(cols)))
        self._g(x, y, ang, inner, top=True)
        if state == 'YF':
            self.over(f'<text x="{x}" y="{y-16}" text-anchor="middle" font-size="12" font-weight="800" fill="#111827" stroke="#fff" stroke-width="3" paint-order="stroke">kedip</text>')

    def mirror(self, x, y):
        self.over(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+26}" stroke="#334155" stroke-width="3"/><circle cx="{x}" cy="{y}" r="11" fill="#fb923c" stroke="#7c2d12" stroke-width="3"/><circle cx="{x}" cy="{y}" r="6" fill="#e0f2fe"/>')

    def cone(self, x, y):
        self.over(f'<polygon points="{x},{y-12} {x-9},{y+9} {x+9},{y+9}" fill="#f97316" stroke="#7c2d12" stroke-width="1.5"/><rect x="{x-6}" y="{y-2}" width="12" height="3" fill="#fff"/>')

    # ---------- arrows / annotations ----------
    def path(self, d, kind='go', width=6):
        if kind == 'go':
            self.over(f'<path d="{d}" fill="none" stroke="#16a34a" stroke-width="{width}" stroke-linecap="round" marker-end="url(#ah)" stroke-opacity="0.9"/>')
        elif kind == 'danger':
            self.over(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="{width-1}" stroke-dasharray="12 9" stroke-linecap="round" marker-end="url(#ar)"/>')
        elif kind == 'ghost':
            self.over(f'<path d="{d}" fill="none" stroke="#f8fafc" stroke-width="{width-2}" stroke-dasharray="8 8" marker-end="url(#ag)" stroke-opacity="0.85"/>')

    def bang(self, x, y, n):
        self.over(f'<g><circle cx="{x}" cy="{y}" r="15" fill="{RED}" stroke="#fff" stroke-width="3"/><text x="{x}" y="{y+6}" text-anchor="middle" font-size="17" font-weight="900" fill="#fff">{n}</text></g>')

    def label(self, x, y, text, anchor='start', color='#111827', bg='#ffffff', size=15):
        lines = text.split('\n')
        w = max(sum(1.75 if ord(ch) > 0x2E80 else 1 for ch in l) for l in lines) * size * 0.56 + 16
        h = len(lines) * (size + 4) + 10
        bx = x if anchor == 'start' else (x - w if anchor == 'end' else x - w / 2)
        t = ''.join(f'<text x="{bx+8}" y="{y+size+3+i*(size+4)}" font-size="{size}" font-weight="700" fill="{color}">{l}</text>' for i, l in enumerate(lines))
        self.over(f'<g><rect x="{bx}" y="{y}" width="{w}" height="{h}" rx="7" fill="{bg}" fill-opacity="0.94" stroke="#334155" stroke-width="1.2"/>{t}</g>')

    def title(self, text):
        self.over(f'<g><rect x="12" y="12" width="{len(text)*8.6+24}" height="32" rx="8" fill="#0f172a" fill-opacity="0.85"/><text x="24" y="34" font-size="16" font-weight="800" fill="#fff">{text}</text></g>')

    def rain(self):
        import random
        random.seed(3)
        s = ''.join(f'<line x1="{x}" y1="{y}" x2="{x-6}" y2="{y+18}" stroke="#e0f2fe" stroke-width="2" stroke-opacity="0.7"/>' for x, y in [(random.randint(0, W), random.randint(0, H)) for _ in range(140)])
        self.over(s)

    def puddle(self, x, y, rx=34, ry=14):
        self.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#60a5fa" fill-opacity="0.55" stroke="#93c5fd"/>')

    def beam(self, x, y, ang=0, length=170, spread=60):
        self.add(f'<g transform="translate({x},{y}) rotate({ang})"><path d="M-6,-20 L{-spread},{-20-length} L{spread},{-20-length} L6,-20 z" fill="#fef08a" fill-opacity="0.38"/></g>')

    def dark(self, opacity=0.55):
        self.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{NIGHT}" fill-opacity="{opacity}"/>')

    def tracks(self, y, x0=0, x1=W):
        self.add(f'<rect x="{x0}" y="{y-26}" width="{x1-x0}" height="52" fill="#a8a29e"/>')
        for xx in range(x0, x1, 22):
            self.add(f'<rect x="{xx}" y="{y-24}" width="9" height="48" fill="#78350f"/>')
        self.add(f'<rect x="{x0}" y="{y-14}" width="{x1-x0}" height="5" fill="#334155"/><rect x="{x0}" y="{y+9}" width="{x1-x0}" height="5" fill="#334155"/>')

    def gate(self, x, y, length=90, ang=0):
        self.over(f'<g transform="translate({x},{y}) rotate({ang})"><rect x="0" y="-4" width="{length}" height="8" fill="#fff" stroke="#0f172a"/>' + ''.join(f'<rect x="{i*18}" y="-4" width="9" height="8" fill="#111827"/>' for i in range(int(length/18))) + '<circle cx="0" cy="0" r="8" fill="#ef4444" stroke="#0f172a" stroke-width="2"/></g>')

    def sign(self, x, y, kind):
        if kind == 'school':
            self.over(f'<g transform="translate({x},{y})"><line x1="0" y1="18" x2="0" y2="46" stroke="#334155" stroke-width="3"/><rect x="-16" y="-16" width="32" height="32" transform="rotate(45)" fill="#facc15" stroke="#111" stroke-width="2"/><circle cx="-5" cy="-4" r="4" fill="#111"/><circle cx="6" cy="-2" r="3" fill="#111"/><rect x="-8" y="1" width="6" height="11" fill="#111"/><rect x="4" y="2" width="5" height="9" fill="#111"/></g>')
        if kind == 'work':
            self.over(f'<g transform="translate({x},{y})"><rect x="-16" y="-16" width="32" height="32" transform="rotate(45)" fill="#facc15" stroke="#111" stroke-width="2"/><text x="0" y="6" text-anchor="middle" font-size="15" font-weight="900">!</text></g>')
