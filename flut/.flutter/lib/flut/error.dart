class FlutRuntimeException implements Exception {
  final String? message;
  FlutRuntimeException([this.message]);

  @override
  String toString() => message != null
      ? 'FlutRuntimeException: $message'
      : 'FlutRuntimeException';
}

class FlutMissingRequiredParameterException extends FlutRuntimeException {
  final String widgetType;
  final String paramName;

  FlutMissingRequiredParameterException(this.widgetType, this.paramName)
    : super();

  @override
  String toString() =>
      'FlutMissingRequiredParameterException: $widgetType.$paramName';
}

class FlutUnknownTypeException extends FlutRuntimeException {
  final String type;

  FlutUnknownTypeException(this.type) : super();

  @override
  String toString() => 'FlutUnknownTypeException: $type';
}

class FlutUnknownPropertyException extends FlutRuntimeException {
  final String type;
  final String property;

  FlutUnknownPropertyException(this.type, this.property) : super();

  @override
  String toString() => 'FlutUnknownPropertyException: $type.$property';
}

class FlutUnknownMethodException extends FlutRuntimeException {
  final String method;

  FlutUnknownMethodException(this.method) : super();

  @override
  String toString() => 'FlutUnknownMethodException: $method';
}

// TODO: remove this
class FlutInvalidValueException extends FlutRuntimeException {
  final String type;
  final dynamic value;

  FlutInvalidValueException(this.type, this.value) : super();

  @override
  String toString() => 'FlutInvalidValueException: $type=$value';
}

class FlutOidConflictException extends FlutRuntimeException {
  final int existingOid;
  final int requestedOid;

  FlutOidConflictException(this.existingOid, this.requestedOid) : super();

  @override
  String toString() =>
      'FlutOidConflictException: existing=$existingOid, requested=$requestedOid';
}

class FlutOidInUseException extends FlutRuntimeException {
  final int oid;

  FlutOidInUseException(this.oid) : super();

  @override
  String toString() => 'FlutOidInUseException: $oid';
}

class FlutEncodeException extends FlutRuntimeException {
  final Type type;

  FlutEncodeException(this.type) : super();

  @override
  String toString() => 'FlutEncodeException: $type';
}
