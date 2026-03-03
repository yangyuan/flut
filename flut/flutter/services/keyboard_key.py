from typing import Optional, override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_required_field

_planeMask = 0x0FF00000000

_keyLabels = {
    0x00000000020: "Space",
    0x00000000021: "Exclamation",
    0x00000000022: "Quote",
    0x00000000023: "Number Sign",
    0x00000000024: "Dollar",
    0x00000000025: "Percent",
    0x00000000026: "Ampersand",
    0x00000000027: "Quote Single",
    0x00000000028: "Parenthesis Left",
    0x00000000029: "Parenthesis Right",
    0x0000000002A: "Asterisk",
    0x0000000002B: "Add",
    0x0000000002C: "Comma",
    0x0000000002D: "Minus",
    0x0000000002E: "Period",
    0x0000000002F: "Slash",
    0x00000000030: "Digit 0",
    0x00000000031: "Digit 1",
    0x00000000032: "Digit 2",
    0x00000000033: "Digit 3",
    0x00000000034: "Digit 4",
    0x00000000035: "Digit 5",
    0x00000000036: "Digit 6",
    0x00000000037: "Digit 7",
    0x00000000038: "Digit 8",
    0x00000000039: "Digit 9",
    0x0000000003A: "Colon",
    0x0000000003B: "Semicolon",
    0x0000000003C: "Less",
    0x0000000003D: "Equal",
    0x0000000003E: "Greater",
    0x0000000003F: "Question",
    0x00000000040: "At",
    0x0000000005B: "Bracket Left",
    0x0000000005C: "Backslash",
    0x0000000005D: "Bracket Right",
    0x0000000005E: "Caret",
    0x0000000005F: "Underscore",
    0x00000000060: "Backquote",
    0x00000000061: "Key A",
    0x00000000062: "Key B",
    0x00000000063: "Key C",
    0x00000000064: "Key D",
    0x00000000065: "Key E",
    0x00000000066: "Key F",
    0x00000000067: "Key G",
    0x00000000068: "Key H",
    0x00000000069: "Key I",
    0x0000000006A: "Key J",
    0x0000000006B: "Key K",
    0x0000000006C: "Key L",
    0x0000000006D: "Key M",
    0x0000000006E: "Key N",
    0x0000000006F: "Key O",
    0x00000000070: "Key P",
    0x00000000071: "Key Q",
    0x00000000072: "Key R",
    0x00000000073: "Key S",
    0x00000000074: "Key T",
    0x00000000075: "Key U",
    0x00000000076: "Key V",
    0x00000000077: "Key W",
    0x00000000078: "Key X",
    0x00000000079: "Key Y",
    0x0000000007A: "Key Z",
    0x0000000007B: "Brace Left",
    0x0000000007C: "Bar",
    0x0000000007D: "Brace Right",
    0x0000000007E: "Tilde",
    0x00100000001: "Unidentified",
    0x00100000008: "Backspace",
    0x00100000009: "Tab",
    0x0010000000D: "Enter",
    0x0010000001B: "Escape",
    0x0010000007F: "Delete",
    0x00100000101: "Accel",
    0x00100000103: "Alt Graph",
    0x00100000104: "Caps Lock",
    0x00100000106: "Fn",
    0x00100000107: "Fn Lock",
    0x00100000108: "Hyper",
    0x0010000010A: "Num Lock",
    0x0010000010C: "Scroll Lock",
    0x0010000010E: "Super",
    0x0010000010F: "Symbol",
    0x00100000110: "Symbol Lock",
    0x00100000111: "Shift Level 5",
    0x00100000301: "Arrow Down",
    0x00100000302: "Arrow Left",
    0x00100000303: "Arrow Right",
    0x00100000304: "Arrow Up",
    0x00100000305: "End",
    0x00100000306: "Home",
    0x00100000307: "Page Down",
    0x00100000308: "Page Up",
    0x00100000401: "Clear",
    0x00100000402: "Copy",
    0x00100000403: "Cr Sel",
    0x00100000404: "Cut",
    0x00100000405: "Erase Eof",
    0x00100000406: "Ex Sel",
    0x00100000407: "Insert",
    0x00100000408: "Paste",
    0x00100000409: "Redo",
    0x0010000040A: "Undo",
    0x00100000501: "Accept",
    0x00100000502: "Again",
    0x00100000503: "Attn",
    0x00100000504: "Cancel",
    0x00100000505: "Context Menu",
    0x00100000506: "Execute",
    0x00100000507: "Find",
    0x00100000508: "Help",
    0x00100000509: "Pause",
    0x0010000050A: "Play",
    0x0010000050B: "Props",
    0x0010000050C: "Select",
    0x0010000050D: "Zoom In",
    0x0010000050E: "Zoom Out",
    0x00100000601: "Brightness Down",
    0x00100000602: "Brightness Up",
    0x00100000603: "Camera",
    0x00100000604: "Eject",
    0x00100000605: "Log Off",
    0x00100000606: "Power",
    0x00100000607: "Power Off",
    0x00100000608: "Print Screen",
    0x00100000609: "Hibernate",
    0x0010000060A: "Standby",
    0x0010000060B: "Wake Up",
    0x00100000701: "All Candidates",
    0x00100000702: "Alphanumeric",
    0x00100000703: "Code Input",
    0x00100000704: "Compose",
    0x00100000705: "Convert",
    0x00100000706: "Final Mode",
    0x00100000707: "Group First",
    0x00100000708: "Group Last",
    0x00100000709: "Group Next",
    0x0010000070A: "Group Previous",
    0x0010000070B: "Mode Change",
    0x0010000070C: "Next Candidate",
    0x0010000070D: "Non Convert",
    0x0010000070E: "Previous Candidate",
    0x0010000070F: "Process",
    0x00100000710: "Single Candidate",
    0x00100000711: "Hangul Mode",
    0x00100000712: "Hanja Mode",
    0x00100000713: "Junja Mode",
    0x00100000714: "Eisu",
    0x00100000715: "Hankaku",
    0x00100000716: "Hiragana",
    0x00100000717: "Hiragana Katakana",
    0x00100000718: "Kana Mode",
    0x00100000719: "Kanji Mode",
    0x0010000071A: "Katakana",
    0x0010000071B: "Romaji",
    0x0010000071C: "Zenkaku",
    0x0010000071D: "Zenkaku Hankaku",
    0x00100000801: "F1",
    0x00100000802: "F2",
    0x00100000803: "F3",
    0x00100000804: "F4",
    0x00100000805: "F5",
    0x00100000806: "F6",
    0x00100000807: "F7",
    0x00100000808: "F8",
    0x00100000809: "F9",
    0x0010000080A: "F10",
    0x0010000080B: "F11",
    0x0010000080C: "F12",
    0x0010000080D: "F13",
    0x0010000080E: "F14",
    0x0010000080F: "F15",
    0x00100000810: "F16",
    0x00100000811: "F17",
    0x00100000812: "F18",
    0x00100000813: "F19",
    0x00100000814: "F20",
    0x00100000815: "F21",
    0x00100000816: "F22",
    0x00100000817: "F23",
    0x00100000818: "F24",
    0x00100000901: "Soft 1",
    0x00100000902: "Soft 2",
    0x00100000903: "Soft 3",
    0x00100000904: "Soft 4",
    0x00100000905: "Soft 5",
    0x00100000906: "Soft 6",
    0x00100000907: "Soft 7",
    0x00100000908: "Soft 8",
    0x00100000A01: "Close",
    0x00100000A02: "Mail Forward",
    0x00100000A03: "Mail Reply",
    0x00100000A04: "Mail Send",
    0x00100000A05: "Media Play Pause",
    0x00100000A07: "Media Stop",
    0x00100000A08: "Media Track Next",
    0x00100000A09: "Media Track Previous",
    0x00100000A0A: "New",
    0x00100000A0B: "Open",
    0x00100000A0C: "Print",
    0x00100000A0D: "Save",
    0x00100000A0E: "Spell Check",
    0x00100000A0F: "Audio Volume Down",
    0x00100000A10: "Audio Volume Up",
    0x00100000A11: "Audio Volume Mute",
    0x00100000B01: "Launch Application 2",
    0x00100000B02: "Launch Calendar",
    0x00100000B03: "Launch Mail",
    0x00100000B04: "Launch Media Player",
    0x00100000B05: "Launch Music Player",
    0x00100000B06: "Launch Application 1",
    0x00100000B07: "Launch Screen Saver",
    0x00100000B08: "Launch Spreadsheet",
    0x00100000B09: "Launch Web Browser",
    0x00100000B0A: "Launch Web Cam",
    0x00100000B0B: "Launch Word Processor",
    0x00100000B0C: "Launch Contacts",
    0x00100000B0D: "Launch Phone",
    0x00100000B0E: "Launch Assistant",
    0x00100000B0F: "Launch Control Panel",
    0x00100000C01: "Browser Back",
    0x00100000C02: "Browser Favorites",
    0x00100000C03: "Browser Forward",
    0x00100000C04: "Browser Home",
    0x00100000C05: "Browser Refresh",
    0x00100000C06: "Browser Search",
    0x00100000C07: "Browser Stop",
    0x00100000D01: "Audio Balance Left",
    0x00100000D02: "Audio Balance Right",
    0x00100000D03: "Audio Bass Boost Down",
    0x00100000D04: "Audio Bass Boost Up",
    0x00100000D05: "Audio Fader Front",
    0x00100000D06: "Audio Fader Rear",
    0x00100000D07: "Audio Surround Mode Next",
    0x00100000D08: "AVR Input",
    0x00100000D09: "AVR Power",
    0x00100000D0A: "Channel Down",
    0x00100000D0B: "Channel Up",
    0x00100000D0C: "Color F0 Red",
    0x00100000D0D: "Color F1 Green",
    0x00100000D0E: "Color F2 Yellow",
    0x00100000D0F: "Color F3 Blue",
    0x00100000D10: "Color F4 Grey",
    0x00100000D11: "Color F5 Brown",
    0x00100000D12: "Closed Caption Toggle",
    0x00100000D13: "Dimmer",
    0x00100000D14: "Display Swap",
    0x00100000D15: "Exit",
    0x00100000D16: "Favorite Clear 0",
    0x00100000D17: "Favorite Clear 1",
    0x00100000D18: "Favorite Clear 2",
    0x00100000D19: "Favorite Clear 3",
    0x00100000D1A: "Favorite Recall 0",
    0x00100000D1B: "Favorite Recall 1",
    0x00100000D1C: "Favorite Recall 2",
    0x00100000D1D: "Favorite Recall 3",
    0x00100000D1E: "Favorite Store 0",
    0x00100000D1F: "Favorite Store 1",
    0x00100000D20: "Favorite Store 2",
    0x00100000D21: "Favorite Store 3",
    0x00100000D22: "Guide",
    0x00100000D23: "Guide Next Day",
    0x00100000D24: "Guide Previous Day",
    0x00100000D25: "Info",
    0x00100000D26: "Instant Replay",
    0x00100000D27: "Link",
    0x00100000D28: "List Program",
    0x00100000D29: "Live Content",
    0x00100000D2A: "Lock",
    0x00100000D2B: "Media Apps",
    0x00100000D2C: "Media Fast Forward",
    0x00100000D2D: "Media Last",
    0x00100000D2E: "Media Pause",
    0x00100000D2F: "Media Play",
    0x00100000D30: "Media Record",
    0x00100000D31: "Media Rewind",
    0x00100000D32: "Media Skip",
    0x00100000D33: "Next Favorite Channel",
    0x00100000D34: "Next User Profile",
    0x00100000D35: "On Demand",
    0x00100000D36: "P In P Down",
    0x00100000D37: "P In P Move",
    0x00100000D38: "P In P Toggle",
    0x00100000D39: "P In P Up",
    0x00100000D3A: "Play Speed Down",
    0x00100000D3B: "Play Speed Reset",
    0x00100000D3C: "Play Speed Up",
    0x00100000D3D: "Random Toggle",
    0x00100000D3E: "Rc Low Battery",
    0x00100000D3F: "Record Speed Next",
    0x00100000D40: "Rf Bypass",
    0x00100000D41: "Scan Channels Toggle",
    0x00100000D42: "Screen Mode Next",
    0x00100000D43: "Settings",
    0x00100000D44: "Split Screen Toggle",
    0x00100000D45: "STB Input",
    0x00100000D46: "STB Power",
    0x00100000D47: "Subtitle",
    0x00100000D48: "Teletext",
    0x00100000D49: "TV",
    0x00100000D4A: "TV Input",
    0x00100000D4B: "TV Power",
    0x00100000D4C: "Video Mode Next",
    0x00100000D4D: "Wink",
    0x00100000D4E: "Zoom Toggle",
    0x00100000D4F: "DVR",
    0x00100000D50: "Media Audio Track",
    0x00100000D51: "Media Skip Backward",
    0x00100000D52: "Media Skip Forward",
    0x00100000D53: "Media Step Backward",
    0x00100000D54: "Media Step Forward",
    0x00100000D55: "Media Top Menu",
    0x00100000D56: "Navigate In",
    0x00100000D57: "Navigate Next",
    0x00100000D58: "Navigate Out",
    0x00100000D59: "Navigate Previous",
    0x00100000D5A: "Pairing",
    0x00100000D5B: "Media Close",
    0x00100000E02: "Audio Bass Boost Toggle",
    0x00100000E04: "Audio Treble Down",
    0x00100000E05: "Audio Treble Up",
    0x00100000E06: "Microphone Toggle",
    0x00100000E07: "Microphone Volume Down",
    0x00100000E08: "Microphone Volume Up",
    0x00100000E09: "Microphone Volume Mute",
    0x00100000F01: "Speech Correction List",
    0x00100000F02: "Speech Input Toggle",
    0x00100001001: "App Switch",
    0x00100001002: "Call",
    0x00100001003: "Camera Focus",
    0x00100001004: "End Call",
    0x00100001005: "Go Back",
    0x00100001006: "Go Home",
    0x00100001007: "Headset Hook",
    0x00100001008: "Last Number Redial",
    0x00100001009: "Notification",
    0x0010000100A: "Manner Mode",
    0x0010000100B: "Voice Dial",
    0x00100001101: "TV 3 D Mode",
    0x00100001102: "TV Antenna Cable",
    0x00100001103: "TV Audio Description",
    0x00100001104: "TV Audio Description Mix Down",
    0x00100001105: "TV Audio Description Mix Up",
    0x00100001106: "TV Contents Menu",
    0x00100001107: "TV Data Service",
    0x00100001108: "TV Input Component 1",
    0x00100001109: "TV Input Component 2",
    0x0010000110A: "TV Input Composite 1",
    0x0010000110B: "TV Input Composite 2",
    0x0010000110C: "TV Input HDMI 1",
    0x0010000110D: "TV Input HDMI 2",
    0x0010000110E: "TV Input HDMI 3",
    0x0010000110F: "TV Input HDMI 4",
    0x00100001110: "TV Input VGA 1",
    0x00100001111: "TV Media Context",
    0x00100001112: "TV Network",
    0x00100001113: "TV Number Entry",
    0x00100001114: "TV Radio Service",
    0x00100001115: "TV Satellite",
    0x00100001116: "TV Satellite BS",
    0x00100001117: "TV Satellite CS",
    0x00100001118: "TV Satellite Toggle",
    0x00100001119: "TV Terrestrial Analog",
    0x0010000111A: "TV Terrestrial Digital",
    0x0010000111B: "TV Timer",
    0x00100001201: "Key 11",
    0x00100001202: "Key 12",
    0x00200000000: "Suspend",
    0x00200000001: "Resume",
    0x00200000002: "Sleep",
    0x00200000003: "Abort",
    0x00200000010: "Lang 1",
    0x00200000011: "Lang 2",
    0x00200000012: "Lang 3",
    0x00200000013: "Lang 4",
    0x00200000014: "Lang 5",
    0x00200000020: "Intl Backslash",
    0x00200000021: "Intl Ro",
    0x00200000022: "Intl Yen",
    0x00200000100: "Control Left",
    0x00200000101: "Control Right",
    0x00200000102: "Shift Left",
    0x00200000103: "Shift Right",
    0x00200000104: "Alt Left",
    0x00200000105: "Alt Right",
    0x00200000106: "Meta Left",
    0x00200000107: "Meta Right",
    0x002000001F0: "Control",
    0x002000001F2: "Shift",
    0x002000001F4: "Alt",
    0x002000001F6: "Meta",
    0x0020000020D: "Numpad Enter",
    0x00200000228: "Numpad Paren Left",
    0x00200000229: "Numpad Paren Right",
    0x0020000022A: "Numpad Multiply",
    0x0020000022B: "Numpad Add",
    0x0020000022C: "Numpad Comma",
    0x0020000022D: "Numpad Subtract",
    0x0020000022E: "Numpad Decimal",
    0x0020000022F: "Numpad Divide",
    0x00200000230: "Numpad 0",
    0x00200000231: "Numpad 1",
    0x00200000232: "Numpad 2",
    0x00200000233: "Numpad 3",
    0x00200000234: "Numpad 4",
    0x00200000235: "Numpad 5",
    0x00200000236: "Numpad 6",
    0x00200000237: "Numpad 7",
    0x00200000238: "Numpad 8",
    0x00200000239: "Numpad 9",
    0x0020000023D: "Numpad Equal",
    0x00200000301: "Game Button 1",
    0x00200000302: "Game Button 2",
    0x00200000303: "Game Button 3",
    0x00200000304: "Game Button 4",
    0x00200000305: "Game Button 5",
    0x00200000306: "Game Button 6",
    0x00200000307: "Game Button 7",
    0x00200000308: "Game Button 8",
    0x00200000309: "Game Button 9",
    0x0020000030A: "Game Button 10",
    0x0020000030B: "Game Button 11",
    0x0020000030C: "Game Button 12",
    0x0020000030D: "Game Button 13",
    0x0020000030E: "Game Button 14",
    0x0020000030F: "Game Button 15",
    0x00200000310: "Game Button 16",
    0x00200000311: "Game Button A",
    0x00200000312: "Game Button B",
    0x00200000313: "Game Button C",
    0x00200000314: "Game Button Left 1",
    0x00200000315: "Game Button Left 2",
    0x00200000316: "Game Button Mode",
    0x00200000317: "Game Button Right 1",
    0x00200000318: "Game Button Right 2",
    0x00200000319: "Game Button Select",
    0x0020000031A: "Game Button Start",
    0x0020000031B: "Game Button Thumb Left",
    0x0020000031C: "Game Button Thumb Right",
    0x0020000031D: "Game Button X",
    0x0020000031E: "Game Button Y",
    0x0020000031F: "Game Button Z",
}


class _LogicalKeyboardKey(FlutValueObject):
    _flut_type = "LogicalKeyboardKey"

    def __init__(self, keyId: int):
        super().__init__()
        self.keyId = keyId

    @staticmethod
    def _flut_unpack(data: dict) -> "_LogicalKeyboardKey":
        return _LogicalKeyboardKey(
            keyId=_flut_unpack_required_field(data, "keyId"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["keyId"] = _flut_pack_value(self.keyId)
        return result

    @property
    def keyLabel(self) -> str:
        if self.keyId & _planeMask == 0 and self.keyId >= 0x20:
            return chr(self.keyId)
        return ""

    @property
    def debugName(self) -> Optional[str]:
        return _keyLabels.get(self.keyId)

    def __eq__(self, other):
        if isinstance(other, _LogicalKeyboardKey):
            return self.keyId == other.keyId
        return False

    def __hash__(self):
        return hash(self.keyId)

    def __repr__(self):
        name = self.debugName or f"0x{self.keyId:08x}"
        return f"LogicalKeyboardKey({name})"


class LogicalKeyboardKey(_LogicalKeyboardKey):
    space = _LogicalKeyboardKey(0x00000000020)
    exclamation = _LogicalKeyboardKey(0x00000000021)
    quote = _LogicalKeyboardKey(0x00000000022)
    numberSign = _LogicalKeyboardKey(0x00000000023)
    dollar = _LogicalKeyboardKey(0x00000000024)
    percent = _LogicalKeyboardKey(0x00000000025)
    ampersand = _LogicalKeyboardKey(0x00000000026)
    quoteSingle = _LogicalKeyboardKey(0x00000000027)
    parenthesisLeft = _LogicalKeyboardKey(0x00000000028)
    parenthesisRight = _LogicalKeyboardKey(0x00000000029)
    asterisk = _LogicalKeyboardKey(0x0000000002A)
    add = _LogicalKeyboardKey(0x0000000002B)
    comma = _LogicalKeyboardKey(0x0000000002C)
    minus = _LogicalKeyboardKey(0x0000000002D)
    period = _LogicalKeyboardKey(0x0000000002E)
    slash = _LogicalKeyboardKey(0x0000000002F)

    digit0 = _LogicalKeyboardKey(0x00000000030)
    digit1 = _LogicalKeyboardKey(0x00000000031)
    digit2 = _LogicalKeyboardKey(0x00000000032)
    digit3 = _LogicalKeyboardKey(0x00000000033)
    digit4 = _LogicalKeyboardKey(0x00000000034)
    digit5 = _LogicalKeyboardKey(0x00000000035)
    digit6 = _LogicalKeyboardKey(0x00000000036)
    digit7 = _LogicalKeyboardKey(0x00000000037)
    digit8 = _LogicalKeyboardKey(0x00000000038)
    digit9 = _LogicalKeyboardKey(0x00000000039)

    colon = _LogicalKeyboardKey(0x0000000003A)
    semicolon = _LogicalKeyboardKey(0x0000000003B)
    less = _LogicalKeyboardKey(0x0000000003C)
    equal = _LogicalKeyboardKey(0x0000000003D)
    greater = _LogicalKeyboardKey(0x0000000003E)
    question = _LogicalKeyboardKey(0x0000000003F)
    at = _LogicalKeyboardKey(0x00000000040)

    bracketLeft = _LogicalKeyboardKey(0x0000000005B)
    backslash = _LogicalKeyboardKey(0x0000000005C)
    bracketRight = _LogicalKeyboardKey(0x0000000005D)
    caret = _LogicalKeyboardKey(0x0000000005E)
    underscore = _LogicalKeyboardKey(0x0000000005F)
    backquote = _LogicalKeyboardKey(0x00000000060)

    keyA = _LogicalKeyboardKey(0x00000000061)
    keyB = _LogicalKeyboardKey(0x00000000062)
    keyC = _LogicalKeyboardKey(0x00000000063)
    keyD = _LogicalKeyboardKey(0x00000000064)
    keyE = _LogicalKeyboardKey(0x00000000065)
    keyF = _LogicalKeyboardKey(0x00000000066)
    keyG = _LogicalKeyboardKey(0x00000000067)
    keyH = _LogicalKeyboardKey(0x00000000068)
    keyI = _LogicalKeyboardKey(0x00000000069)
    keyJ = _LogicalKeyboardKey(0x0000000006A)
    keyK = _LogicalKeyboardKey(0x0000000006B)
    keyL = _LogicalKeyboardKey(0x0000000006C)
    keyM = _LogicalKeyboardKey(0x0000000006D)
    keyN = _LogicalKeyboardKey(0x0000000006E)
    keyO = _LogicalKeyboardKey(0x0000000006F)
    keyP = _LogicalKeyboardKey(0x00000000070)
    keyQ = _LogicalKeyboardKey(0x00000000071)
    keyR = _LogicalKeyboardKey(0x00000000072)
    keyS = _LogicalKeyboardKey(0x00000000073)
    keyT = _LogicalKeyboardKey(0x00000000074)
    keyU = _LogicalKeyboardKey(0x00000000075)
    keyV = _LogicalKeyboardKey(0x00000000076)
    keyW = _LogicalKeyboardKey(0x00000000077)
    keyX = _LogicalKeyboardKey(0x00000000078)
    keyY = _LogicalKeyboardKey(0x00000000079)
    keyZ = _LogicalKeyboardKey(0x0000000007A)

    braceLeft = _LogicalKeyboardKey(0x0000000007B)
    bar = _LogicalKeyboardKey(0x0000000007C)
    braceRight = _LogicalKeyboardKey(0x0000000007D)
    tilde = _LogicalKeyboardKey(0x0000000007E)

    unidentified = _LogicalKeyboardKey(0x00100000001)

    backspace = _LogicalKeyboardKey(0x00100000008)
    tab = _LogicalKeyboardKey(0x00100000009)
    enter = _LogicalKeyboardKey(0x0010000000D)
    escape = _LogicalKeyboardKey(0x0010000001B)
    delete = _LogicalKeyboardKey(0x0010000007F)

    accel = _LogicalKeyboardKey(0x00100000101)
    altGraph = _LogicalKeyboardKey(0x00100000103)
    capsLock = _LogicalKeyboardKey(0x00100000104)
    fn = _LogicalKeyboardKey(0x00100000106)
    fnLock = _LogicalKeyboardKey(0x00100000107)
    hyper = _LogicalKeyboardKey(0x00100000108)
    numLock = _LogicalKeyboardKey(0x0010000010A)
    scrollLock = _LogicalKeyboardKey(0x0010000010C)
    superKey = _LogicalKeyboardKey(0x0010000010E)
    symbol = _LogicalKeyboardKey(0x0010000010F)
    symbolLock = _LogicalKeyboardKey(0x00100000110)
    shiftLevel5 = _LogicalKeyboardKey(0x00100000111)

    arrowDown = _LogicalKeyboardKey(0x00100000301)
    arrowLeft = _LogicalKeyboardKey(0x00100000302)
    arrowRight = _LogicalKeyboardKey(0x00100000303)
    arrowUp = _LogicalKeyboardKey(0x00100000304)

    end = _LogicalKeyboardKey(0x00100000305)
    home = _LogicalKeyboardKey(0x00100000306)
    pageDown = _LogicalKeyboardKey(0x00100000307)
    pageUp = _LogicalKeyboardKey(0x00100000308)

    clear = _LogicalKeyboardKey(0x00100000401)
    copy = _LogicalKeyboardKey(0x00100000402)
    crSel = _LogicalKeyboardKey(0x00100000403)
    cut = _LogicalKeyboardKey(0x00100000404)
    eraseEof = _LogicalKeyboardKey(0x00100000405)
    exSel = _LogicalKeyboardKey(0x00100000406)
    insert = _LogicalKeyboardKey(0x00100000407)
    paste = _LogicalKeyboardKey(0x00100000408)
    redo = _LogicalKeyboardKey(0x00100000409)
    undo = _LogicalKeyboardKey(0x0010000040A)

    accept = _LogicalKeyboardKey(0x00100000501)
    again = _LogicalKeyboardKey(0x00100000502)
    attn = _LogicalKeyboardKey(0x00100000503)
    cancel = _LogicalKeyboardKey(0x00100000504)
    contextMenu = _LogicalKeyboardKey(0x00100000505)
    execute = _LogicalKeyboardKey(0x00100000506)
    find = _LogicalKeyboardKey(0x00100000507)
    help = _LogicalKeyboardKey(0x00100000508)
    pause = _LogicalKeyboardKey(0x00100000509)
    play = _LogicalKeyboardKey(0x0010000050A)
    props = _LogicalKeyboardKey(0x0010000050B)
    select = _LogicalKeyboardKey(0x0010000050C)
    zoomIn = _LogicalKeyboardKey(0x0010000050D)
    zoomOut = _LogicalKeyboardKey(0x0010000050E)

    brightnessDown = _LogicalKeyboardKey(0x00100000601)
    brightnessUp = _LogicalKeyboardKey(0x00100000602)
    camera = _LogicalKeyboardKey(0x00100000603)
    eject = _LogicalKeyboardKey(0x00100000604)
    logOff = _LogicalKeyboardKey(0x00100000605)
    power = _LogicalKeyboardKey(0x00100000606)
    powerOff = _LogicalKeyboardKey(0x00100000607)
    printScreen = _LogicalKeyboardKey(0x00100000608)
    hibernate = _LogicalKeyboardKey(0x00100000609)
    standby = _LogicalKeyboardKey(0x0010000060A)
    wakeUp = _LogicalKeyboardKey(0x0010000060B)

    allCandidates = _LogicalKeyboardKey(0x00100000701)
    alphanumeric = _LogicalKeyboardKey(0x00100000702)
    codeInput = _LogicalKeyboardKey(0x00100000703)
    compose = _LogicalKeyboardKey(0x00100000704)
    convert = _LogicalKeyboardKey(0x00100000705)
    finalMode = _LogicalKeyboardKey(0x00100000706)
    groupFirst = _LogicalKeyboardKey(0x00100000707)
    groupLast = _LogicalKeyboardKey(0x00100000708)
    groupNext = _LogicalKeyboardKey(0x00100000709)
    groupPrevious = _LogicalKeyboardKey(0x0010000070A)
    modeChange = _LogicalKeyboardKey(0x0010000070B)
    nextCandidate = _LogicalKeyboardKey(0x0010000070C)
    nonConvert = _LogicalKeyboardKey(0x0010000070D)
    previousCandidate = _LogicalKeyboardKey(0x0010000070E)
    process = _LogicalKeyboardKey(0x0010000070F)
    singleCandidate = _LogicalKeyboardKey(0x00100000710)
    hangulMode = _LogicalKeyboardKey(0x00100000711)
    hanjaMode = _LogicalKeyboardKey(0x00100000712)
    junjaMode = _LogicalKeyboardKey(0x00100000713)
    eisu = _LogicalKeyboardKey(0x00100000714)
    hankaku = _LogicalKeyboardKey(0x00100000715)
    hiragana = _LogicalKeyboardKey(0x00100000716)
    hiraganaKatakana = _LogicalKeyboardKey(0x00100000717)
    kanaMode = _LogicalKeyboardKey(0x00100000718)
    kanjiMode = _LogicalKeyboardKey(0x00100000719)
    katakana = _LogicalKeyboardKey(0x0010000071A)
    romaji = _LogicalKeyboardKey(0x0010000071B)
    zenkaku = _LogicalKeyboardKey(0x0010000071C)
    zenkakuHankaku = _LogicalKeyboardKey(0x0010000071D)

    f1 = _LogicalKeyboardKey(0x00100000801)
    f2 = _LogicalKeyboardKey(0x00100000802)
    f3 = _LogicalKeyboardKey(0x00100000803)
    f4 = _LogicalKeyboardKey(0x00100000804)
    f5 = _LogicalKeyboardKey(0x00100000805)
    f6 = _LogicalKeyboardKey(0x00100000806)
    f7 = _LogicalKeyboardKey(0x00100000807)
    f8 = _LogicalKeyboardKey(0x00100000808)
    f9 = _LogicalKeyboardKey(0x00100000809)
    f10 = _LogicalKeyboardKey(0x0010000080A)
    f11 = _LogicalKeyboardKey(0x0010000080B)
    f12 = _LogicalKeyboardKey(0x0010000080C)
    f13 = _LogicalKeyboardKey(0x0010000080D)
    f14 = _LogicalKeyboardKey(0x0010000080E)
    f15 = _LogicalKeyboardKey(0x0010000080F)
    f16 = _LogicalKeyboardKey(0x00100000810)
    f17 = _LogicalKeyboardKey(0x00100000811)
    f18 = _LogicalKeyboardKey(0x00100000812)
    f19 = _LogicalKeyboardKey(0x00100000813)
    f20 = _LogicalKeyboardKey(0x00100000814)
    f21 = _LogicalKeyboardKey(0x00100000815)
    f22 = _LogicalKeyboardKey(0x00100000816)
    f23 = _LogicalKeyboardKey(0x00100000817)
    f24 = _LogicalKeyboardKey(0x00100000818)

    soft1 = _LogicalKeyboardKey(0x00100000901)
    soft2 = _LogicalKeyboardKey(0x00100000902)
    soft3 = _LogicalKeyboardKey(0x00100000903)
    soft4 = _LogicalKeyboardKey(0x00100000904)
    soft5 = _LogicalKeyboardKey(0x00100000905)
    soft6 = _LogicalKeyboardKey(0x00100000906)
    soft7 = _LogicalKeyboardKey(0x00100000907)
    soft8 = _LogicalKeyboardKey(0x00100000908)

    close = _LogicalKeyboardKey(0x00100000A01)
    mailForward = _LogicalKeyboardKey(0x00100000A02)
    mailReply = _LogicalKeyboardKey(0x00100000A03)
    mailSend = _LogicalKeyboardKey(0x00100000A04)
    mediaPlayPause = _LogicalKeyboardKey(0x00100000A05)
    mediaStop = _LogicalKeyboardKey(0x00100000A07)
    mediaTrackNext = _LogicalKeyboardKey(0x00100000A08)
    mediaTrackPrevious = _LogicalKeyboardKey(0x00100000A09)
    newKey = _LogicalKeyboardKey(0x00100000A0A)
    open = _LogicalKeyboardKey(0x00100000A0B)
    print = _LogicalKeyboardKey(0x00100000A0C)
    save = _LogicalKeyboardKey(0x00100000A0D)
    spellCheck = _LogicalKeyboardKey(0x00100000A0E)
    audioVolumeDown = _LogicalKeyboardKey(0x00100000A0F)
    audioVolumeUp = _LogicalKeyboardKey(0x00100000A10)
    audioVolumeMute = _LogicalKeyboardKey(0x00100000A11)

    launchApplication2 = _LogicalKeyboardKey(0x00100000B01)
    launchCalendar = _LogicalKeyboardKey(0x00100000B02)
    launchMail = _LogicalKeyboardKey(0x00100000B03)
    launchMediaPlayer = _LogicalKeyboardKey(0x00100000B04)
    launchMusicPlayer = _LogicalKeyboardKey(0x00100000B05)
    launchApplication1 = _LogicalKeyboardKey(0x00100000B06)
    launchScreenSaver = _LogicalKeyboardKey(0x00100000B07)
    launchSpreadsheet = _LogicalKeyboardKey(0x00100000B08)
    launchWebBrowser = _LogicalKeyboardKey(0x00100000B09)
    launchWebCam = _LogicalKeyboardKey(0x00100000B0A)
    launchWordProcessor = _LogicalKeyboardKey(0x00100000B0B)
    launchContacts = _LogicalKeyboardKey(0x00100000B0C)
    launchPhone = _LogicalKeyboardKey(0x00100000B0D)
    launchAssistant = _LogicalKeyboardKey(0x00100000B0E)
    launchControlPanel = _LogicalKeyboardKey(0x00100000B0F)

    browserBack = _LogicalKeyboardKey(0x00100000C01)
    browserFavorites = _LogicalKeyboardKey(0x00100000C02)
    browserForward = _LogicalKeyboardKey(0x00100000C03)
    browserHome = _LogicalKeyboardKey(0x00100000C04)
    browserRefresh = _LogicalKeyboardKey(0x00100000C05)
    browserSearch = _LogicalKeyboardKey(0x00100000C06)
    browserStop = _LogicalKeyboardKey(0x00100000C07)

    audioBalanceLeft = _LogicalKeyboardKey(0x00100000D01)
    audioBalanceRight = _LogicalKeyboardKey(0x00100000D02)
    audioBassBoostDown = _LogicalKeyboardKey(0x00100000D03)
    audioBassBoostUp = _LogicalKeyboardKey(0x00100000D04)
    audioFaderFront = _LogicalKeyboardKey(0x00100000D05)
    audioFaderRear = _LogicalKeyboardKey(0x00100000D06)
    audioSurroundModeNext = _LogicalKeyboardKey(0x00100000D07)
    avrInput = _LogicalKeyboardKey(0x00100000D08)
    avrPower = _LogicalKeyboardKey(0x00100000D09)
    channelDown = _LogicalKeyboardKey(0x00100000D0A)
    channelUp = _LogicalKeyboardKey(0x00100000D0B)
    colorF0Red = _LogicalKeyboardKey(0x00100000D0C)
    colorF1Green = _LogicalKeyboardKey(0x00100000D0D)
    colorF2Yellow = _LogicalKeyboardKey(0x00100000D0E)
    colorF3Blue = _LogicalKeyboardKey(0x00100000D0F)
    colorF4Grey = _LogicalKeyboardKey(0x00100000D10)
    colorF5Brown = _LogicalKeyboardKey(0x00100000D11)
    closedCaptionToggle = _LogicalKeyboardKey(0x00100000D12)
    dimmer = _LogicalKeyboardKey(0x00100000D13)
    displaySwap = _LogicalKeyboardKey(0x00100000D14)
    exit = _LogicalKeyboardKey(0x00100000D15)
    favoriteClear0 = _LogicalKeyboardKey(0x00100000D16)
    favoriteClear1 = _LogicalKeyboardKey(0x00100000D17)
    favoriteClear2 = _LogicalKeyboardKey(0x00100000D18)
    favoriteClear3 = _LogicalKeyboardKey(0x00100000D19)
    favoriteRecall0 = _LogicalKeyboardKey(0x00100000D1A)
    favoriteRecall1 = _LogicalKeyboardKey(0x00100000D1B)
    favoriteRecall2 = _LogicalKeyboardKey(0x00100000D1C)
    favoriteRecall3 = _LogicalKeyboardKey(0x00100000D1D)
    favoriteStore0 = _LogicalKeyboardKey(0x00100000D1E)
    favoriteStore1 = _LogicalKeyboardKey(0x00100000D1F)
    favoriteStore2 = _LogicalKeyboardKey(0x00100000D20)
    favoriteStore3 = _LogicalKeyboardKey(0x00100000D21)
    guide = _LogicalKeyboardKey(0x00100000D22)
    guideNextDay = _LogicalKeyboardKey(0x00100000D23)
    guidePreviousDay = _LogicalKeyboardKey(0x00100000D24)
    info = _LogicalKeyboardKey(0x00100000D25)
    instantReplay = _LogicalKeyboardKey(0x00100000D26)
    link = _LogicalKeyboardKey(0x00100000D27)
    listProgram = _LogicalKeyboardKey(0x00100000D28)
    liveContent = _LogicalKeyboardKey(0x00100000D29)
    lock = _LogicalKeyboardKey(0x00100000D2A)
    mediaApps = _LogicalKeyboardKey(0x00100000D2B)
    mediaFastForward = _LogicalKeyboardKey(0x00100000D2C)
    mediaLast = _LogicalKeyboardKey(0x00100000D2D)
    mediaPause = _LogicalKeyboardKey(0x00100000D2E)
    mediaPlay = _LogicalKeyboardKey(0x00100000D2F)
    mediaRecord = _LogicalKeyboardKey(0x00100000D30)
    mediaRewind = _LogicalKeyboardKey(0x00100000D31)
    mediaSkip = _LogicalKeyboardKey(0x00100000D32)
    nextFavoriteChannel = _LogicalKeyboardKey(0x00100000D33)
    nextUserProfile = _LogicalKeyboardKey(0x00100000D34)
    onDemand = _LogicalKeyboardKey(0x00100000D35)
    pInPDown = _LogicalKeyboardKey(0x00100000D36)
    pInPMove = _LogicalKeyboardKey(0x00100000D37)
    pInPToggle = _LogicalKeyboardKey(0x00100000D38)
    pInPUp = _LogicalKeyboardKey(0x00100000D39)
    playSpeedDown = _LogicalKeyboardKey(0x00100000D3A)
    playSpeedReset = _LogicalKeyboardKey(0x00100000D3B)
    playSpeedUp = _LogicalKeyboardKey(0x00100000D3C)
    randomToggle = _LogicalKeyboardKey(0x00100000D3D)
    rcLowBattery = _LogicalKeyboardKey(0x00100000D3E)
    recordSpeedNext = _LogicalKeyboardKey(0x00100000D3F)
    rfBypass = _LogicalKeyboardKey(0x00100000D40)
    scanChannelsToggle = _LogicalKeyboardKey(0x00100000D41)
    screenModeNext = _LogicalKeyboardKey(0x00100000D42)
    settings = _LogicalKeyboardKey(0x00100000D43)
    splitScreenToggle = _LogicalKeyboardKey(0x00100000D44)
    stbInput = _LogicalKeyboardKey(0x00100000D45)
    stbPower = _LogicalKeyboardKey(0x00100000D46)
    subtitle = _LogicalKeyboardKey(0x00100000D47)
    teletext = _LogicalKeyboardKey(0x00100000D48)
    tv = _LogicalKeyboardKey(0x00100000D49)
    tvInput = _LogicalKeyboardKey(0x00100000D4A)
    tvPower = _LogicalKeyboardKey(0x00100000D4B)
    videoModeNext = _LogicalKeyboardKey(0x00100000D4C)
    wink = _LogicalKeyboardKey(0x00100000D4D)
    zoomToggle = _LogicalKeyboardKey(0x00100000D4E)
    dvr = _LogicalKeyboardKey(0x00100000D4F)
    mediaAudioTrack = _LogicalKeyboardKey(0x00100000D50)
    mediaSkipBackward = _LogicalKeyboardKey(0x00100000D51)
    mediaSkipForward = _LogicalKeyboardKey(0x00100000D52)
    mediaStepBackward = _LogicalKeyboardKey(0x00100000D53)
    mediaStepForward = _LogicalKeyboardKey(0x00100000D54)
    mediaTopMenu = _LogicalKeyboardKey(0x00100000D55)
    navigateIn = _LogicalKeyboardKey(0x00100000D56)
    navigateNext = _LogicalKeyboardKey(0x00100000D57)
    navigateOut = _LogicalKeyboardKey(0x00100000D58)
    navigatePrevious = _LogicalKeyboardKey(0x00100000D59)
    pairing = _LogicalKeyboardKey(0x00100000D5A)
    mediaClose = _LogicalKeyboardKey(0x00100000D5B)

    audioBassBoostToggle = _LogicalKeyboardKey(0x00100000E02)
    audioTrebleDown = _LogicalKeyboardKey(0x00100000E04)
    audioTrebleUp = _LogicalKeyboardKey(0x00100000E05)
    microphoneToggle = _LogicalKeyboardKey(0x00100000E06)
    microphoneVolumeDown = _LogicalKeyboardKey(0x00100000E07)
    microphoneVolumeUp = _LogicalKeyboardKey(0x00100000E08)
    microphoneVolumeMute = _LogicalKeyboardKey(0x00100000E09)

    speechCorrectionList = _LogicalKeyboardKey(0x00100000F01)
    speechInputToggle = _LogicalKeyboardKey(0x00100000F02)

    appSwitch = _LogicalKeyboardKey(0x00100001001)
    call = _LogicalKeyboardKey(0x00100001002)
    cameraFocus = _LogicalKeyboardKey(0x00100001003)
    endCall = _LogicalKeyboardKey(0x00100001004)
    goBack = _LogicalKeyboardKey(0x00100001005)
    goHome = _LogicalKeyboardKey(0x00100001006)
    headsetHook = _LogicalKeyboardKey(0x00100001007)
    lastNumberRedial = _LogicalKeyboardKey(0x00100001008)
    notification = _LogicalKeyboardKey(0x00100001009)
    mannerMode = _LogicalKeyboardKey(0x0010000100A)
    voiceDial = _LogicalKeyboardKey(0x0010000100B)

    tv3DMode = _LogicalKeyboardKey(0x00100001101)
    tvAntennaCable = _LogicalKeyboardKey(0x00100001102)
    tvAudioDescription = _LogicalKeyboardKey(0x00100001103)
    tvAudioDescriptionMixDown = _LogicalKeyboardKey(0x00100001104)
    tvAudioDescriptionMixUp = _LogicalKeyboardKey(0x00100001105)
    tvContentsMenu = _LogicalKeyboardKey(0x00100001106)
    tvDataService = _LogicalKeyboardKey(0x00100001107)
    tvInputComponent1 = _LogicalKeyboardKey(0x00100001108)
    tvInputComponent2 = _LogicalKeyboardKey(0x00100001109)
    tvInputComposite1 = _LogicalKeyboardKey(0x0010000110A)
    tvInputComposite2 = _LogicalKeyboardKey(0x0010000110B)
    tvInputHDMI1 = _LogicalKeyboardKey(0x0010000110C)
    tvInputHDMI2 = _LogicalKeyboardKey(0x0010000110D)
    tvInputHDMI3 = _LogicalKeyboardKey(0x0010000110E)
    tvInputHDMI4 = _LogicalKeyboardKey(0x0010000110F)
    tvInputVGA1 = _LogicalKeyboardKey(0x00100001110)
    tvMediaContext = _LogicalKeyboardKey(0x00100001111)
    tvNetwork = _LogicalKeyboardKey(0x00100001112)
    tvNumberEntry = _LogicalKeyboardKey(0x00100001113)
    tvRadioService = _LogicalKeyboardKey(0x00100001114)
    tvSatellite = _LogicalKeyboardKey(0x00100001115)
    tvSatelliteBS = _LogicalKeyboardKey(0x00100001116)
    tvSatelliteCS = _LogicalKeyboardKey(0x00100001117)
    tvSatelliteToggle = _LogicalKeyboardKey(0x00100001118)
    tvTerrestrialAnalog = _LogicalKeyboardKey(0x00100001119)
    tvTerrestrialDigital = _LogicalKeyboardKey(0x0010000111A)
    tvTimer = _LogicalKeyboardKey(0x0010000111B)

    key11 = _LogicalKeyboardKey(0x00100001201)
    key12 = _LogicalKeyboardKey(0x00100001202)

    suspend = _LogicalKeyboardKey(0x00200000000)
    resume = _LogicalKeyboardKey(0x00200000001)
    sleep = _LogicalKeyboardKey(0x00200000002)
    abort = _LogicalKeyboardKey(0x00200000003)

    lang1 = _LogicalKeyboardKey(0x00200000010)
    lang2 = _LogicalKeyboardKey(0x00200000011)
    lang3 = _LogicalKeyboardKey(0x00200000012)
    lang4 = _LogicalKeyboardKey(0x00200000013)
    lang5 = _LogicalKeyboardKey(0x00200000014)

    intlBackslash = _LogicalKeyboardKey(0x00200000020)
    intlRo = _LogicalKeyboardKey(0x00200000021)
    intlYen = _LogicalKeyboardKey(0x00200000022)

    controlLeft = _LogicalKeyboardKey(0x00200000100)
    controlRight = _LogicalKeyboardKey(0x00200000101)
    shiftLeft = _LogicalKeyboardKey(0x00200000102)
    shiftRight = _LogicalKeyboardKey(0x00200000103)
    altLeft = _LogicalKeyboardKey(0x00200000104)
    altRight = _LogicalKeyboardKey(0x00200000105)
    metaLeft = _LogicalKeyboardKey(0x00200000106)
    metaRight = _LogicalKeyboardKey(0x00200000107)

    control = _LogicalKeyboardKey(0x002000001F0)
    shift = _LogicalKeyboardKey(0x002000001F2)
    alt = _LogicalKeyboardKey(0x002000001F4)
    meta = _LogicalKeyboardKey(0x002000001F6)

    numpadEnter = _LogicalKeyboardKey(0x0020000020D)
    numpadParenLeft = _LogicalKeyboardKey(0x00200000228)
    numpadParenRight = _LogicalKeyboardKey(0x00200000229)
    numpadMultiply = _LogicalKeyboardKey(0x0020000022A)
    numpadAdd = _LogicalKeyboardKey(0x0020000022B)
    numpadComma = _LogicalKeyboardKey(0x0020000022C)
    numpadSubtract = _LogicalKeyboardKey(0x0020000022D)
    numpadDecimal = _LogicalKeyboardKey(0x0020000022E)
    numpadDivide = _LogicalKeyboardKey(0x0020000022F)
    numpad0 = _LogicalKeyboardKey(0x00200000230)
    numpad1 = _LogicalKeyboardKey(0x00200000231)
    numpad2 = _LogicalKeyboardKey(0x00200000232)
    numpad3 = _LogicalKeyboardKey(0x00200000233)
    numpad4 = _LogicalKeyboardKey(0x00200000234)
    numpad5 = _LogicalKeyboardKey(0x00200000235)
    numpad6 = _LogicalKeyboardKey(0x00200000236)
    numpad7 = _LogicalKeyboardKey(0x00200000237)
    numpad8 = _LogicalKeyboardKey(0x00200000238)
    numpad9 = _LogicalKeyboardKey(0x00200000239)
    numpadEqual = _LogicalKeyboardKey(0x0020000023D)

    gameButton1 = _LogicalKeyboardKey(0x00200000301)
    gameButton2 = _LogicalKeyboardKey(0x00200000302)
    gameButton3 = _LogicalKeyboardKey(0x00200000303)
    gameButton4 = _LogicalKeyboardKey(0x00200000304)
    gameButton5 = _LogicalKeyboardKey(0x00200000305)
    gameButton6 = _LogicalKeyboardKey(0x00200000306)
    gameButton7 = _LogicalKeyboardKey(0x00200000307)
    gameButton8 = _LogicalKeyboardKey(0x00200000308)
    gameButton9 = _LogicalKeyboardKey(0x00200000309)
    gameButton10 = _LogicalKeyboardKey(0x0020000030A)
    gameButton11 = _LogicalKeyboardKey(0x0020000030B)
    gameButton12 = _LogicalKeyboardKey(0x0020000030C)
    gameButton13 = _LogicalKeyboardKey(0x0020000030D)
    gameButton14 = _LogicalKeyboardKey(0x0020000030E)
    gameButton15 = _LogicalKeyboardKey(0x0020000030F)
    gameButton16 = _LogicalKeyboardKey(0x00200000310)
    gameButtonA = _LogicalKeyboardKey(0x00200000311)
    gameButtonB = _LogicalKeyboardKey(0x00200000312)
    gameButtonC = _LogicalKeyboardKey(0x00200000313)
    gameButtonLeft1 = _LogicalKeyboardKey(0x00200000314)
    gameButtonLeft2 = _LogicalKeyboardKey(0x00200000315)
    gameButtonMode = _LogicalKeyboardKey(0x00200000316)
    gameButtonRight1 = _LogicalKeyboardKey(0x00200000317)
    gameButtonRight2 = _LogicalKeyboardKey(0x00200000318)
    gameButtonSelect = _LogicalKeyboardKey(0x00200000319)
    gameButtonStart = _LogicalKeyboardKey(0x0020000031A)
    gameButtonThumbLeft = _LogicalKeyboardKey(0x0020000031B)
    gameButtonThumbRight = _LogicalKeyboardKey(0x0020000031C)
    gameButtonX = _LogicalKeyboardKey(0x0020000031D)
    gameButtonY = _LogicalKeyboardKey(0x0020000031E)
    gameButtonZ = _LogicalKeyboardKey(0x0020000031F)


_physicalKeyLabels = {
    0x00070004: "Key A",
    0x00070005: "Key B",
    0x00070006: "Key C",
    0x00070007: "Key D",
    0x00070008: "Key E",
    0x00070009: "Key F",
    0x0007000A: "Key G",
    0x0007000B: "Key H",
    0x0007000C: "Key I",
    0x0007000D: "Key J",
    0x0007000E: "Key K",
    0x0007000F: "Key L",
    0x00070010: "Key M",
    0x00070011: "Key N",
    0x00070012: "Key O",
    0x00070013: "Key P",
    0x00070014: "Key Q",
    0x00070015: "Key R",
    0x00070016: "Key S",
    0x00070017: "Key T",
    0x00070018: "Key U",
    0x00070019: "Key V",
    0x0007001A: "Key W",
    0x0007001B: "Key X",
    0x0007001C: "Key Y",
    0x0007001D: "Key Z",
    0x0007001E: "Digit 1",
    0x0007001F: "Digit 2",
    0x00070020: "Digit 3",
    0x00070021: "Digit 4",
    0x00070022: "Digit 5",
    0x00070023: "Digit 6",
    0x00070024: "Digit 7",
    0x00070025: "Digit 8",
    0x00070026: "Digit 9",
    0x00070027: "Digit 0",
    0x00070028: "Enter",
    0x00070029: "Escape",
    0x0007002A: "Backspace",
    0x0007002B: "Tab",
    0x0007002C: "Space",
    0x0007004F: "Arrow Right",
    0x00070050: "Arrow Left",
    0x00070051: "Arrow Down",
    0x00070052: "Arrow Up",
}


class _PhysicalKeyboardKey(FlutValueObject):
    _flut_type = "PhysicalKeyboardKey"

    def __init__(self, usbHidUsage: int):
        super().__init__()
        self.usbHidUsage = usbHidUsage

    @staticmethod
    def _flut_unpack(data: dict) -> "_PhysicalKeyboardKey":
        return _PhysicalKeyboardKey(
            usbHidUsage=_flut_unpack_required_field(data, "usbHidUsage"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["usbHidUsage"] = _flut_pack_value(self.usbHidUsage)
        return result

    @property
    def debugName(self) -> Optional[str]:
        return _physicalKeyLabels.get(self.usbHidUsage)

    def __eq__(self, other):
        if isinstance(other, _PhysicalKeyboardKey):
            return self.usbHidUsage == other.usbHidUsage
        return False

    def __hash__(self):
        return hash(self.usbHidUsage)

    def __repr__(self):
        name = self.debugName or f"0x{self.usbHidUsage:08x}"
        return f"PhysicalKeyboardKey({name})"


class PhysicalKeyboardKey(_PhysicalKeyboardKey):
    keyA = _PhysicalKeyboardKey(0x00070004)
    keyB = _PhysicalKeyboardKey(0x00070005)
    keyC = _PhysicalKeyboardKey(0x00070006)
    keyD = _PhysicalKeyboardKey(0x00070007)
    keyE = _PhysicalKeyboardKey(0x00070008)
    keyF = _PhysicalKeyboardKey(0x00070009)
    keyG = _PhysicalKeyboardKey(0x0007000A)
    keyH = _PhysicalKeyboardKey(0x0007000B)
    keyI = _PhysicalKeyboardKey(0x0007000C)
    keyJ = _PhysicalKeyboardKey(0x0007000D)
    keyK = _PhysicalKeyboardKey(0x0007000E)
    keyL = _PhysicalKeyboardKey(0x0007000F)
    keyM = _PhysicalKeyboardKey(0x00070010)
    keyN = _PhysicalKeyboardKey(0x00070011)
    keyO = _PhysicalKeyboardKey(0x00070012)
    keyP = _PhysicalKeyboardKey(0x00070013)
    keyQ = _PhysicalKeyboardKey(0x00070014)
    keyR = _PhysicalKeyboardKey(0x00070015)
    keyS = _PhysicalKeyboardKey(0x00070016)
    keyT = _PhysicalKeyboardKey(0x00070017)
    keyU = _PhysicalKeyboardKey(0x00070018)
    keyV = _PhysicalKeyboardKey(0x00070019)
    keyW = _PhysicalKeyboardKey(0x0007001A)
    keyX = _PhysicalKeyboardKey(0x0007001B)
    keyY = _PhysicalKeyboardKey(0x0007001C)
    keyZ = _PhysicalKeyboardKey(0x0007001D)

    digit1 = _PhysicalKeyboardKey(0x0007001E)
    digit2 = _PhysicalKeyboardKey(0x0007001F)
    digit3 = _PhysicalKeyboardKey(0x00070020)
    digit4 = _PhysicalKeyboardKey(0x00070021)
    digit5 = _PhysicalKeyboardKey(0x00070022)
    digit6 = _PhysicalKeyboardKey(0x00070023)
    digit7 = _PhysicalKeyboardKey(0x00070024)
    digit8 = _PhysicalKeyboardKey(0x00070025)
    digit9 = _PhysicalKeyboardKey(0x00070026)
    digit0 = _PhysicalKeyboardKey(0x00070027)

    enter = _PhysicalKeyboardKey(0x00070028)
    escape = _PhysicalKeyboardKey(0x00070029)
    backspace = _PhysicalKeyboardKey(0x0007002A)
    tab = _PhysicalKeyboardKey(0x0007002B)
    space = _PhysicalKeyboardKey(0x0007002C)

    arrowRight = _PhysicalKeyboardKey(0x0007004F)
    arrowLeft = _PhysicalKeyboardKey(0x00070050)
    arrowDown = _PhysicalKeyboardKey(0x00070051)
    arrowUp = _PhysicalKeyboardKey(0x00070052)
