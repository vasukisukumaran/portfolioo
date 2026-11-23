"""The small, accessible line icons and project overlays used throughout the site."""

ICONS = {
    "arrow": '<path d="M4 12h15m-6-6 6 6-6 6"/>',
    "north-east": '<path d="M5 19 19 5M7 5h12v12"/>',
    "down": '<path d="M12 3v17m-6-6 6 6 6-6"/>',
    "back": '<path d="M20 12H4m6-6-6 6 6 6"/>',
    "up": '<path d="M12 21V4m-6 6 6-6 6 6"/>',
    "expand": '<path d="M14 4h6v6M4 14v6h6M20 4l-7 7M4 20l7-7"/>',
    "close": '<path d="m5 5 14 14M19 5 5 19"/>',
    "code": '<path d="m8 6-6 6 6 6m8-12 6 6-6 6M14.5 3l-5 18"/>',
    "layers": '<path d="m2 8 10-5 10 5-10 5L2 8Zm0 4 10 5 10-5M2 16l10 5 10-5"/>',
    "grid": '<rect x="3" y="3" width="18" height="18" rx=".7"/><path d="M3 10h18M10 3v18m5-11v11"/>',
    "network": '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="5" r="2.5"/><circle cx="12" cy="13" r="2.5"/><circle cx="5" cy="20" r="2"/><circle cx="19" cy="20" r="2"/><path d="m8 8 2.5 3m3-1L16 7m-5 8-4 4m7-4 3.5 3.5"/>',
    "database": '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v12c0 4.2 16 4.2 16 0v-12M4 11.5c0 4 16 4 16 0"/>',
    "braces": '<path d="M8.5 3H7C3 3 6.5 10 2.5 12c4 2 1 9 4.5 9h1.5M15.5 3H17c4 0 .5 7 4.5 9-4 2-1 9-4.5 9h-1.5"/>',
    "tools": '<path d="m3 4 4 1 3 4-2 2-4-3-1-4Zm6 6 11 10m-12-6-5 5a1.6 1.6 0 0 0 2.2 2.2l5-5m3-6c-.8-2 .1-5.3 2-6.6 1.2-.7 2.5-.9 3.6-.6l-3.1 3.1 2.8 2.8 3.1-3.1c.7 3.6-2.4 6.4-5.4 5.9"/>',
    "people": '<circle cx="9" cy="7" r="3"/><path d="M2 20v-2c0-6 14-6 14 0v2Zm14-16a3 3 0 0 1 0 6m2 4c2.2.5 4 2.3 4 4.5V20h-3"/>',
    "mail": '<rect x="2.5" y="5" width="19" height="14" rx="1.5"/><path d="m3 6 9 7 9-7"/>',
    "phone": '<path d="m7.8 3 2.4 4-2.6 2.7a15.5 15.5 0 0 0 6.9 6.8l2.6-2.6 4 2.3c-.5 3-2.2 4.7-4.4 4.3A19.2 19.2 0 0 1 3.5 7.1C3.2 5 4.9 3.4 7.8 3Z"/>',
    "pin": '<path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 0 1 14 0Z"/><circle cx="12" cy="10" r="2.3"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7.4 10v7m0-10v.2m4.1 9.8v-7m.2 3.4c0-4 5.4-4.2 5.4-.3V17"/>',
    "github": '<path d="M9 20c-4.2 1.1-4.2-2-6-2.5M15.5 22v-3.6c0-1-.4-1.8-1-2.1 3.4-.4 6.4-1.7 6.4-7a5.4 5.4 0 0 0-1.5-3.8 5 5 0 0 0-.1-3.6s-1.2-.4-3.9 1.4a13.6 13.6 0 0 0-7.2 0C5.4 1.5 4.2 2 4.2 2a5 5 0 0 0-.1 3.6A5.4 5.4 0 0 0 2.7 9c0 5.3 3 6.7 6.4 7.1-.6.4-1.1 1.3-1.1 2.4V22"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="14" rx="1"/><path d="M8 7V4h8v3m-13 5a25 25 0 0 0 18 0m-10 1h2"/>',
}


def icon(name, extra=""):
    return f'<svg class="icon {extra}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


def photo_overlay(plate):
    """Graphic studies over the landscape images. These are not product screens."""
    if plate == "farm":
        diagram = '''
          <g transform="translate(565 242)" stroke-linejoin="round">
            <g fill="#2c2b30" fill-opacity=".77" stroke="#f3c7be" stroke-width="1.45">
              <path d="m0 48 80-38 81 35-80 40Z"/><path d="m0 31 80-38 81 35-80 40Z"/>
              <path d="m0 14 80-38 81 35-80 40Z"/><path d="m0-3 80-38 81 35-80 40Z"/>
            </g>
            <g fill="none" stroke="#f58f7c" stroke-width="1.15">
              <ellipse cx="81" cy="-1" rx="35" ry="14"/><ellipse cx="81" cy="-1" rx="25" ry="9"/>
              <path d="M81-1v-65l27-15h26"/>
            </g>
            <circle cx="81" cy="-1" r="3" fill="#f58f7c"/>
          </g>'''
    elif plate == "city":
        diagram = '''
          <g fill="none" stroke="#ffad9b" stroke-width="2.8" stroke-linejoin="round">
            <path d="M190 325h80l56-61h77l77-78h84l52-52h115"/>
            <path d="M326 264v-67l61-61h78" opacity=".71"/>
            <path d="M564 186v75l41 41h96" opacity=".71"/>
          </g>
          <g fill="#f9aa9c" stroke="#29262b" stroke-width="2">
            <circle cx="190" cy="325" r="5"/><circle cx="326" cy="264" r="6"/>
            <circle cx="465" cy="136" r="5"/><circle cx="564" cy="186" r="6"/>
            <circle cx="731" cy="134" r="5"/><circle cx="701" cy="302" r="5"/>
          </g>'''
    else:
        diagram = '''
          <g transform="matrix(1,-.08,0,1,499,193)">
            <rect x="0" y="0" width="218" height="121" fill="#29282d" fill-opacity=".7" stroke="#efc7c4" stroke-opacity=".73"/>
            <g fill="none" stroke="#f0d4d0" stroke-width="1.5">
              <path d="M14 13h190M14 108h190M19 13v33m26-33v33m26-33v33m26-33v33m26-33v33m26-33v33m26-33v33m26-33v33"/>
              <path d="M19 108V75m26 33V75m26 33V75m26 33V75m26 33V75m26 33V75m26 33V75m26 33V75"/>
              <path d="M17 60h185" stroke-dasharray="7 7" opacity=".6"/>
            </g>
            <g fill="#f58f7c" opacity=".88"><rect x="47" y="14" width="22" height="30"/><rect x="125" y="77" width="22" height="30"/></g>
          </g>'''
    return f'<svg class="photo-diagram" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">{diagram}</svg>'
