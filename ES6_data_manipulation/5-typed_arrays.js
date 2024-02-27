export default function createInt8TypedArray(length, position, value) {
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const int8View = new DataView(buffer, 0);
  int8View.seInt8(position, value);
  return int8View;
}
