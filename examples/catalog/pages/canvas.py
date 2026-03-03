import math

from flut.dart import (
    Color,
    ColorSpace,
    Offset,
    Paint,
    PaintingStyle,
    Rect,
    Size,
    StrokeCap,
    StrokeJoin,
    BlendMode,
)
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Center,
    Padding,
    ConstrainedBox,
    CustomPaint,
)
from flut.flutter.rendering import (
    CrossAxisAlignment,
    BoxConstraints,
    CustomPainter,
)
from flut.flutter.material import (
    Colors,
    ElevatedButton,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BorderRadius,
    BoxDecoration,
)
from widgets import CatalogPage, SplitViewTile, CodeArea


class _RectMethodsPainter(CustomPainter):
    def paint(self, canvas, size):
        bg = Paint()
        bg.color = Color(0xFFF5F5F5)
        canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), bg)

        a = Offset(40, 30)
        b = Offset(220, 130)
        rect = Rect.fromPoints(a, b)
        rp = Paint()
        rp.color = Color(0xFF1565C0)
        rp.style = PaintingStyle.stroke
        rp.strokeWidth = 2.0
        canvas.drawRect(rect, rp)
        fp = Paint()
        fp.color = Color(0x201565C0)
        canvas.drawRect(rect, fp)
        dot = Paint()
        dot.color = Color(0xFFE53935)
        for pt in [rect.topLeft, rect.topRight, rect.bottomLeft, rect.bottomRight]:
            canvas.drawCircle(pt, 4, dot)
        cp = Paint()
        cp.color = Color(0xFF43A047)
        canvas.drawCircle(rect.center, 5, cp)
        shifted = rect.shift(Offset(15, 15))
        sp = Paint()
        sp.color = Color(0xFFFF8F00)
        sp.style = PaintingStyle.stroke
        sp.strokeWidth = 1.5
        canvas.drawRect(shifted, sp)
        inflated = rect.inflate(8)
        ip = Paint()
        ip.color = Color(0xFF8E24AA)
        ip.style = PaintingStyle.stroke
        ip.strokeWidth = 1.0
        canvas.drawRect(inflated, ip)
        other = Rect.fromLTWH(140, 70, 180, 90)
        op = Paint()
        op.color = Color(0x3043A047)
        canvas.drawRect(other, op)
        inter = rect.intersect(other)
        xp = Paint()
        xp.color = Color(0x60FFEB3B)
        canvas.drawRect(inter, xp)


class _StrokeCapJoinPainter(CustomPainter):
    def paint(self, canvas, size):
        bg = Paint()
        bg.color = Color(0xFFF5F5F5)
        canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), bg)

        caps = [
            (StrokeCap.butt, Color(0xFFE53935)),
            (StrokeCap.round, Color(0xFF43A047)),
            (StrokeCap.square, Color(0xFF1E88E5)),
        ]
        y = 30.0
        for cap, color in caps:
            p = Paint()
            p.color = color
            p.strokeWidth = 14.0
            p.strokeCap = cap
            p.style = PaintingStyle.stroke
            canvas.drawLine(Offset(80, y), Offset(220, y), p)
            y += 40

        joins = [
            (StrokeJoin.miter, Color(0xFFFF8F00)),
            (StrokeJoin.round, Color(0xFF8E24AA)),
            (StrokeJoin.bevel, Color(0xFF00838F)),
        ]
        x = 30.0
        for join, color in joins:
            p = Paint()
            p.color = color
            p.strokeWidth = 6.0
            p.strokeJoin = join
            p.style = PaintingStyle.stroke
            canvas.drawLine(
                Offset(x, size.height - 15), Offset(x + 25, size.height - 50), p
            )
            canvas.drawLine(
                Offset(x + 25, size.height - 50), Offset(x + 50, size.height - 15), p
            )
            x += 85


class _BlendModePainter(CustomPainter):
    def paint(self, canvas, size):
        bg = Paint()
        bg.color = Color(0xFFFFFFFF)
        canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), bg)

        modes = [
            BlendMode.srcOver,
            BlendMode.multiply,
            BlendMode.screen,
            BlendMode.overlay,
        ]
        x = 50.0
        for mode in modes:
            base = Paint()
            base.color = Color(0xFF1565C0)
            canvas.drawCircle(Offset(x, 45), 28, base)
            blend = Paint()
            blend.color = Color(0xFFE53935)
            blend.blendMode = mode
            canvas.drawCircle(Offset(x + 18, 45), 28, blend)
            x += 85


class _ConstantsPainter(CustomPainter):
    def paint(self, canvas, size):
        bg = Paint()
        bg.color = Color(0xFFF5F5F5)
        canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), bg)

        label = Paint()
        label.color = Color(0xFF333333)
        label.strokeWidth = 1.0
        origin = Offset.zero
        marker = Paint()
        marker.color = Color(0xFFE53935)
        canvas.drawCircle(origin, 6, marker)
        delta = Offset(30, 20)
        moved = Offset.zero + delta
        canvas.drawCircle(moved, 4, marker)
        canvas.drawLine(origin, moved, label)
        box_paint = Paint()
        box_paint.color = Color(0xFF1E88E5)
        box_paint.style = PaintingStyle.stroke
        box_paint.strokeWidth = 2.0
        rect = Offset(60, 10) & Size(100, 60)
        canvas.drawRect(rect, box_paint)
        grown = Size.zero + Offset(80, 50)
        dot = Paint()
        dot.color = Color(0xFF43A047)
        canvas.drawCircle(Offset(200, 40), grown.width / 4, dot)
        spaces = [
            (ColorSpace.sRGB, 0.3),
            (ColorSpace.displayP3, 0.6),
            (ColorSpace.extendedSRGB, 0.9),
        ]
        cs_paint = Paint()
        y = 90.0
        for cs, green in spaces:
            cs_paint.color = Color.from_(
                alpha=1.0, red=0.2, green=green, blue=0.4, colorSpace=cs
            )
            canvas.drawCircle(Offset(40, y), 14, cs_paint)
            y += 36
        inf_paint = Paint()
        inf_paint.color = Color(0xFFFF8F00)
        canvas.drawCircle(Offset.infinite, 5, inf_paint)
        inf_rect = Offset.zero & Size.infinite
        canvas.drawRect(inf_rect, inf_paint)


class SmileyPainter(CustomPainter):
    def paint(self, canvas, size):
        face = Paint()
        face.color = Color(0xFFEECC00)

        eye = Paint()
        eye.color = Color(0xFF000000)

        smile = Paint()
        smile.color = Color(0xFF000000)
        smile.strokeWidth = 5.0
        smile.style = PaintingStyle.stroke

        cx = size.width / 2
        cy = size.height / 2
        r = min(cx, cy) - 10

        canvas.drawCircle(Offset(cx, cy), r, face)
        canvas.drawCircle(Offset(cx - r * 0.27, cy - r * 0.2), r * 0.08, eye)
        canvas.drawCircle(Offset(cx + r * 0.27, cy - r * 0.2), r * 0.08, eye)
        canvas.drawLine(
            Offset(cx - r * 0.35, cy + r * 0.25),
            Offset(cx + r * 0.35, cy + r * 0.25),
            smile,
        )


class GridPainter(CustomPainter):
    def __init__(self, spacing=20, color=None):
        super().__init__()
        self.spacing = spacing
        self.grid_color = color or Color(0x30000000)

    def paint(self, canvas, size):
        p = Paint()
        p.color = self.grid_color
        p.strokeWidth = 0.5

        x = 0.0
        while x <= size.width:
            canvas.drawLine(Offset(x, 0), Offset(x, size.height), p)
            x += self.spacing

        y = 0.0
        while y <= size.height:
            canvas.drawLine(Offset(0, y), Offset(size.width, y), p)
            y += self.spacing


class ShapesPainter(CustomPainter):
    def __init__(self, hue_offset=0.0):
        super().__init__()
        self.hue_offset = hue_offset

    def _hue_color(self, hue):
        h = (hue + self.hue_offset) % 360
        s = 0.8
        v = 0.9
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        return Color.fromARGB(
            255, int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)
        )

    def paint(self, canvas, size):
        from flut.dart.ui import Rect

        fill = Paint()
        stroke = Paint()
        stroke.style = PaintingStyle.stroke
        stroke.strokeWidth = 2.0

        fill.color = self._hue_color(0)
        canvas.drawCircle(Offset(50, 80), 35, fill)
        stroke.color = self._hue_color(0)
        canvas.drawCircle(Offset(50, 80), 35, stroke)

        fill.color = self._hue_color(90)
        canvas.drawRect(Rect.fromLTWH(105, 45, 70, 70), fill)

        fill.color = self._hue_color(180)
        canvas.drawOval(Rect.fromLTWH(195, 45, 80, 70), fill)

        fill.color = self._hue_color(270)
        canvas.drawArc(Rect.fromLTWH(295, 45, 55, 70), 0, math.pi * 1.5, True, fill)

        canvas.save()
        canvas.translate(80, size.height - 60)
        labels_paint = Paint()
        labels_paint.color = Color(0xFF666666)
        labels_paint.strokeWidth = 1.5
        labels_paint.style = PaintingStyle.stroke
        canvas.drawCircle(Offset(0, 0), 20, labels_paint)
        canvas.restore()


class _ShapesGalleryDemo(StatefulWidget):
    def createState(self):
        return _ShapesGalleryDemoState()


class _ShapesGalleryDemoState(State[_ShapesGalleryDemo]):
    def initState(self):
        self.hue_offset = 0.0

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text(f"Rotate Hue (+30\u00b0)"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "hue_offset",
                                    (self.hue_offset + 30) % 360,
                                )
                            ),
                        ),
                        SizedBox(width=12),
                        Text(
                            f"Offset: {self.hue_offset:.0f}\u00b0",
                            style=TextStyle(fontSize=13, color=Colors.grey),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    decoration=BoxDecoration(
                        color=Colors.white,
                        borderRadius=BorderRadius.circular(12),
                    ),
                    child=CustomPaint(
                        size=Size(360, 180),
                        painter=ShapesPainter(hue_offset=self.hue_offset),
                    ),
                ),
            ],
        )


class _GridOverlayDemo(StatefulWidget):
    def createState(self):
        return _GridOverlayDemoState()


class _GridOverlayDemoState(State[_GridOverlayDemo]):
    def initState(self):
        self.grid_spacing = 20

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text(f"Toggle Grid ({self.grid_spacing}px)"),
                            onPressed=lambda: self.setState(
                                lambda: setattr(
                                    self,
                                    "grid_spacing",
                                    40 if self.grid_spacing == 20 else 20,
                                )
                            ),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Container(
                    decoration=BoxDecoration(
                        color=Colors.grey.withValues(alpha=0.03),
                        borderRadius=BorderRadius.circular(12),
                    ),
                    child=CustomPaint(
                        size=Size(560, 160),
                        painter=GridPainter(spacing=self.grid_spacing),
                    ),
                ),
            ],
        )


class _ForegroundBgPainter(CustomPainter):
    def paint(self, canvas, size):
        bg = Paint()
        bg.color = Color(0xFF1565C0)
        canvas.drawRect(Rect.fromLTWH(20, 20, size.width - 40, size.height - 40), bg)

    def shouldRepaint(self, old):
        return False


class _ForegroundXPainter(CustomPainter):
    def paint(self, canvas, size):
        xp = Paint()
        xp.color = Color(0xFFE53935)
        xp.strokeWidth = 4.0
        xp.style = PaintingStyle.stroke
        canvas.drawLine(Offset(0, 0), Offset(size.width, size.height), xp)
        canvas.drawLine(Offset(size.width, 0), Offset(0, size.height), xp)

    def shouldRepaint(self, old):
        return False


class _ComplexPatternPainter(CustomPainter):
    def paint(self, canvas, size):
        bg = Paint()
        bg.color = Color(0xFFF5F5F5)
        canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), bg)
        p = Paint()
        p.strokeWidth = 2.0
        p.style = PaintingStyle.stroke
        colors = [Color(0xFF1565C0), Color(0xFFE53935), Color(0xFF43A047)]
        y = 15.0
        for i in range(5):
            p.color = colors[i % 3]
            canvas.drawCircle(Offset(size.width / 2, y + 10), 8, p)
            canvas.drawRect(Rect.fromLTWH(10, y, size.width - 20, 20), p)
            y += 25.0

    def shouldRepaint(self, old):
        return False


class CanvasPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Canvas & CustomPaint",
            description=(
                "Explains custom drawing from simple shapes to layered scenes, "
                "while showing how paint commands issued in Python appear on the "
                "Flutter canvas."
            ),
            children=[
                SplitViewTile(
                    title="Smiley Face",
                    description="drawCircle + drawLine with fill and stroke Paint styles.",
                    instruction="A static CustomPainter demo. The smiley is drawn with circles for the face and eyes, and a line for the mouth.",
                    visible=Center(
                        child=Container(
                            decoration=BoxDecoration(
                                color=Colors.white,
                                borderRadius=BorderRadius.circular(12),
                            ),
                            child=CustomPaint(
                                size=Size(200, 200),
                                painter=SmileyPainter(),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class SmileyPainter(CustomPainter):\n"
                            "    def paint(self, canvas, size):\n"
                            "        face = Paint()\n"
                            "        face.color = Color(0xFFEECC00)\n"
                            "        cx = size.width / 2\n"
                            "        cy = size.height / 2\n"
                            "        r = min(cx, cy) - 10\n"
                            "        canvas.drawCircle(Offset(cx, cy), r, face)\n\n"
                            "CustomPaint(\n"
                            "    size=Size(200, 200),\n"
                            "    painter=SmileyPainter(),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Shapes Gallery",
                    description="drawCircle, drawRect, drawOval, drawArc with HSV color cycling via a hue offset parameter.",
                    instruction="Click Rotate Hue to shift all shape colors by 30\u00b0 around the HSV wheel. The offset value is shown next to the button.",
                    visible=_ShapesGalleryDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class ShapesPainter(CustomPainter):\n"
                            "    def __init__(self, hue_offset=0.0):\n"
                            "        super().__init__()\n"
                            "        self.hue_offset = hue_offset\n\n"
                            "    def paint(self, canvas, size):\n"
                            "        fill = Paint()\n"
                            "        fill.color = hue_color(0)\n"
                            "        canvas.drawCircle(Offset(80, 80), 40, fill)\n"
                            "        fill.color = hue_color(90)\n"
                            "        canvas.drawRect(Rect.fromLTWH(160, 40, 80, 80), fill)\n\n"
                            "CustomPaint(\n"
                            "    size=Size(560, 180),\n"
                            "    painter=ShapesPainter(hue_offset=30),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Grid Overlay",
                    description="drawLine in a loop to render a grid. Tests canvas performance with many sequential draw calls.",
                    instruction="Click Toggle Grid to switch the grid spacing between 20px and 40px.",
                    visible=_GridOverlayDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class GridPainter(CustomPainter):\n"
                            "    def __init__(self, spacing=20):\n"
                            "        super().__init__()\n"
                            "        self.spacing = spacing\n\n"
                            "    def paint(self, canvas, size):\n"
                            "        p = Paint()\n"
                            "        p.strokeWidth = 0.5\n"
                            "        x = 0.0\n"
                            "        while x <= size.width:\n"
                            "            canvas.drawLine(Offset(x, 0), Offset(x, size.height), p)\n"
                            "            x += self.spacing\n\n"
                            "CustomPaint(\n"
                            "    size=Size(560, 160),\n"
                            "    painter=GridPainter(spacing=20),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Rect Methods",
                    description="Rect.fromPoints, shift, inflate, intersect exercised through real draw calls.",
                    instruction="Blue: original Rect.fromPoints(a,b). Red dots: corners (topLeft, topRight, bottomLeft, bottomRight). Green dot: center. Orange: shifted by (15,15). Purple: inflated by 8. Semi-green rect overlaps; yellow highlights the intersection.",
                    visible=Container(
                        decoration=BoxDecoration(
                            color=Colors.white,
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=CustomPaint(
                            size=Size(360, 180),
                            painter=_RectMethodsPainter(),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "a, b = Offset(40, 30), Offset(220, 130)\n"
                            "rect = Rect.fromPoints(a, b)\n\n"
                            "rect.center       # midpoint Offset\n"
                            "rect.topLeft       # corner Offsets\n\n"
                            "rect.shift(Offset(15, 15))   # translate\n"
                            "rect.inflate(8)              # grow\n"
                            "rect.intersect(other)        # overlap"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="StrokeCap & StrokeJoin",
                    description="Paint.strokeCap and Paint.strokeJoin control line endings and corner shapes.",
                    instruction="Top: lines with StrokeCap.butt (red), .round (green), .square (blue). Bottom: V-shapes with StrokeJoin.miter (orange), .round (purple), .bevel (teal).",
                    visible=Container(
                        decoration=BoxDecoration(
                            color=Colors.white,
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=CustomPaint(
                            size=Size(300, 190),
                            painter=_StrokeCapJoinPainter(),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "p = Paint()\n"
                            "p.strokeCap = StrokeCap.round\n"
                            "p.strokeJoin = StrokeJoin.bevel\n"
                            "p.strokeWidth = 14.0\n"
                            "p.style = PaintingStyle.stroke\n"
                            "canvas.drawLine(start, end, p)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="BlendMode",
                    description="Paint.blendMode controls how overlapping colours combine.",
                    instruction="Overlapping blue + red circles: srcOver (normal), multiply, screen, overlay — left to right.",
                    visible=Container(
                        decoration=BoxDecoration(
                            color=Colors.white,
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=CustomPaint(
                            size=Size(370, 90),
                            painter=_BlendModePainter(),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "p = Paint()\n"
                            "p.color = Color(0xFFE53935)\n"
                            "p.blendMode = BlendMode.multiply\n"
                            "canvas.drawCircle(center, 28, p)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="dart:ui Constants",
                    description="Exercises Size.zero/infinite, Offset.zero/infinite and ColorSpace through real FFI draw calls.",
                    instruction="Red dots: Offset.zero at origin + arithmetic. Blue rect: Offset & Size. Green circle: Size.zero + Offset. Colored circles: Color.from_ with each ColorSpace. Orange: Offset.infinite and Size.infinite sent directly through FFI (Flutter clips to canvas bounds). If inf serialization is broken, the tile crashes.",
                    visible=Container(
                        decoration=BoxDecoration(
                            color=Colors.white,
                            borderRadius=BorderRadius.circular(12),
                        ),
                        child=CustomPaint(
                            size=Size(280, 200),
                            painter=_ConstantsPainter(),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "# Offset.zero at origin, then arithmetic\n"
                            "canvas.drawCircle(Offset.zero, 6, red)\n"
                            "moved = Offset.zero + Offset(30, 20)\n\n"
                            "# Size.zero arithmetic\n"
                            "grown = Size.zero + Offset(80, 50)\n\n"
                            "# ColorSpace through Color.from_\n"
                            "Color.from_(alpha=1, red=0.2, green=0.6,\n"
                            "    blue=0.4, colorSpace=ColorSpace.displayP3)\n\n"
                            "# inf goes through FFI — crashes if broken\n"
                            "canvas.drawCircle(Offset.infinite, 5, paint)\n"
                            "canvas.drawRect(Offset.zero & Size.infinite, paint)"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CustomPaint foregroundPainter",
                    description="CustomPaint with both painter (blue rect background) and foregroundPainter (red X crosshair drawn on top).",
                    instruction="The blue rectangle is drawn by the painter. The red X is drawn by the foregroundPainter on top of everything, including any child widget.",
                    visible=Center(
                        child=Container(
                            decoration=BoxDecoration(
                                color=Colors.white,
                                borderRadius=BorderRadius.circular(12),
                            ),
                            child=CustomPaint(
                                size=Size(200, 160),
                                painter=_ForegroundBgPainter(),
                                foregroundPainter=_ForegroundXPainter(),
                            ),
                        ),
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "class BgPainter(CustomPainter):\n"
                            "    def paint(self, canvas, size):\n"
                            "        p = Paint()\n"
                            "        p.color = Color(0xFF1565C0)\n"
                            "        canvas.drawRect(\n"
                            "            Rect.fromLTWH(20, 20,\n"
                            "                size.width-40, size.height-40), p)\n\n"
                            "class XPainter(CustomPainter):\n"
                            "    def paint(self, canvas, size):\n"
                            "        p = Paint()\n"
                            "        p.color = Color(0xFFE53935)\n"
                            "        p.strokeWidth = 4.0\n"
                            "        p.style = PaintingStyle.stroke\n"
                            "        canvas.drawLine(\n"
                            "            Offset(0,0),\n"
                            "            Offset(size.width, size.height), p)\n\n"
                            "CustomPaint(\n"
                            "    size=Size(200, 160),\n"
                            "    painter=BgPainter(),\n"
                            "    foregroundPainter=XPainter(),\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="CustomPaint isComplex & willChange",
                    description="Two CustomPaints side by side: one with isComplex=True and willChange=True (performance hints), one with defaults. Both draw the same pattern.",
                    instruction="Left: isComplex=True, willChange=True (tells Flutter to cache and expect frequent repaints). Right: default settings. Visually identical output, different performance characteristics.",
                    visible=Row(
                        children=[
                            Column(
                                children=[
                                    Container(
                                        decoration=BoxDecoration(
                                            color=Colors.white,
                                            borderRadius=BorderRadius.circular(12),
                                        ),
                                        child=CustomPaint(
                                            size=Size(150, 150),
                                            painter=_ComplexPatternPainter(),
                                            isComplex=True,
                                            willChange=True,
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    Text(
                                        "isComplex=True",
                                        style=TextStyle(fontSize=11, color=Colors.grey),
                                    ),
                                ],
                            ),
                            SizedBox(width=16),
                            Column(
                                children=[
                                    Container(
                                        decoration=BoxDecoration(
                                            color=Colors.white,
                                            borderRadius=BorderRadius.circular(12),
                                        ),
                                        child=CustomPaint(
                                            size=Size(150, 150),
                                            painter=_ComplexPatternPainter(),
                                        ),
                                    ),
                                    SizedBox(height=4),
                                    Text(
                                        "default",
                                        style=TextStyle(fontSize=11, color=Colors.grey),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    code=CodeArea(
                        language="python",
                        code=(
                            "CustomPaint(\n"
                            "    size=Size(150, 150),\n"
                            "    painter=PatternPainter(),\n"
                            "    isComplex=True,\n"
                            "    willChange=True,\n"
                            ")\n\n"
                            "CustomPaint(\n"
                            "    size=Size(150, 150),\n"
                            "    painter=PatternPainter(),\n"
                            ")"
                        ),
                    ),
                ),
            ],
        )
