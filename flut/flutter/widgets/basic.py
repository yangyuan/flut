from typing import Callable, Optional, override

from flut._flut.engine import named_constructor, wrap_widget_builder, _flut_pack_value
from flut.flutter.rendering.box import BoxConstraints
from flut.flutter.rendering.flex import (
    FlexFit,
    MainAxisAlignment,
    MainAxisSize,
    CrossAxisAlignment,
)
from flut.flutter.rendering.wrap import WrapAlignment, WrapCrossAlignment
from flut.flutter.painting.alignment import Alignment, AlignmentDirectional
from flut.flutter.painting.basic_types import Axis, VerticalDirection
from flut.flutter.painting.border_radius import BorderRadius
from flut.flutter.painting.box_fit import BoxFit
from flut.flutter.rendering.stack import StackFit
from flut.flutter.services.mouse_cursor import MouseCursor
from flut.dart.ui import Clip, Offset, Size, TextBaseline, TextDirection
from flut.flutter.rendering.custom_paint import CustomPainter
from flut.flutter.widgets.framework import BuildContext, Widget


class Center(Widget):
    _flut_type = "Center"

    def __init__(
        self,
        *,
        key=None,
        widthFactor: Optional[float] = None,
        heightFactor: Optional[float] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.widthFactor = widthFactor
        self.heightFactor = heightFactor
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.widthFactor is not None:
            result["widthFactor"] = _flut_pack_value(self.widthFactor)
        if self.heightFactor is not None:
            result["heightFactor"] = _flut_pack_value(self.heightFactor)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class Expanded(Widget):
    _flut_type = "Expanded"

    def __init__(
        self,
        *,
        key=None,
        flex: int = 1,
        child,
    ):
        super().__init__(key=key)
        self.flex = flex
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["flex"] = _flut_pack_value(self.flex)
        result["child"] = _flut_pack_value(self.child)
        return result


class Flexible(Widget):
    _flut_type = "Flexible"

    def __init__(
        self,
        *,
        key=None,
        flex: int = 1,
        fit: FlexFit = FlexFit.loose,
        child,
    ):
        super().__init__(key=key)
        self.flex = flex
        self.fit = fit
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["flex"] = _flut_pack_value(self.flex)
        result["fit"] = _flut_pack_value(self.fit)
        result["child"] = _flut_pack_value(self.child)
        return result


class SizedBox(Widget):
    _flut_type = "SizedBox"

    def __init__(
        self,
        *,
        key=None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.width = width
        self.height = height
        self.child = child

    @named_constructor
    def expand(cls, *, key=None, child: Optional[Widget] = None):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.width = float("inf")
        instance.height = float("inf")
        instance.child = child
        return instance

    @named_constructor
    def shrink(cls, *, key=None, child: Optional[Widget] = None):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.width = 0.0
        instance.height = 0.0
        instance.child = child
        return instance

    @named_constructor
    def fromSize(
        cls, *, key=None, child: Optional[Widget] = None, size: Optional[Size] = None
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.width = size.width if size is not None else None
        instance.height = size.height if size is not None else None
        instance._fromSize_size = size
        instance.child = child
        return instance

    @named_constructor
    def square(
        cls,
        *,
        key=None,
        child: Optional[Widget] = None,
        dimension: Optional[float] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.width = dimension
        instance.height = dimension
        instance._square_dimension = dimension
        instance.child = child
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self._flut_init == "fromSize":
            size = getattr(self, "_fromSize_size", None)
            if size is not None:
                result["size"] = _flut_pack_value(size)
        elif self._flut_init == "square":
            dimension = getattr(self, "_square_dimension", None)
            if dimension is not None:
                result["dimension"] = _flut_pack_value(dimension)
        elif self._flut_init is None:
            if self.width is not None:
                result["width"] = _flut_pack_value(self.width)
            if self.height is not None:
                result["height"] = _flut_pack_value(self.height)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class Column(Widget):
    _flut_type = "Column"

    def __init__(
        self,
        *,
        key=None,
        mainAxisAlignment: MainAxisAlignment = MainAxisAlignment.start,
        mainAxisSize: MainAxisSize = MainAxisSize.max,
        crossAxisAlignment: CrossAxisAlignment = CrossAxisAlignment.center,
        textDirection: Optional[TextDirection] = None,
        verticalDirection: VerticalDirection = VerticalDirection.down,
        textBaseline: Optional[TextBaseline] = None,
        spacing: float = 0.0,
        children: list[Widget] = [],
    ):
        super().__init__(key=key)
        self.mainAxisAlignment = mainAxisAlignment
        self.mainAxisSize = mainAxisSize
        self.crossAxisAlignment = crossAxisAlignment
        self.textDirection = textDirection
        self.verticalDirection = verticalDirection
        self.textBaseline = textBaseline
        self.spacing = spacing
        self.children = children

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["children"] = _flut_pack_value(self.children)
        result["mainAxisAlignment"] = _flut_pack_value(self.mainAxisAlignment)
        result["mainAxisSize"] = _flut_pack_value(self.mainAxisSize)
        result["crossAxisAlignment"] = _flut_pack_value(self.crossAxisAlignment)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        result["verticalDirection"] = _flut_pack_value(self.verticalDirection)
        if self.textBaseline is not None:
            result["textBaseline"] = _flut_pack_value(self.textBaseline)
        result["spacing"] = _flut_pack_value(self.spacing)
        return result


class Row(Widget):
    _flut_type = "Row"

    def __init__(
        self,
        *,
        key=None,
        mainAxisAlignment: MainAxisAlignment = MainAxisAlignment.start,
        mainAxisSize: MainAxisSize = MainAxisSize.max,
        crossAxisAlignment: CrossAxisAlignment = CrossAxisAlignment.center,
        textDirection: Optional[TextDirection] = None,
        verticalDirection: VerticalDirection = VerticalDirection.down,
        textBaseline: Optional[TextBaseline] = None,
        spacing: float = 0.0,
        children: list[Widget] = [],
    ):
        super().__init__(key=key)
        self.mainAxisAlignment = mainAxisAlignment
        self.mainAxisSize = mainAxisSize
        self.crossAxisAlignment = crossAxisAlignment
        self.textDirection = textDirection
        self.verticalDirection = verticalDirection
        self.textBaseline = textBaseline
        self.spacing = spacing
        self.children = children

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["children"] = _flut_pack_value(self.children)
        result["mainAxisAlignment"] = _flut_pack_value(self.mainAxisAlignment)
        result["mainAxisSize"] = _flut_pack_value(self.mainAxisSize)
        result["crossAxisAlignment"] = _flut_pack_value(self.crossAxisAlignment)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        result["verticalDirection"] = _flut_pack_value(self.verticalDirection)
        if self.textBaseline is not None:
            result["textBaseline"] = _flut_pack_value(self.textBaseline)
        result["spacing"] = _flut_pack_value(self.spacing)
        return result


class Stack(Widget):
    _flut_type = "Stack"

    def __init__(
        self,
        *,
        key=None,
        alignment: AlignmentDirectional = AlignmentDirectional.topStart,
        textDirection: Optional[TextDirection] = None,
        fit: StackFit = StackFit.loose,
        clipBehavior: Clip = Clip.hardEdge,
        children: list[Widget] = [],
    ):
        super().__init__(key=key)
        self.alignment = alignment
        self.textDirection = textDirection
        self.fit = fit
        self.clipBehavior = clipBehavior
        self.children = children

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["alignment"] = _flut_pack_value(self.alignment)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        result["fit"] = _flut_pack_value(self.fit)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        result["children"] = _flut_pack_value(self.children)
        return result


class Positioned(Widget):
    _flut_type = "Positioned"

    def __init__(
        self,
        *,
        key=None,
        left: Optional[float] = None,
        top: Optional[float] = None,
        right: Optional[float] = None,
        bottom: Optional[float] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        child,
    ):
        super().__init__(key=key)
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.left is not None:
            result["left"] = _flut_pack_value(self.left)
        if self.top is not None:
            result["top"] = _flut_pack_value(self.top)
        if self.right is not None:
            result["right"] = _flut_pack_value(self.right)
        if self.bottom is not None:
            result["bottom"] = _flut_pack_value(self.bottom)
        if self.width is not None:
            result["width"] = _flut_pack_value(self.width)
        if self.height is not None:
            result["height"] = _flut_pack_value(self.height)
        result["child"] = _flut_pack_value(self.child)
        return result


class MouseRegion(Widget):
    _flut_type = "MouseRegion"

    def __init__(
        self,
        *,
        key=None,
        onEnter=None,
        onExit=None,
        onHover=None,
        cursor: MouseCursor = MouseCursor.defer,
        opaque: bool = True,
        hitTestBehavior=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.onEnter = onEnter
        self.onExit = onExit
        self.onHover = onHover
        self.cursor = cursor
        self.opaque = opaque
        self.hitTestBehavior = hitTestBehavior
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["cursor"] = _flut_pack_value(self.cursor)
        result["opaque"] = _flut_pack_value(self.opaque)
        if self.onEnter is not None:
            result["onEnter"] = self._register_action(
                self.onEnter, "PointerEnterEventListener"
            )._flut_pack()
        if self.onExit is not None:
            result["onExit"] = self._register_action(
                self.onExit, "PointerExitEventListener"
            )._flut_pack()
        if self.onHover is not None:
            result["onHover"] = self._register_action(
                self.onHover, "PointerHoverEventListener"
            )._flut_pack()
        if self.hitTestBehavior is not None:
            result["hitTestBehavior"] = _flut_pack_value(self.hitTestBehavior)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class Padding(Widget):
    _flut_type = "Padding"

    def __init__(self, *, key=None, padding, child: Optional[Widget] = None):
        super().__init__(key=key)
        self.padding = padding
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["padding"] = _flut_pack_value(self.padding)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class Align(Widget):
    _flut_type = "Align"

    def __init__(
        self,
        *,
        key=None,
        alignment: Alignment = Alignment.center,
        widthFactor: Optional[float] = None,
        heightFactor: Optional[float] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.alignment = alignment
        self.widthFactor = widthFactor
        self.heightFactor = heightFactor
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["alignment"] = _flut_pack_value(self.alignment)
        if self.widthFactor is not None:
            result["widthFactor"] = _flut_pack_value(self.widthFactor)
        if self.heightFactor is not None:
            result["heightFactor"] = _flut_pack_value(self.heightFactor)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class Opacity(Widget):
    _flut_type = "Opacity"

    def __init__(
        self,
        *,
        key=None,
        opacity: float,
        alwaysIncludeSemantics: bool = False,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.opacity = opacity
        self.alwaysIncludeSemantics = alwaysIncludeSemantics
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["opacity"] = _flut_pack_value(self.opacity)
        result["alwaysIncludeSemantics"] = _flut_pack_value(self.alwaysIncludeSemantics)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class ClipRRect(Widget):
    _flut_type = "ClipRRect"

    def __init__(
        self,
        *,
        key=None,
        borderRadius: BorderRadius = BorderRadius.circular(0),
        clipper=None,
        clipBehavior: Clip = Clip.antiAlias,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.borderRadius = borderRadius
        self.clipper = clipper
        self.clipBehavior = clipBehavior
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["borderRadius"] = _flut_pack_value(self.borderRadius)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.clipper is not None:
            result["clipper"] = _flut_pack_value(self.clipper)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class Wrap(Widget):
    _flut_type = "Wrap"

    def __init__(
        self,
        *,
        key=None,
        direction: Axis = Axis.horizontal,
        alignment: WrapAlignment = WrapAlignment.start,
        spacing: float = 0.0,
        runAlignment: WrapAlignment = WrapAlignment.start,
        runSpacing: float = 0.0,
        crossAxisAlignment: WrapCrossAlignment = WrapCrossAlignment.start,
        textDirection: Optional[TextDirection] = None,
        verticalDirection: VerticalDirection = VerticalDirection.down,
        clipBehavior: Clip = Clip.none,
        children: list[Widget] = [],
    ):
        super().__init__(key=key)
        self.direction = direction
        self.alignment = alignment
        self.spacing = spacing
        self.runAlignment = runAlignment
        self.runSpacing = runSpacing
        self.crossAxisAlignment = crossAxisAlignment
        self.textDirection = textDirection
        self.verticalDirection = verticalDirection
        self.clipBehavior = clipBehavior
        self.children = children

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["direction"] = _flut_pack_value(self.direction)
        result["alignment"] = _flut_pack_value(self.alignment)
        result["spacing"] = _flut_pack_value(self.spacing)
        result["runAlignment"] = _flut_pack_value(self.runAlignment)
        result["runSpacing"] = _flut_pack_value(self.runSpacing)
        result["crossAxisAlignment"] = _flut_pack_value(self.crossAxisAlignment)
        result["verticalDirection"] = _flut_pack_value(self.verticalDirection)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.textDirection is not None:
            result["textDirection"] = _flut_pack_value(self.textDirection)
        result["children"] = _flut_pack_value(self.children)
        return result


class Transform(Widget):
    _flut_type = "Transform"

    def __init__(
        self,
        *,
        key=None,
        transform,
        origin=None,
        alignment=None,
        transformHitTests: bool = True,
        filterQuality=None,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.transform = transform
        self.origin = origin
        self.alignment = alignment
        self.transformHitTests = transformHitTests
        self.filterQuality = filterQuality
        self.child = child

    @named_constructor
    def rotate(
        cls,
        *,
        key=None,
        angle: float,
        origin=None,
        alignment=None,
        transformHitTests: bool = True,
        filterQuality=None,
        child: Optional[Widget] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.angle = angle
        instance.origin = origin
        instance.alignment = alignment
        instance.transformHitTests = transformHitTests
        instance.filterQuality = filterQuality
        instance.child = child
        return instance

    @named_constructor
    def scale(
        cls,
        *,
        key=None,
        scale: Optional[float] = None,
        scaleX: Optional[float] = None,
        scaleY: Optional[float] = None,
        origin=None,
        alignment=None,
        transformHitTests: bool = True,
        filterQuality=None,
        child: Optional[Widget] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.scale = scale
        instance.scaleX = scaleX
        instance.scaleY = scaleY
        instance.origin = origin
        instance.alignment = alignment
        instance.transformHitTests = transformHitTests
        instance.filterQuality = filterQuality
        instance.child = child
        return instance

    @named_constructor
    def translate(
        cls,
        *,
        key=None,
        offset: Offset,
        transformHitTests: bool = True,
        filterQuality=None,
        child: Optional[Widget] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.offset = offset
        instance.origin = None
        instance.alignment = None
        instance.transformHitTests = transformHitTests
        instance.filterQuality = filterQuality
        instance.child = child
        return instance

    @named_constructor
    def flip(
        cls,
        *,
        key=None,
        flipX: bool = False,
        flipY: bool = False,
        origin=None,
        transformHitTests: bool = True,
        filterQuality=None,
        child: Optional[Widget] = None,
    ):
        instance = cls.__new__(cls)
        Widget.__init__(instance, key=key)
        instance.flipX = flipX
        instance.flipY = flipY
        instance.origin = origin
        instance.alignment = None
        instance.transformHitTests = transformHitTests
        instance.filterQuality = filterQuality
        instance.child = child
        return instance

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.origin is not None:
            result["origin"] = _flut_pack_value(self.origin)
        if self.alignment is not None:
            result["alignment"] = _flut_pack_value(self.alignment)
        result["transformHitTests"] = _flut_pack_value(self.transformHitTests)
        if self.filterQuality is not None:
            result["filterQuality"] = _flut_pack_value(self.filterQuality)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        if self._flut_init is None:
            result["transform"] = _flut_pack_value(self.transform)
        if self._flut_init == "rotate":
            result["angle"] = _flut_pack_value(self.angle)
        if self._flut_init == "scale":
            if self.scale is not None:
                result["scale"] = _flut_pack_value(self.scale)
            if self.scaleX is not None:
                result["scaleX"] = _flut_pack_value(self.scaleX)
            if self.scaleY is not None:
                result["scaleY"] = _flut_pack_value(self.scaleY)
        if self._flut_init == "translate":
            result["offset"] = _flut_pack_value(self.offset)
        if self._flut_init == "flip":
            result["flipX"] = _flut_pack_value(self.flipX)
            result["flipY"] = _flut_pack_value(self.flipY)
        return result


class Builder(Widget):
    _flut_type = "Builder"

    def __init__(self, *, key=None, builder: Callable[[BuildContext], Widget]):
        super().__init__(key=key)
        self.builder = builder

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["builder"] = self._register_build_action(
            wrap_widget_builder(self.builder), "WidgetBuilder"
        )._flut_pack()
        return result


class AspectRatio(Widget):
    _flut_type = "AspectRatio"

    def __init__(self, *, key=None, aspectRatio: float, child: Optional[Widget] = None):
        super().__init__(key=key)
        self.aspectRatio = aspectRatio
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["aspectRatio"] = _flut_pack_value(self.aspectRatio)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class FittedBox(Widget):
    _flut_type = "FittedBox"

    def __init__(
        self,
        *,
        key=None,
        fit: BoxFit = BoxFit.contain,
        alignment: Alignment = Alignment.center,
        clipBehavior: Clip = Clip.none,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.fit = fit
        self.alignment = alignment
        self.clipBehavior = clipBehavior
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["fit"] = _flut_pack_value(self.fit)
        result["alignment"] = _flut_pack_value(self.alignment)
        result["clipBehavior"] = _flut_pack_value(self.clipBehavior)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class ConstrainedBox(Widget):
    _flut_type = "ConstrainedBox"

    def __init__(
        self, *, key=None, constraints: BoxConstraints, child: Optional[Widget] = None
    ):
        super().__init__(key=key)
        self.constraints = constraints
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["constraints"] = _flut_pack_value(self.constraints)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class SliverPadding(Widget):
    _flut_type = "SliverPadding"

    def __init__(self, *, key=None, padding, sliver: Optional[Widget] = None):
        super().__init__(key=key)
        self.padding = padding
        self.sliver = sliver

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["padding"] = _flut_pack_value(self.padding)
        if self.sliver is not None:
            result["sliver"] = _flut_pack_value(self.sliver)
        return result


class SliverToBoxAdapter(Widget):
    _flut_type = "SliverToBoxAdapter"

    def __init__(self, *, key=None, child: Optional[Widget] = None):
        super().__init__(key=key)
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result


class CustomPaint(Widget):
    _flut_type = "CustomPaint"

    def __init__(
        self,
        *,
        key=None,
        painter: Optional[CustomPainter] = None,
        foregroundPainter: Optional[CustomPainter] = None,
        size: Size = Size(0, 0),
        isComplex: bool = False,
        willChange: bool = False,
        child: Optional[Widget] = None,
    ):
        super().__init__(key=key)
        self.painter = painter
        self.foregroundPainter = foregroundPainter
        self.size = size
        self.isComplex = isComplex
        self.willChange = willChange
        self.child = child

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["size"] = _flut_pack_value(self.size)
        result["isComplex"] = _flut_pack_value(self.isComplex)
        result["willChange"] = _flut_pack_value(self.willChange)
        if self.painter is not None:
            result["painter"] = _flut_pack_value(self.painter)
        if self.foregroundPainter is not None:
            result["foregroundPainter"] = _flut_pack_value(self.foregroundPainter)
        if self.child is not None:
            result["child"] = _flut_pack_value(self.child)
        return result
