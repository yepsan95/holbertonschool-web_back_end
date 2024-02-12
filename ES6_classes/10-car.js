export default class Car {
  constructor(brand, motor, color) {
    if (typeof (brand) !== 'string') {
      throw TypeError('brand must be a string');
    }
    if (typeof (motor) !== 'string') {
      throw TypeError('motor must be a string');
    }
    if (typeof (color) !== 'string') {
      throw TypeError('color must be a string');
    }
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return new this.constructor();
  }
}
